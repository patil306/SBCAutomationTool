from collections import OrderedDict
import listenthread
from transport import SignalingSocket
from messagebuffer import MessageBuffer
from util import isStopTraffic, stopTraffic, isTrafficOn, Util
from uac import sendInvite, sendPrack, handleProvResponse, handle200OK, sendAck, sendBye
from uas import handleInvite, handlePrack, handleAck, handleBye
from parserandbuilder import parseHeaders
from uasession import UASession
from sipconstants import CRLF, SipHeaders, SipCallState, SDPState, Transport
import unexpectedmessage
import time
# import json
from hashlib import md5
import threading
import queue
import sys, getopt, errno
import socket
import datetime
import logging
logging.basicConfig(filename='example.log', level=logging.WARNING)
#logging.basicConfig(filename='/home/ubuntu/app.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
def main():
    local_ip, outbound_ip, domain = "", "", ""
    wait_time = 180
    transport = "tcp"
    num_sessions = 1000
    caller, callee = None, None
    isUac = True
    isReliable = False
    remote_port = 5060
    machine_call_id = "1000"
    opts, args = getopt.getopt(sys.argv[1:], "i:r:d:s:w:p:t", ["uac", "UAC", "uas", "UAS", "rel", "clr=", "cle="])
    for opt, value in opts:
        if opt == "-i":
            local_ip = value
        elif opt == "-r":
            outbound_ip = value
        elif opt == "-t":
            transport = Transport.TCP.value
        elif opt == "-d":
            domain = value
        elif opt == "-p":
            remote_port = int(value)
        elif opt == "-s":
            num_sessions = int(value)
        elif opt == "-w":
            machine_call_id = value
        elif opt == "--clr":
            caller = int(value)
        elif opt == "--cle":
            callee = int(value)
        elif opt in ["--uac", "--UAC"]:
            isUac = True
        elif opt in ["--uas", "--UAS"]:
            isUac = False
        elif opt in ["--rel"]:
            isReliable = True

    call_count = 0
    sipCallId_map = OrderedDict()
    msg_q = queue.Queue()
    Util._hostIP = local_ip
    msg_buffer = MessageBuffer()
    sigSocket = SignalingSocket(local_ip, 5060, outbound_ip, remote_port, transport)
    print("tcp handshake should start here")
    if isUac:
        sigSocket.connectSocket()

    time.sleep(1)
    listen_thread = listenthread.ListenThread()
    chThread_ListenSig = threading.Thread(target=listen_thread.startListening, args=(sigSocket, msg_buffer, isUac))
    chThread_ListenSig.start()
    chThread_readBuff = threading.Thread(target=msg_buffer.readFromStringBuffer)
    chThread_readBuff.start()
    callFailed_cnt = 0
    callSuccess_cnt = 0
    callResp_cnt = 0
    chThread_loadRunner = None
    chThread_monitorSipCall = None
    chThread_RtpRecvr = threading.Thread(target=startReceivingMedia, args=(local_ip, 18, "", num_sessions))
    chThread_RtpRecvr.start()
    isTrafficComplete = False
    end_time = time.time() + num_sessions + 200
    if isUac:
        chThread_loadRunner = threading.Thread(target=startTraffic, args=(
        sipCallId_map, msg_q, sigSocket, num_sessions, caller, callee, domain, isReliable, machine_call_id))
        chThread_loadRunner.start()
        chThread_monitorSipCall = threading.Thread(target=monitorSipCall,args=(sipCallId_map, msg_q, num_sessions, wait_time, isTrafficComplete))
        chThread_monitorSipCall.start()
    try:
        bye_count = 0
        port = 60000
        while True:
            if isTrafficComplete:
                break
            if (time.time() > end_time):
                break
            buff_evt, raw_msg = msg_buffer.popTopMessage()
            if buff_evt == "100":
                pass
            elif buff_evt == "INVITE":
                uaSession = UASession()
                uaSession.setSigSocket(sigSocket)
                uaSession.setReliable(isReliable)

                handleInvite(uaSession, raw_msg, port)
                sipCallId_map[uaSession.getCallID()] = uaSession
                callResp_cnt += 1
                # port += 1
            elif buff_evt in ['180', '183']:
                handleProvResponse(sipCallId_map, raw_msg)
            elif buff_evt == 'PRACK':
                handlePrack(sipCallId_map, raw_msg)
            elif buff_evt == '200':
                msg_200 = handle200OK(sipCallId_map, raw_msg)
                uaSession = sipCallId_map.get(msg_200.getCallID().strip())
                if msg_200.getMethod() == "INVITE":
                    # ACK has been sent while handling the 200 OK to INVITE.
                    if uaSession.isSessionComplete():
                        callSuccess_cnt += 1
                        msg_q.put(uaSession)
                        # print("------ Total Successful Calls: ",callSuccess_cnt,
                        #   "++++++ Total Failed Calls: ",callFailed_cnt)
                elif msg_200.getMethod() == "BYE":
                    bye_count += 1
                    '''if bye_count >= 10000:
                       print("**** Bye count 10, breaking")
                       break'''
            elif buff_evt == "ACK":
                handleAck(sipCallId_map, raw_msg)
                callSuccess_cnt += 1
                # print("------ Total Successful Calls: ", callSuccess_cnt,
                #     "++++++ Total Failed Calls: ", callFailed_cnt)
            elif buff_evt == "BYE":
                handleBye(sipCallId_map, raw_msg)
                bye_count += 1
                #
                raw_msgx = raw_msg.split(CRLF + CRLF)
                bye_msgx = parseHeaders(raw_msgx[0])
                call_idx = bye_msgx.getCallID().strip()
                if (call_idx):
                    sipCallId_map.pop(call_idx)
                    # print("removing from dict")
                else:
                    pass

                '''if(bye_count >= 10000):
                    break'''

                #if callResp_cnt == bye_count:
                #    break
                #
                #if bye_count == call_count:
                #    break
            elif (buff_evt.startswith("4") or buff_evt.startswith("5")):
                # this is indication of call failure if it is uac
                if isUac:
                    callFailed_cnt += 1
                    # raw_msg_sig = raw_msg.split(CRLF+CRLF)[0]
                    try:
                        err_msg = parseHeaders(raw_msg)
                        callId = err_msg.getCallID()
                        uaSession = sipCallId_map.get(callId)
                        if (uaSession):
                            sendAck(uaSession, False)
                    except:
                        # print("4xx or 5xx recived and ignoring")
                        pass
                    # print("------ Total Successful Calls: ", callSuccess_cnt,
                    #      "++++++ Total Failed Calls: ", callFailed_cnt)

    finally:
        print("******", datetime.datetime.now())
        print("****** IN Finally")
        print("****** Total call count ", callResp_cnt, "------ Total Successful Calls: ", callSuccess_cnt, "++++++ Total Failed Calls: ", callFailed_cnt, "+++Total cleared calls ", bye_count)
        logging.warning("****** Total call count %s", callResp_cnt)
        logging.warning("------ Total Successful Calls: %s", callSuccess_cnt)
        logging.warning("++++++ Total Failed Calls: %s", callFailed_cnt) 
        logging.warning("+++Total cleared calls %s", bye_count)
        listen_thread.setStopThread(True)
        msg_buffer.stopReading()
        chThread_ListenSig.join()
        chThread_readBuff.join()
        chThread_RtpRecvr.join()
        if isUac:
            print("****finally Under UAC waiting for thread to join")
            chThread_loadRunner.join()
            chThread_monitorSipCall.join()
        print("***closing socket***")
        if sigSocket:
            sigSocket.closeSocket()


def monitorSipCall(sipCallId_map, msg_q, num_sessions, wait_time, isTrafficComplete):
    # while True:
    #     if sipCallId_map:
    #         break
    # bye_count = 0
    # for k, v in sipCallId_map.items():
    #     while True:
    #         if v.isSessionComplete():
    #             delta = time.time() - v.getSessionStartTime()
    #             if delta >= wait_time:
    #                 sendBye(v)
    #                 bye_count += 1
    #                 break
    #             else:
    #                 time.sleep(wait_time-delta)
    #                 sendBye(v)
    #                 bye_count += 1
    #                 break
    bye_count = 0

    flag = True
    while True:
        if (flag):
            uaSession = msg_q.get()
            flag = False
        else:
            if (msg_q.empty()):
                print("******* Monitor thread -> Messege queue empty")
                time.sleep(180)
                if (msg_q.empty()):
                    print("**********Messge queue empty after 180 seconds")
                    break
            else:
                uaSession = msg_q.get()

        delta = time.time() - uaSession.getSessionStartTime()
        if delta >= wait_time:
            sendBye(uaSession)
            bye_count += 1

            # print("*****in if Bye sent no ", bye_count)
        else:
            time.sleep(wait_time - delta)
            sendBye(uaSession)
            bye_count += 1
            # print("*****Bye sent no ", bye_count)
        #
        callid = uaSession.getCallID()
        if (callid):
            sipCallId_map.pop(callid)
            # print("removing from dict")
        else:
            pass
            # print("didnot get callid")
        #
        # if bye_count == call_count:
        #   break
    isTrafficComplete = True
    print("*****Total BYE sent", bye_count)


def startTraffic(sipCallId_map, msg_q, sigSocket, num_sessions, caller, callee, domain, isReliable, machine_callid):
    call_pumped = 0
    i = 1000
    port = 60000
    #    for i in range(1, num_sessions+1):
    t_end = time.time() + num_sessions
    while time.time() < t_end:
        uaSession = UASession()
        uaSession.setSigSocket(sigSocket)
        callid = str(machine_callid) + str(i)
        uaSession.setCallID(callid)
        uaSession.setUserName(caller)
        uaSession.setTargetExtn(callee)
        uaSession.setDomain(domain)
        uaSession.setReliable(isReliable)
        # write code to send Invite with i as call-id
        # sendInvite(uaSession, port)
        uaSession.setSipCallState(SipCallState.INVITE_SENT.value)
        uaSession.setSDPstate(SDPState.SDP_SENT.value)
        cur_time = time.time()
        uaSession.setSessionStartTime(cur_time)
        sipCallId_map[callid] = uaSession
        sendInvite(uaSession, port)
        call_pumped += 1
        #       msg_q.put(uaSession)
        i += 1
        # port += 1
        time.sleep(0.1)
    #        break
    
    print(f'****{call_pumped} INVITE message Pumped')


###3rd march
def startReceivingMedia(myIp, prefaudiocodec, rxKey, num_sessions):
    myport = 60000
    __buffSize = 2048
    prefaudiocodec = int(prefaudiocodec)
    __recvSockId = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    local_host = (myIp, myport)
    __recvSockId.bind(local_host)
    # test_report = TestReport.getInstance()
    # print("=====Receiving Media====")
    recv_count = 0
    end_tme = time.time() + num_sessions + 200
    try:
        while time.time() < end_tme:
            __recvSockId.settimeout(2)
            try:
                rtp_packet, address = __recvSockId.recvfrom(__buffSize)
                recv_count += 1
                # rtp_string = rtp_packet.hex() if not rxKey else rtp_packet
                if rxKey:
                    key = base64.b64decode(rxKey)
                    rx_policy = Policy(key=key, ssrc_type=Policy.SSRC_ANY_INBOUND)
                    rx_session = Session(policy=rx_policy)
                    # rtp_string = rx_session.unprotect(rtp_string).hex()
                '''payload_string = getPayloadFromRtpString(rtp_string)
                if payload_string:
                    #print(payload_string)
                    pass
                    #test_report.setMediaReport(TestCaseResult.PASS.value)
                else:
                    pass'''
                # test_report.setMediaReport(TestCaseResult.FAIL.value)
                # rtp_map = decodeRTPpacket(rtp_string)
                # rcvd_payload = rtp_map.get('payload')
                # print("###### payload recevied", rcvd_payload)
                # my_payload = ""
                # if prefaudiocodec == 8:
                #     my_payload = "f3"*160
                # elif prefaudiocodec == 0:
                #     my_payload = "d5"*160
                #
                # if  rcvd_payload == my_payload:
                #     # print("MEDIA TEST PASS")
                #     test_report.setMediaReport(TestCaseResult.PASS.value)
                # else:
                #     test_report.setMediaReport(TestCaseResult.FAIL.value)
                # print("MEDIA TEST FAIL")
                # recv_count += 1
                # if recv_count == 5:
                #     print("5 packets received successfully")
                #     break
            except socket.timeout as e:
                err = e.args[0]
                if err == 'timed out':
                    # print("Recv Socket timeout, retry after 1sec")
                    time.sleep(1)
                    continue
                else:
                    print("SOCKET TIMEOUT ++++++")
                    print(e)
                #    sys.exit(1)
            except socket.error as e:
                print("SOCKET error in user exception ", e)
                pass
            except IOError as e:
                if (e.errno == errno.EPIPE):
                    print("pipe error igonring")
                    pass
            except:
                print("unknown exception ")
                pass
    finally:
        print("RTP total packets recvd ", recv_count)
###
main()

# 155

