from email.headerregistry import UniqueAddressHeader
from operator import inv
from uasession import UASession
from sipmessage import SipMessage
from util import createBranchID, createFromTag, createToTag, getMyHostIP, genCNonce, genRSeq, createCallID
from sipconstants import SipHeaders, CRLF, SipRespCodeMap, SDPState
from parserandbuilder import parseHeaders, parseContent, parseInputAndModifyMessage
import authenticate
import socket, copy
#from hashlib import md5
  
def sendInvite(uaSession:UASession):          
    invite_msg = buildOODINVITE(uaSession)    
    uaSession.setDialogOwner(True)    
    uaSession.setLocalTag(invite_msg.getFromTag())
    uaSession.setFromHeader(invite_msg.getHeader(SipHeaders.FROM.value))    
    #uaSession.setCallID(invite_msg.getCallID()) # commented as Trial code
    uaSession.setLocalContact(invite_msg.getHeader(SipHeaders.CONTACT.value))
    uaSession.setCurSipMessage(invite_msg)       
    return invite_msg
    

def buildOODINVITE(uaSession:UASession):
    oodInvite = SipMessage()       
    oodInvite.setRequestLine(f'INVITE sip:{uaSession.getTargetExtn()}@{uaSession.getDomain()} SIP/2.0')
    hdr_callid = uaSession.getCallID()
    oodInvite.addHeader(SipHeaders.CALLID.value,hdr_callid)
    f_tag = createFromTag()
    hdr_frm = f'"{uaSession.getUserDisplayName()}"<sip:{uaSession.getUserName()}@{uaSession.getDomain()}>;tag={f_tag}'
    oodInvite.addHeader(SipHeaders.FROM.value, hdr_frm)
    hdr_to = f'<sip:{uaSession.getTargetExtn()}@{uaSession.getDomain()}>'   
    oodInvite.addHeader(SipHeaders.TO.value, hdr_to) 
    host_ip = getMyHostIP()
    branch_id= createBranchID()
    hdr_via = f'SIP/2.0/{uaSession.getTransport()} {host_ip};branch={branch_id}'
    oodInvite.addHeader(SipHeaders.VIA.value, hdr_via)
    port = 5060
    if uaSession.getUserType() in ["RW", "INT"]:
        port = uaSession.getSigSocket().getEphemeralPort()
    hdr_contact = f'"{uaSession.getUserDisplayName()}"<sip:{uaSession.getUserName()}@{host_ip}:{port};transport={uaSession.getTransport()}>'
    oodInvite.addHeader(SipHeaders.CONTACT.value, hdr_contact)
    oodInvite.addHeader(SipHeaders.MAXFORWARDS.value, '70')
    oodInvite.addHeader(SipHeaders.CONTENTTYPE.value, 'application/sdp')
    cseq = uaSession.getLastCSeq() + 1
    hdr_cseq = f'{cseq} INVITE'
    oodInvite.addHeader(SipHeaders.CSEQ.value, hdr_cseq) 
    uaSession.setCSeq(cseq)
    content = uaSession.getCurSDP()
    content_len = content.getContentLength() if content else 0
    oodInvite.addHeader(SipHeaders.CONTENTLENGTH.value, content_len)
    featuretags = uaSession.getFeatureTags()    
    if uaSession.isReliable():
        if "100rel" not in featuretags:
            featuretags.append("100rel")           
    if featuretags:  
        supported_tags = ",".join(featuretags)              
        oodInvite.addHeader(SipHeaders.SUPPORTED.value, supported_tags)  
    allowedmethods = uaSession.getAllowedMethods()
    if allowedmethods:
        oodInvite.addHeader(SipHeaders.ALLOW.value, allowedmethods)        
    return oodInvite

def send407Ack(uaSession:UASession):
    inv_msg = uaSession.getMsgObj('INVITE')
    msg_407 = uaSession.getCurSipMessage()
    ack_407 = copy.deepcopy(inv_msg)
    to_tag = msg_407.getToTag()
    hdr_to = ack_407.getHeader(SipHeaders.TO.value)[0]
    hdr_to += f';tag={to_tag}'
    ack_407.replaceHeader(SipHeaders.TO.value, hdr_to)
    ack_407.replaceHeader(SipHeaders.CONTENTLENGTH.value, 0)
    routes = uaSession.getRouteSet()
    for route in routes:
        ack_407.addHeader(SipHeaders.ROUTE.value, route)
    cseq = uaSession.getLastCSeq()
    hdr_cseq = f'{cseq} ACK'
    ack_407.replaceHeader(SipHeaders.CSEQ.value, hdr_cseq)
    # hdr_via = f'SIP/2.0/{uaSession.getTransport()} {getMyHostIP()};branch={createBranchID()}'
    # ack_407.replaceHeader(SipHeaders.VIA.value, hdr_via)
    ack_407.setRequestLine((f'ACK sip:{uaSession.getTargetExtn()}@{uaSession.getDomain()} SIP/2.0'))
    return ack_407


def sendInvWithAuth(uaSession:UASession):
    invWithAuth = buildInvWithAuth(uaSession)
    uaSession.setProxyAuth(True)
    return invWithAuth

def buildInvWithAuth(uaSession:UASession):
    inv_msg = uaSession.getMsgObj('INVITE')
    invWithAuth = copy.deepcopy(inv_msg)
    hdr_via = f'SIP/2.0/{uaSession.getTransport()} {getMyHostIP()};branch={createBranchID()}'
    invWithAuth.replaceHeader(SipHeaders.VIA.value, hdr_via)
    cseq = uaSession.getLastCSeq() + 1
    uaSession.setCSeq(cseq)
    hdr_cseq = f'{cseq} INVITE'
    invWithAuth.replaceHeader(SipHeaders.CSEQ.value, hdr_cseq)
    hdr_auth = authenticate.calcDigestResp(uaSession, uaSession.getUserName(), uaSession.getPassword(), 'INVITE')    
    invWithAuth.addHeader(SipHeaders.PROXYAUTHORIZATION.value,hdr_auth)
    return invWithAuth


def recvInvite(uaSession:UASession, raw_message):        
    sip_msg = raw_message.split(CRLF+CRLF)
    sig_msg = sip_msg[0]
    sdp_msg = sip_msg[1] if len(sip_msg) > 1 else ""
    rcvdInvite = parseHeaders(sig_msg)        
    uaSession.setCallID(rcvdInvite.getCallID())
    uaSession.setToHeader(rcvdInvite.getHeader(SipHeaders.FROM.value))
    uaSession.setFromHeader(rcvdInvite.getHeader(SipHeaders.TO.value))
    uaSession.setRemoteTarget(rcvdInvite.getHeader(SipHeaders.CONTACT.value))
    uaSession.setRemoteTag(rcvdInvite.getFromTag())
    uaSession.setDialogOwner(False)    
    uaSession.setRouteSet(rcvdInvite.getRecordRoutes(False))
    if sdp_msg:
        sdp = parseContent(sdp_msg)
        uaSession.setRemoteSDP(sdp)
        uaSession.setSDPstate(SDPState.SDP_RCVD.value)
    return rcvdInvite  


def send100Trying(uaSession):
    trying_msg = build100Trying(uaSession)
    return trying_msg

def build100Trying(uaSession:UASession):
    inv_msg = uaSession.getMsgObj("INVITE")
    trying_msg = copy.deepcopy(inv_msg)
    hdr_list = [SipHeaders.VIA.value, SipHeaders.TO.value, SipHeaders.FROM.value, SipHeaders.CALLID.value, SipHeaders.CSEQ.value]
    trying_msg.removeAllHeadersExcept(hdr_list)
    trying_msg.setResponseLine(f'SIP/2.0 100 Trying')
    trying_msg.addHeader(SipHeaders.CONTENTLENGTH.value, 0)
    return trying_msg


def sendProvResponse(uaSession:UASession, respcode):
    # sipMessage = uaSession.getCurSipMessage()
    provResp = buildProvResponse(uaSession, respcode)    
    uaSession.setLocalTag(provResp.getToTag())
    uaSession.setLocalContact(provResp.getHeader(SipHeaders.CONTACT.value)) 
    uaSession.setFromHeader(provResp.getHeader(SipHeaders.TO.value))     
    return provResp    

def buildProvResponse(uaSession:UASession, respcode):
    lastMsg = uaSession.getMsgObj("INVITE")
    provResp = copy.deepcopy(lastMsg)
    respText = SipRespCodeMap.get(respcode)
    provResp.setResponseLine(f'SIP/2.0 {respcode} {respText}')    
    to_tag = createToTag()
    hdr_to = uaSession.getFromHeader() + f';tag={to_tag}'
    provResp.replaceHeader(SipHeaders.TO.value, hdr_to)
    my_ext = uaSession.getUserName()
    my_IP = getMyHostIP()
    scheme = uaSession.getScheme()
    port = 5060
    if uaSession.getUserType() in ["RW", "INT"]:
        port = uaSession.getSigSocket().getEphemeralPort()
    hdr_contact = f'"{uaSession.getUserDisplayName()}" <{scheme}:{my_ext}@{my_IP}:{port};transport={uaSession.getTransport()}>'
    provResp.replaceHeader(SipHeaders.CONTACT.value, hdr_contact)   
    featuretags = uaSession.getFeatureTags()    
    if uaSession.isReliable():
        if '100rel' not in featuretags:
            featuretags.append('100rel')
        hdr_require = f'100rel'
        provResp.addHeader(SipHeaders.REQUIRE.value, hdr_require)
        rseq =  uaSession.getRSeq() if uaSession.getRSeq() else genRSeq()
        uaSession.setRSeq(rseq)
        provResp.addHeader(SipHeaders.RSEQ.value, rseq)   
    if featuretags:
        supported_tags = ",".join(featuretags)
        provResp.replaceHeader(SipHeaders.SUPPORTED.value, supported_tags)        
    allowed_methods = uaSession.getAllowedMethods()
    if allowed_methods:
        provResp.replaceHeader(SipHeaders.ALLOW.value, allowed_methods)
    content = uaSession.getCurSDP()
    content_len = content.getContentLength() if content else 0
    provResp.replaceHeader(SipHeaders.CONTENTLENGTH.value, content_len)
    if content_len > 0 : provResp.replaceHeader(SipHeaders.CONTENTTYPE.value, 'application/sdp')
    return provResp

def recvProvResponse(uaSession:UASession, raw_msg):
    raw_msg = raw_msg.split(CRLF+CRLF)
    sip_hdrs = raw_msg[0]
    sip_content = raw_msg[1] if len(raw_msg) > 1 else ""
    recv_provResp = parseHeaders(sip_hdrs)    
    uaSession.setRemoteTarget(recv_provResp.getHeader(SipHeaders.CONTACT.value))
    uaSession.setRemoteTag(recv_provResp.getToTag())
    uaSession.setRouteSet(recv_provResp.getRecordRoutes(True))
    uaSession.setToHeader(recv_provResp.getHeader(SipHeaders.TO.value))
    uaSession.setRSeq(recv_provResp.getRSeq())
    if sip_content:
        sdp_obj = parseContent(sip_content)
        uaSession.setRemoteSDP(sdp_obj)
        uaSession.setSDPstate(SDPState.SDP_RCVD.value)
    return recv_provResp

def send200InvResp(uaSession:UASession):
    resp200Inv = build200InvResp(uaSession)
    
    uaSession.setFromHeader(resp200Inv.getHeader(SipHeaders.TO.value))
    
    return resp200Inv

def build200InvResp(uaSession:UASession):
    lastInv_msg = uaSession.getMsgObj('INVITE') 
    inv200_msg = copy.deepcopy(lastInv_msg)
    inv200_msg.setResponseLine(f'SIP/2.0 200 OK')
    my_ext = uaSession.getUserName()
    my_IP = getMyHostIP()
    scheme = uaSession.getScheme()
    inv200_msg.replaceHeader(SipHeaders.TO.value, uaSession.getFromHeader())
    port = 5060
    if uaSession.getUserType() in ["RW", "INT"]:
        port = uaSession.getSigSocket().getEphemeralPort()
    hdr_contact = f'"{uaSession.getUserDisplayName()}"<{scheme}:{my_ext}@{my_IP}:{port};transport={uaSession.getTransport()}>'
    inv200_msg.replaceHeader(SipHeaders.CONTACT.value, hdr_contact)
    hdr_to = uaSession.getFromHeader()
    inv200_msg.replaceHeader(SipHeaders.TO.value, hdr_to)
    content = uaSession.getCurSDP()
    content_len = content.getContentLength() if content else 0
    inv200_msg.replaceHeader(SipHeaders.CONTENTLENGTH.value, content_len)
    if content_len > 0: inv200_msg.replaceHeader(SipHeaders.CONTENTTYPE.value, 'application/sdp')
    return inv200_msg

def recv200Invite(uaSession:UASession, raw_msg):
    raw_msg = raw_msg.split(CRLF+CRLF)
    sip_hdrs = raw_msg[0]
    sip_content = raw_msg[1] if len(raw_msg) > 1 else ""
    recv_200Inv = parseHeaders(sip_hdrs)    
    uaSession.setRemoteTarget(recv_200Inv.getHeader(SipHeaders.CONTACT.value))
    uaSession.setRemoteTag(recv_200Inv.getToTag())
    uaSession.setRouteSet(recv_200Inv.getRecordRoutes(True))    
    if sip_content:
        sdp_obj = parseContent(sip_content)
        uaSession.setRemoteSDP(sdp_obj)
        if uaSession.getSDPState() == SDPState.COMPLETE.value:
            pass
        else:
            uaSession.setSDPstate(SDPState.SDP_RCVD.value)
    return recv_200Inv

def sendInvAck(uaSession:UASession):
    invAck_msg = buildInvAck(uaSession)
    return invAck_msg

def buildInvAck(uaSession:UASession):
    invMsg = uaSession.getMsgObj("INVITE")
    ack = copy.deepcopy(invMsg)
    cur_msg = uaSession.getCurSipMessage() 
    to_tag = cur_msg.getToTag()
    hdr_to = ack.getHeader(SipHeaders.TO.value)[0]
    hdr_to += f';tag={to_tag}'
    ack.replaceHeader(SipHeaders.TO.value,hdr_to)   
    contact_uri = uaSession.getRemoteURL()
    ack.setRequestLine(f'ACK {contact_uri} SIP/2.0')
    branch_id= createBranchID()
    transport = uaSession.getTransport()
    my_ip = getMyHostIP()
    hdr_via = f'SIP/2.0/{transport} {my_ip};branch={branch_id}'
    ack.replaceHeader(SipHeaders.VIA.value, hdr_via)
    if uaSession.getProxyAuth():
        hdr_auth = authenticate.calcDigestResp(uaSession, uaSession.getUserName(), uaSession.getPassword(), 'ACK')
        ack.replaceHeader(SipHeaders.PROXYAUTHORIZATION.value, hdr_auth)
    cseq = int(invMsg.getCSeq())
    hdr_cseq = f'{cseq} ACK'
    ack.replaceHeader(SipHeaders.CSEQ.value, hdr_cseq)
    content_length = uaSession.getCurSDP().getContentLength() if uaSession.getCurSDP() else 0
    ack.replaceHeader(SipHeaders.CONTENTLENGTH.value, content_length)
    ack.removeHeader(SipHeaders.ROUTE.value)
    route_set = uaSession.getRouteSet()      
    for route in route_set:
        ack.addHeader(SipHeaders.ROUTE.value, route)
    return ack    

def sendAckForErrorResponse(uaSession):
    msg_inv = uaSession.getMsgObj("INVITE")
    cseq = msg_inv.getCSeq()
    msg_ack = copy.deepcopy(msg_inv)
    msg_ack.replaceHeader(SipHeaders.CSEQ.value, f'{cseq} ACK')
    to_hdr = uaSession.getToHeader()
    msg_ack.replaceHeader(SipHeaders.TO.value, to_hdr)
    return msg_ack

def recvInvACK(uaSession:UASession, raw_msg):
    raw_msg = raw_msg.split(CRLF+CRLF)
    ack_msg = parseHeaders(raw_msg[0])
    sip_content = raw_msg[1] if len(raw_msg) > 1 else ""
    if sip_content:
        ack_sdp = parseContent(raw_msg[1])
        uaSession.setRemoteSDP(ack_sdp)
        uaSession.setSDPstate(SDPState.SDP_RCVD.value)
    return ack_msg

def sendReInvite(uaSession:UASession):
    reInv_msg = buildReInvite(uaSession)
    return reInv_msg

def buildReInvite(uaSession:UASession):
    reInv_msg = SipMessage()       
    reInv_msg.setRequestLine(f'INVITE {uaSession.getRemoteURL()} SIP/2.0')
    reInv_msg.addHeader(SipHeaders.CALLID.value,uaSession.getCallID())
    reInv_msg.addHeader(SipHeaders.FROM.value, uaSession.getFromHeader())
    reInv_msg.addHeader(SipHeaders.TO.value, uaSession.getToHeader()) 
    hdr_via = f'SIP/2.0/{uaSession.getTransport()} {getMyHostIP()};branch={createBranchID()}'
    reInv_msg.addHeader(SipHeaders.VIA.value, hdr_via)
    port = 5060
    if uaSession.getUserType() in ["RW", "INT"]:
        port = uaSession.getSigSocket().getEphemeralPort()
    hdr_contact = f'"{uaSession.getUserDisplayName()}"<sip:{uaSession.getUserName()}@{getMyHostIP()}:{port};transport={uaSession.getTransport()}>'
    reInv_msg.addHeader(SipHeaders.CONTACT.value, hdr_contact)
    reInv_msg.addHeader(SipHeaders.MAXFORWARDS.value, '70')
    reInv_msg.addHeader(SipHeaders.CONTENTTYPE.value, 'application/sdp')
    cseq = uaSession.getLastCSeq() + 1
    hdr_cseq = f'{cseq} INVITE'
    reInv_msg.addHeader(SipHeaders.CSEQ.value, hdr_cseq) 
    uaSession.setCSeq(cseq)
    reInv_msg.removeHeader(SipHeaders.ROUTE.value)
    route_set = uaSession.getRouteSet()
    for route in route_set:
        reInv_msg.addHeader(SipHeaders.ROUTE.value, route)
    if uaSession.getProxyAuth():
        hdr_auth = authenticate.calcDigestResp(uaSession, uaSession.getUserName(), uaSession.getPassword(), 'INVITE')
        reInv_msg.addHeader(SipHeaders.PROXYAUTHORIZATION.value,hdr_auth)
    featuretags = uaSession.getFeatureTags()       
    if featuretags:  
        supported_tags = ",".join(featuretags)              
        reInv_msg.addHeader(SipHeaders.SUPPORTED.value, supported_tags)  
    allowedmethods = uaSession.getAllowedMethods()
    if allowedmethods:
        reInv_msg.addHeader(SipHeaders.ALLOW.value, allowedmethods)    
    content = uaSession.getCurSDP()
    content_len = content.getContentLength() if content else 0
    reInv_msg.addHeader(SipHeaders.CONTENTLENGTH.value, content_len)

    return reInv_msg


def recvReInvite(uaSession:UASession, raw_message):
    sip_msg = raw_message.split(CRLF+CRLF)
    sig_msg = sip_msg[0]
    sdp_msg = sip_msg[1] if len(sip_msg) > 1 else ""
    rcvdReInv = parseHeaders(sig_msg)        
    if sdp_msg:
        sdp = parseContent(sdp_msg)
        uaSession.setRemoteSDP(sdp)  
    return rcvdReInv


def sendInvWithReplaces(uaSession:UASession, prev_session):
    invWithReplaces = buildInvWithReplaces(uaSession, prev_session)
    return invWithReplaces

def buildInvWithReplaces(uaSession:UASession, prev_session:UASession):
    invWithReplaces = SipMessage()       
    invWithReplaces.setRequestLine(f'INVITE {prev_session.getReferTo()} SIP/2.0')
    hdr_callid = uaSession.getCallID()
    invWithReplaces.addHeader(SipHeaders.CALLID.value,hdr_callid)
    f_tag = createFromTag()
    hdr_frm = f'"{uaSession.getUserDisplayName()}"<sip:{uaSession.getUserName()}@{uaSession.getDomain()}>;tag={f_tag}'
    invWithReplaces.addHeader(SipHeaders.FROM.value, hdr_frm)
    hdr_to = f'<sip:{uaSession.getTargetExtn()}@{uaSession.getDomain()}>'   
    invWithReplaces.addHeader(SipHeaders.TO.value, hdr_to) 
    host_ip = getMyHostIP()
    branch_id= createBranchID()
    hdr_via = f'SIP/2.0/{uaSession.getTransport()} {host_ip};branch={branch_id}'
    invWithReplaces.addHeader(SipHeaders.VIA.value, hdr_via)
    port = 5060
    if uaSession.getUserType() in ["RW", "INT"]:
        port = uaSession.getSigSocket().getEphemeralPort()
    hdr_contact = f'"{uaSession.getUserDisplayName()}"<sip:{uaSession.getUserName()}@{host_ip}:{port};transport={uaSession.getTransport()}>'
    invWithReplaces.addHeader(SipHeaders.CONTACT.value, hdr_contact)
    hdr_replaces = prev_session.getReplaces()
    invWithReplaces.addHeader(SipHeaders.REPLACES.value, hdr_replaces)
    hdr_refrd_by = prev_session.getReferredBy()
    invWithReplaces.addHeader(SipHeaders.REFERREDBY.value, hdr_refrd_by)
    invWithReplaces.addHeader(SipHeaders.MAXFORWARDS.value, '70')
    invWithReplaces.addHeader(SipHeaders.CONTENTTYPE.value, 'application/sdp')
    cseq = uaSession.getLastCSeq() + 1
    hdr_cseq = f'{cseq} INVITE'
    invWithReplaces.addHeader(SipHeaders.CSEQ.value, hdr_cseq) 
    uaSession.setCSeq(cseq)
    content = uaSession.getCurSDP()
    content_len = content.getContentLength() if content else 0
    invWithReplaces.addHeader(SipHeaders.CONTENTLENGTH.value, content_len)
    featuretags = uaSession.getFeatureTags()    
    if uaSession.isReliable():
        if "100rel" not in featuretags:
            featuretags.append("100rel")           
    if featuretags:  
        supported_tags = ",".join(featuretags)              
        invWithReplaces.addHeader(SipHeaders.SUPPORTED.value, supported_tags)  
    allowedmethods = uaSession.getAllowedMethods()
    if allowedmethods:
        invWithReplaces.addHeader(SipHeaders.ALLOW.value, allowedmethods)        
    return invWithReplaces



# def sendCancel(uaSession:UASession):
#     cancel_msg = buildCancel(UASession)
#     return cancel_msg

# def buildCancel(uaSession:UASession):
#     inv_msg = uaSession.getMsgObj("INVITE")
#     cancel_msg = copy.deepcopy(inv_msg)
#     cancel_msg.setRequestLine(f'CANCEL {SipMessage.getRequestURL()}')
#     return cancel_msg