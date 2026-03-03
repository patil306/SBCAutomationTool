from sipmessage import SipMessage
from uasession import UASession
from util import getMyHostIP, createBranchID
from sipconstants import SipHeaders, SDPState, CRLF
from parserandbuilder import parseHeaders, parseContent
import authenticate
import copy

def sendUpdate(uaSession:UASession):
    update_msg = buildUpdate(uaSession)
    
    return update_msg

def buildUpdate(uaSession:UASession):    
    update_msg = SipMessage()
    remote_target = uaSession.getRemoteURL()
    update_msg.setRequestLine(f'UPDATE {remote_target} SIP/2.0')
    hdr_callid = uaSession.getCallID()
    update_msg.addHeader(SipHeaders.CALLID.value, hdr_callid)
    hdr_via = f'SIP/2.0/{uaSession.getTransport()} {getMyHostIP()};branch={createBranchID()}'
    update_msg.addHeader(SipHeaders.VIA.value, hdr_via)
    hdr_from = f'"{uaSession.getUserDisplayName()}"{uaSession.getFromHeader()}'
    update_msg.addHeader(SipHeaders.FROM.value, hdr_from)
    hdr_to = uaSession.getToHeader()
    update_msg.addHeader(SipHeaders.TO.value, hdr_to)
    cseq = uaSession.getLastCSeq() + 1
    hdr_cseq = f'{cseq} UPDATE'
    update_msg.addHeader(SipHeaders.CSEQ.value, hdr_cseq)
    port = 5060
    if uaSession.getUserType() in ["RW", "INT"]:
        port = uaSession.getSigSocket().getEphemeralPort()
    hdr_contact = f'"{uaSession.getUserDisplayName()}"<sip:{uaSession.getUserName()}@{getMyHostIP()}:{port}>'
    update_msg.addHeader(SipHeaders.CONTACT.value, hdr_contact)
    update_msg.addHeader(SipHeaders.MAXFORWARDS.value, 70)
    if uaSession.getProxyAuth():
        hdr_auth = authenticate.calcDigestResp(uaSession, uaSession.getUserName(), uaSession.getPassword(), 'UPDATE')
        update_msg.addHeader(SipHeaders.PROXYAUTHORIZATION.value,hdr_auth)
    content = uaSession.getCurSDP()
    content_len = content.getContentLength() if content else 0
    update_msg.replaceHeader(SipHeaders.CONTENTLENGTH.value, content_len)
   
    return update_msg

def sendUpdateWithAuth(uaSession:UASession):    
    update_msg = uaSession.getMsgObj('UPDATE')
    updateWithAuth = copy.deepcopy(update_msg)
    hdr_via = f'SIP/2.0/{uaSession.getTransport()} {getMyHostIP()};branch={createBranchID()}'
    updateWithAuth.replaceHeader(SipHeaders.VIA.value, hdr_via)
    hdr_auth = authenticate.calcDigestResp(uaSession, uaSession.getUserName(), uaSession.getPassword(), 'UPDATE')
    updateWithAuth.addHeader(SipHeaders.PROXYAUTHORIZATION.value,hdr_auth)

    return updateWithAuth


def recvUpdate(uaSession:UASession, raw_msg):
    raw_msg = raw_msg.split(CRLF+CRLF)
    sip_hdrs = raw_msg[0]
    sip_content = raw_msg[1] if len(raw_msg) > 1 else ""
    recv_update = parseHeaders(sip_hdrs)
    if sip_content:
        sdp_obj = parseContent(sip_content)
        uaSession.setRemoteSDP(sdp_obj)
        uaSession.setSDPstate(SDPState.SDP_RCVD.value)

    return recv_update

def send200Update(uaSession:UASession):
    update200_msg = build200Update(uaSession)

    return update200_msg

def build200Update(uaSession:UASession):
    last_msg = uaSession.getMsgObj('UPDATE') 
    update200_msg = copy.deepcopy(last_msg)
    resp_line = f'SIP/2.0 200 OK'
    update200_msg.setResponseLine(resp_line)
    # update200_msg.replaceHeader(SipHeaders.TO.value, uaSession.getFromHeader())
    port = 5060
    if uaSession.getUserType() in ["RW", "INT"]:
        port = uaSession.getSigSocket().getEphemeralPort()
    hdr_contact = f'"{uaSession.getUserDisplayName()}" <{uaSession.getScheme()}:{uaSession.getUserName()}@{getMyHostIP()}:{port}>'
    update200_msg.replaceHeader(SipHeaders.CONTACT.value, hdr_contact)
    content = uaSession.getCurSDP()
    content_len = content.getContentLength() if content else 0
    update200_msg.replaceHeader(SipHeaders.CONTENTLENGTH.value, content_len)
    if content_len > 0: update200_msg.replaceHeader(SipHeaders.CONTENTTYPE.value, 'application/sdp')

    return update200_msg
    
def recv200Update(uaSession:UASession, raw_msg):
    raw_msg = raw_msg.split(CRLF+CRLF)
    sip_hdrs = raw_msg[0]
    sip_content = raw_msg[1] if len(raw_msg) > 1 else ""
    recv_200Update = parseHeaders(sip_hdrs)
    if sip_content:
        sdp_obj = parseContent(sip_content)
        uaSession.setRemoteSDP(sdp_obj)
        uaSession.setSDPstate(SDPState.SDP_RCVD.value)

    return recv_200Update