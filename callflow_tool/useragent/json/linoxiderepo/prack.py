from parserandbuilder import parseHeaders, parseContent
from uasession import UASession
from sipconstants import SipHeaders, SDPState, CRLF
from util import createBranchID, getMyHostIP
import copy
import authenticate

def sendPrack(uaSession:UASession):
    prack = buildPrack(uaSession)
    return prack
    
def buildPrack(uaSession:UASession ):
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
    route_set = uaSession.getRouteSet()
    prack.removeHeader(SipHeaders.ROUTE.value)
    for route in route_set:
        prack.addHeader(SipHeaders.ROUTE.value, route)
    if uaSession.isReliable():
        cseq = invMsg.getCSeq()
        rseq = uaSession.getRSeq()        
        hdr_rack = f'{rseq} {cseq} INVITE'
        prack.addHeader(SipHeaders.RACK.value, hdr_rack) 
    if uaSession.getProxyAuth():
        hdr_auth = authenticate.calcDigestResp(uaSession, uaSession.getUserName(), uaSession.getPassword(), 'PRACK')
        prack.replaceHeader(SipHeaders.PROXYAUTHORIZATION.value,hdr_auth)    
    cur_sdp = uaSession.getCurSDP()
    cont_len = cur_sdp.getContentLength() if cur_sdp else 0
    prack.replaceHeader(SipHeaders.CONTENTLENGTH.value, cont_len)
    
    return prack

def recvPrack(uaSession:UASession, raw_msg:str):
    raw_msg = raw_msg.split(CRLF+CRLF)
    prack_msg = parseHeaders(raw_msg[0])       
    if len(raw_msg)> 1:
        prack_sdp = parseContent(raw_msg[1])
        uaSession.setRemoteSDP(prack_sdp)
        uaSession.setSDPstate(SDPState.SDP_RCVD.value)
    return prack_msg    

def send200Prack(uaSession:UASession):
    prack200_msg = build200Prack(uaSession)
    return prack200_msg

def build200Prack(uaSession:UASession):
    lastPrack_msg = uaSession.getMsgObj('PRACK') 
    prack200_msg = copy.deepcopy(lastPrack_msg)
    resp_line = f'SIP/2.0 200 OK'
    prack200_msg.setResponseLine(resp_line)
    my_ext = uaSession.getUserName()
    my_IP = getMyHostIP()
    scheme = uaSession.getScheme()
    port = 5060
    if uaSession.getUserType() in ["RW", "INT"]:
        port = uaSession.getSigSocket().getEphemeralPort()
    hdr_contact = f'"{uaSession.getUserDisplayName()}" <{scheme}:{my_ext}@{my_IP}:{port};transport={uaSession.getTransport()}>'
    prack200_msg.replaceHeader(SipHeaders.CONTACT.value, hdr_contact)
    prack200_msg.removeHeader(SipHeaders.RACK.value)
    content = uaSession.getCurSDP()
    content_len = content.getContentLength() if content else 0
    prack200_msg.replaceHeader(SipHeaders.CONTENTLENGTH.value, content_len)
    if content_len > 0: prack200_msg.replaceHeader(SipHeaders.CONTENTTYPE.value, 'application/sdp')
    return prack200_msg

def recv200Prack(uaSession:UASession, raw_msg):
    raw_msg = raw_msg.split(CRLF+CRLF)
    sip_hdrs = raw_msg[0]
    sip_content = raw_msg[1]
    recv_200Prack = parseHeaders(sip_hdrs)    
    uaSession.setRemoteTarget(recv_200Prack.getHeader(SipHeaders.CONTACT.value))
    uaSession.setRemoteTag(recv_200Prack.getToTag())
    if sip_content:
        sdp_obj = parseContent(sip_content)
        uaSession.setRemoteSDP(sdp_obj)
        uaSession.setSDPstate(SDPState.SDP_RCVD.value)
    return recv_200Prack