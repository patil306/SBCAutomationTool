from uasession import UASession
from sipmessage import SipMessage
from sipconstants import CRLF, SipHeaders, SDPState
from util import createFromTag, getMyHostIP, createBranchID
from parserandbuilder import buildContent, buildMessage, parseHeaders, parseContent
import copy
from media import Media, procSDPAndGetMediaParams, procSDPAndGetMedDirection
import socket,sys, errno


def sendInvite(uaSession: UASession, port):
    global curr_port
    oodInvite = SipMessage()
    oodInvite.setRequestLine(f'INVITE sip:{uaSession.getTargetExtn()}@{uaSession.getDomain()} SIP/2.0')
    hdr_callid = uaSession.getCallID()
    oodInvite.addHeader(SipHeaders.CALLID.value, hdr_callid)
    f_tag = createFromTag()
    hdr_frm = f'<sip:{uaSession.getUserName()}@{uaSession.getDomain()}>;tag={f_tag}'
    oodInvite.addHeader(SipHeaders.FROM.value, hdr_frm)
    hdr_to = f'<sip:{uaSession.getTargetExtn()}@{uaSession.getDomain()}>'
    oodInvite.addHeader(SipHeaders.TO.value, hdr_to)
    host_ip = getMyHostIP()
    branch_id = createBranchID()
    hdr_via = f'SIP/2.0/{uaSession.getTransport()} {host_ip};branch={branch_id}'
    oodInvite.addHeader(SipHeaders.VIA.value, hdr_via)
    hdr_contact = f'<sip:{uaSession.getUserName()}@{host_ip}>'
    oodInvite.addHeader(SipHeaders.CONTACT.value, hdr_contact)
    oodInvite.addHeader(SipHeaders.MAXFORWARDS.value, '70')
    oodInvite.addHeader(SipHeaders.CONTENTTYPE.value, 'application/sdp')
    cseq = uaSession.getLastCSeq() + 1
    hdr_cseq = f'{cseq} INVITE'
    oodInvite.addHeader(SipHeaders.CSEQ.value, hdr_cseq)
    uaSession.setCSeq(cseq)
    content = buildContent(uaSession, port)
    content_len = len(content)
    oodInvite.addHeader(SipHeaders.CONTENTLENGTH.value, content_len)
    featuretags = "100rel, timer"
    oodInvite.addHeader(SipHeaders.SUPPORTED.value, featuretags)
    allowedmethods = "INVITE, ACK, CANCEL, BYE, PRACK"
    oodInvite.addHeader(SipHeaders.ALLOW.value, allowedmethods)
    uaSession.setCurSipMessage(oodInvite)
    uaSession.addMsgObj("INVITE", oodInvite)
    uaSession.setLocalTag(f_tag)
    uaSession.setFromHeader(hdr_frm)
    uaSession.setDialogOwner(True)
    raw_message = buildMessage(oodInvite, content)
    #
    if(content):
        sdp_obj = parseContent(content)
        #uaSession.setCurSDP(sdp_obj)
        uaSession.setLocalSDP(sdp_obj)
        uaSession.setSDPstate(SDPState.SDP_SENT.value)
        #
    try:
        sock_obg = uaSession.getSigSocket()
        sock_obg.sendMessage(raw_message)
    except socket.error as e:
        print("socket error in sending invite ", e)
    except IOError as e:
        if (e.errno == errno.EPIPE):
            print("IO error in invite sending ignoring :-", e)
            pass
    except:
        print("sending invite failed")
        pass

def handleProvResponse(sipCallId_map, raw_msg):
    raw_msg = raw_msg.split(CRLF + CRLF)
    sip_hdrs = raw_msg[0]
    sip_content = raw_msg[1] if len(raw_msg) > 1 else ""
    recv_provResp = parseHeaders(sip_hdrs)
    callid = recv_provResp.getCallID().strip()
    uaSession = sipCallId_map.get(str(callid))
    uaSession.setRemoteTarget(recv_provResp.getHeader(SipHeaders.CONTACT.value))
    uaSession.setRemoteTag(recv_provResp.getToTag())
    uaSession.setRouteSet(recv_provResp.getRouteSet(True))
    uaSession.setToHeader(recv_provResp.getHeader(SipHeaders.TO.value))
    uaSession.setFromHeader(recv_provResp.getHeader(SipHeaders.FROM.value))
    uaSession.setRSeq(recv_provResp.getRSeq())
    hdr_require = recv_provResp.getHeader(SipHeaders.REQUIRE.value)[0] if recv_provResp.getHeader(SipHeaders.REQUIRE.value) else ""
    if uaSession.isReliable() and hdr_require == "100rel":
        sendPrack(uaSession)

def sendPrack(uaSession:UASession):
    invMsg = uaSession.getMsgObj("INVITE")
    prack = copy.deepcopy(invMsg)
    contact_uri = uaSession.getRemoteURL()
    prack.setRequestLine(f'PRACK {contact_uri} SIP/2.0')
    branch_id = createBranchID()
    transport = uaSession.getTransport()
    my_ip = getMyHostIP()
    hdr_via = f'SIP/2.0/{transport} {my_ip};branch={branch_id}'
    prack.replaceHeader(SipHeaders.VIA.value, hdr_via)
    cseq = uaSession.getLastCSeq()
    hdr_cseq = f'{cseq} PRACK'
    prack.replaceHeader(SipHeaders.CSEQ.value, hdr_cseq)
    hdr_to = uaSession.getToHeader()
    prack.replaceHeader(SipHeaders.TO.value, hdr_to)
    cseq = invMsg.getCSeq()
    rseq = uaSession.getRSeq()
    hdr_rack = f'{rseq} {cseq} INVITE'
    prack.addHeader(SipHeaders.RACK.value, hdr_rack)
    prack.replaceHeader(SipHeaders.CONTENTLENGTH.value, 0)
    raw_msg = buildMessage(prack, "")
    sock_obj = uaSession.getSigSocket()
    sock_obj.sendMessage(raw_msg)

def handle200OK(sipCallId_map, raw_msg) -> UASession:
    raw_msg = raw_msg.split(CRLF + CRLF)
    sip_hdrs = raw_msg[0]
    sip_content = raw_msg[1] if len(raw_msg) > 1 else ""
    msg_200 = parseHeaders(sip_hdrs)
    callid = msg_200.getCallID().strip()
    uaSession = sipCallId_map.get(str(callid))
    if msg_200.getMethod() == "INVITE":
        handle200Invite(uaSession, msg_200, sip_content)
    elif msg_200.getMethod() == "PRACK":
        handle200Prack(uaSession, msg_200)
    return msg_200

def handle200Invite(uaSession:UASession, recv_200Inv, content):
    uaSession.setRemoteTarget(recv_200Inv.getHeader(SipHeaders.CONTACT.value))
    uaSession.setRemoteTag(recv_200Inv.getToTag())
    uaSession.setRouteSet(recv_200Inv.getRouteSet(True))
    #
    if content:
        sdp_obj = parseContent(content)
        uaSession.setRemoteSDP(sdp_obj)
        if uaSession.getSDPState() == SDPState.COMPLETE.value:
            pass
        else:
            uaSession.setSDPstate(SDPState.SDP_RCVD.value)
    #
    sendAck(uaSession)

def handle200Prack(uaSession:UASession, recv_200Prack):
    uaSession.setRemoteTarget(recv_200Prack.getHeader(SipHeaders.CONTACT.value))
    uaSession.setRemoteTag(recv_200Prack.getToTag())

def sendAck(uaSession:UASession, isMedia=True):
    inv_msg = uaSession.getMsgObj("INVITE")
    ack_msg = copy.deepcopy(inv_msg)
    ack_msg.setRequestLine(f'ACK {uaSession.getRemoteURL()} SIP/2.0')
    branch_id = createBranchID()
    transport = uaSession.getTransport()
    my_ip = getMyHostIP()
    hdr_via = f'SIP/2.0/{transport} {my_ip};branch={branch_id}'
    ack_msg.replaceHeader(SipHeaders.VIA.value, hdr_via)
    cseq = uaSession.getLastCSeq()
    hdr_cseq = f'{cseq} ACK'
    ack_msg.replaceHeader(SipHeaders.CSEQ.value, hdr_cseq)
    hdr_to = uaSession.getToHeader()
    ack_msg.replaceHeader(SipHeaders.TO.value, hdr_to)
    ack_msg.replaceHeader(SipHeaders.CONTENTLENGTH.value, 0)
    raw_msg = buildMessage(ack_msg, "")
    try:
        sock_obj = uaSession.getSigSocket()
        sock_obj.sendMessage(raw_msg)
        uaSession.setSessionComplete(True)
    except socket.error as e:
        print("socket error in sending ACK ", e)
    except IOError as e:
        if (e.errno == errno.EPIPE):
            print("IO error in ACK sending ignoring :-", e)
            pass
    except:
        print("sending invite ACK failed")
        pass
    uaSession.setSessionComplete(True)
    
    if(not isMedia):
        return
    ###

    rem_sdp = uaSession.getRemoteSDP()
    loc_sdp = uaSession.getLocalSDP()
    try:
        rem_medIP, rem_medport, rem_meddir, pref_audiocodec, rxKey = procSDPAndGetMediaParams(rem_sdp)
        loc_medip, loc_medport, loc_meddir, pref_audiocodec, txKey = procSDPAndGetMediaParams(loc_sdp)
        media_obj = Media(loc_medip, loc_medport, rem_medIP, rem_medport)
        media_dir = "sendrecv" if rem_meddir == "sendrecv" and loc_meddir == "sendrecv" else "inactive"
        uaSession.setMediaObject(media_obj)
        media_obj.initiateMedia(media_dir, pref_audiocodec, txKey, rxKey)
    except:
        print("Exception in sending ACK")
''' ###########################################
    uaSession.setSipCallState(SipCallState.COMPLETE.value)
    #uaSession.setActiveCall(True)
    print(uaSession.getSDPState())
    print("+++")
    if uaSession.getSDPState() == SDPState.COMPLETE.value:
        print("here")
        if not uaSession.getMediaObject():
            rem_sdp = uaSession.getRemoteSDP()
            loc_sdp = uaSession.getLocalSDP()
            print(rem_sdp)
            print(loc_sdp)
            print(buildContentFromSDP(rem_sdp))
            print(buildContentFromSDP(loc_sdp))
            rem_medIP, rem_medport, rem_meddir, pref_audiocodec, rxKey = procSDPAndGetMediaParams(rem_sdp)
            loc_medip, loc_medport, loc_meddir, pref_audiocodec, txKey = procSDPAndGetMediaParams(loc_sdp)
            print(loc_medip, loc_medport, rem_medIP, rem_medport, pref_audiocodec)
            media_obj = Media(loc_medip, loc_medport, rem_medIP, rem_medport)
            media_dir = "sendrecv" if rem_meddir == "sendrecv" and loc_meddir == "sendrecv" else "inactive"
            uaSession.setMediaObject(media_obj)
            media_obj.initiateMedia(media_dir, pref_audiocodec, txKey, rxKey)'''

def sendBye(uaSession:UASession):
    bye_msg = SipMessage()
    bye_msg.setRequestLine(f'BYE {uaSession.getRemoteURL()} SIP/2.0')
    hdr_callid = uaSession.getCallID()
    bye_msg.addHeader(SipHeaders.CALLID.value, hdr_callid)
    hdr_frm = uaSession.getFromHeader()
    bye_msg.addHeader(SipHeaders.FROM.value, hdr_frm)
    hdr_to = uaSession.getToHeader()
    bye_msg.addHeader(SipHeaders.TO.value, hdr_to)
    branch_id = createBranchID()
    hdr_via = f'SIP/2.0/{uaSession.getTransport()} {getMyHostIP()};branch={branch_id}'
    bye_msg.addHeader(SipHeaders.VIA.value, hdr_via)
    hdr_contact = f'<sip:{uaSession.getUserName()}@{getMyHostIP()}>'
    bye_msg.addHeader(SipHeaders.CONTACT.value, hdr_contact)
    bye_msg.addHeader(SipHeaders.MAXFORWARDS.value, '70')
    cseq = uaSession.getLastCSeq() + 1
    hdr_cseq = f'{cseq} BYE'
    bye_msg.addHeader(SipHeaders.CSEQ.value, hdr_cseq)
    uaSession.setCSeq(cseq)
    bye_msg.addHeader(SipHeaders.CONTENTLENGTH.value, 0)
    raw_msg = buildMessage(bye_msg, "")
    try:
        sock_obj = uaSession.getSigSocket()
        sock_obj.sendMessage(raw_msg)
    except socket.error as e:
        print("socket error in sending bye ", e)
    except IOError as e:
        if (e.errno == errno.EPIPE):
            print("IO error in bye sending ignoring :-", e)
            pass
    except:
        print("sending  bye failed")
        pass






