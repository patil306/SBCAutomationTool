from  uasession import UASession
from sipconstants import CRLF, SipHeaders, SipRespCodeMap, SDPState
from parserandbuilder import parseHeaders, parseContent, buildMessage, buildContent
from util import createToTag, getMyHostIP, genRSeq
import copy
from media import Media, procSDPAndGetMediaParams, procSDPAndGetMedDirection
from time import sleep
import socket,sys, errno

def handleInvite(uaSession:UASession, raw_message, port):
    sip_msg = raw_message.split(CRLF+CRLF)
    sig_msg = sip_msg[0]
    sdp_msg = sip_msg[1] if len(sip_msg) > 1 else ""
    rcvdInvite = parseHeaders(sig_msg)
    callid = rcvdInvite.getCallID().strip()
    uaSession.setCallID(callid)
    uaSession.setToHeader(rcvdInvite.getHeader(SipHeaders.FROM.value))
    uaSession.setFromHeader(rcvdInvite.getHeader(SipHeaders.TO.value))
    uaSession.setRemoteTarget(rcvdInvite.getHeader(SipHeaders.CONTACT.value))
    uaSession.setRemoteTag(rcvdInvite.getFromTag())
    uaSession.setDialogOwner(False)
    uaSession.setRouteSet(rcvdInvite.getRouteSet(False))
    uaSession.addMsgObj("INVITE", rcvdInvite)
    try:
        if sdp_msg:
            sdp = parseContent(sdp_msg)
            uaSession.setRemoteSDP(sdp)
            #
            uaSession.setSDPstate(SDPState.SDP_RCVD.value)
            #
        provResp = copy.deepcopy(rcvdInvite)
        respcode = "180"
        respText = SipRespCodeMap.get(respcode)
        provResp.setResponseLine(f'SIP/2.0 {respcode} {respText}')
        to_tag = createToTag()
        uaSession.setLocalTag(to_tag)
        hdr_to = uaSession.getFromHeader() + f';tag={to_tag}'
        provResp.replaceHeader(SipHeaders.TO.value, hdr_to)
        uaSession.setFromHeader(provResp.getHeader(SipHeaders.TO.value))
        my_ext = uaSession.getFromUserPart()
        my_IP = getMyHostIP()
        scheme = uaSession.getScheme()
        hdr_contact = f'<{scheme}:{my_ext}@{my_IP}>'
        provResp.replaceHeader(SipHeaders.CONTACT.value, hdr_contact)
        uaSession.setLocalContact(hdr_contact)
        if uaSession.isReliable():
            hdr_require = f'100rel'
            provResp.addHeader(SipHeaders.REQUIRE.value, hdr_require)
            rseq = uaSession.getRSeq() if uaSession.getRSeq() else genRSeq()
            uaSession.setRSeq(rseq)
            provResp.addHeader(SipHeaders.RSEQ.value, rseq)
        content_len =  0
        provResp.replaceHeader(SipHeaders.CONTENTLENGTH.value, content_len)
        if content_len > 0: provResp.replaceHeader(SipHeaders.CONTENTTYPE.value, 'application/sdp')
        raw_message = buildMessage(provResp, "")

        #print(sock_obj)
        try:
            sock_obj = uaSession.getSigSocket()
            sock_obj.sendMessage(raw_message)
        except socket.error as e:
            print("socket error in sending 180 ", e)
        except IOError as e:
            if(e.errno == errno.EPIPE):
                print("IO error in 180 sending ignoring :-", e)
                pass
        except:
            print("sending invite 180 failed")
            pass

        #

        #
        if not uaSession.isReliable():
            sendInv200(uaSession, port)

    except:
        print("something wrong in handleInvite")


def handlePrack(sipCallId_map, raw_msg):
    raw_msg = raw_msg.split(CRLF + CRLF)
    prack_msg = parseHeaders(raw_msg[0])
    uaSession:UASession = sipCallId_map.get(prack_msg.getCallID())
    uaSession.addMsgObj('PRACK', prack_msg)
    prack200_msg = copy.deepcopy(prack_msg)
    resp_line = f'SIP/2.0 200 OK'
    prack200_msg.setResponseLine(resp_line)
    my_ext = uaSession.getUserName()
    my_IP = getMyHostIP()
    scheme = uaSession.getScheme()
    hdr_contact = f'{scheme}:{my_ext}@{my_IP}'
    prack200_msg.replaceHeader(SipHeaders.CONTACT.value, hdr_contact)
    raw_msg = buildMessage(prack200_msg, "")
    sock_obj = uaSession.getSigSocket()
    #print(sock_obj)
    sock_obj.sendMessage(raw_msg)
    sendInv200(uaSession)

def handleAck(sipCallId_map, raw_msg):
    raw_msg = raw_msg.split(CRLF + CRLF)
    ack_msg = parseHeaders(raw_msg[0])
    callId = ack_msg.getCallID().strip()
    uaSession:UASession = sipCallId_map.get(callId)
    uaSession.setSessionComplete(True)
    uaSession.addMsgObj("ACK", ack_msg)
    ###########################################
    try:
        rem_sdp = uaSession.getRemoteSDP()
        loc_sdp = uaSession.getLocalSDP()
        rem_medIP, rem_medport, rem_meddir, pref_audiocodec, rxKey = procSDPAndGetMediaParams(rem_sdp)
        loc_medip, loc_medport, loc_meddir, pref_audiocodec, txKey = procSDPAndGetMediaParams(loc_sdp)
        media_obj = Media(loc_medip, loc_medport, rem_medIP, rem_medport)
        media_dir = "sendrecv" if rem_meddir == "sendrecv" and loc_meddir == "sendrecv" else "inactive"
        uaSession.setMediaObject(media_obj)
        media_obj.initiateMedia(media_dir, pref_audiocodec, txKey, rxKey)
    except:
        print("exception in handling ACK")
''' print("***")
    uaSession.setSipCallState(SipCallState.COMPLETE.value)
    uaSession.setActiveCall(True)
    print(uaSession.getSDPState())
    if uaSession.getSDPState() == SDPState.COMPLETE.value or uaSession.getSDPState() == 0:
        print(uaSession.getMediaObject())
        if not uaSession.getMediaObject():
            rem_sdp = uaSession.getRemoteSDP()
            loc_sdp = uaSession.getLocalSDP()
            print(rem_sdp)
            print("++++")
            print(loc_sdp)
            rem_medIP, rem_medport, rem_meddir, pref_audiocodec, rxKey = procSDPAndGetMediaParams(rem_sdp)
            loc_medip, loc_medport, loc_meddir, pref_audiocodec, txKey = procSDPAndGetMediaParams(loc_sdp)
            print(loc_medport)
            print(rem_medport)
            media_obj = Media(loc_medip, loc_medport, rem_medIP, rem_medport)
            media_dir = "sendrecv" if rem_meddir == "sendrecv" and loc_meddir == "sendrecv" else "inactive"
            uaSession.setMediaObject(media_obj)
            media_obj.initiateMedia(media_dir, pref_audiocodec, txKey, rxKey)'''

def sendInv200(uaSession:UASession, port):
    global curr_port
    inv_msg = uaSession.getMsgObj("INVITE")
    msg_200OK = copy.deepcopy(inv_msg)
    resp_line = f'SIP/2.0 200 OK'
    msg_200OK.setResponseLine(resp_line)
    hdr_contact = uaSession.getLocalContact()
    msg_200OK.replaceHeader(SipHeaders.CONTACT.value, hdr_contact)
    hdr_to = uaSession.getFromHeader()
    msg_200OK.replaceHeader(SipHeaders.TO.value, hdr_to)
    content = buildContent(uaSession, port)
    content_len = len(content)
    msg_200OK.replaceHeader(SipHeaders.CONTENTLENGTH.value, content_len)
    sdp_obj = parseContent(content)
    uaSession.setLocalSDP(sdp_obj)
    #
    uaSession.setSDPstate(SDPState.SDP_SENT.value)
    #
    raw_msg = buildMessage(msg_200OK, content)
    #print(sock_obj)
    try:
        sock_obj = uaSession.getSigSocket()
        sock_obj.sendMessage(raw_msg)
    except socket.error as e:
        print("socket error in sending 200 ", e)
    except IOError as e:
        if (e.errno == errno.EPIPE):
            print("IO error in 200 sending ignoring :-", e)
            pass
    except:
        print("sending invite 200 failed")
        pass

def handleBye(sipCallId_map, raw_msg):
    raw_msg = raw_msg.split(CRLF + CRLF)
    bye_msg = parseHeaders(raw_msg[0])
    uaSession: UASession = sipCallId_map.get(bye_msg.getCallID().strip())
    uaSession.addMsgObj('BYE', bye_msg)
    bye200_msg = copy.deepcopy(bye_msg)
    resp_line = f'SIP/2.0 200 OK'
    bye200_msg.setResponseLine(resp_line)
    hdr_contact = uaSession.getLocalContact()
    bye200_msg.replaceHeader(SipHeaders.CONTACT.value, hdr_contact)
    raw_msg = buildMessage(bye200_msg, "")
    #print(sock_obj)
    try:
        sock_obj = uaSession.getSigSocket()
        sock_obj.sendMessage(raw_msg)
    except socket.error as e:
        print("socket error in sending 200 bye ", e)
    except IOError as e:
        if (e.errno == errno.EPIPE):
            print("IO error in 200 bye sending ignoring :-", e)
            pass
    except:
        print("sending bye 200 failed")
        pass












