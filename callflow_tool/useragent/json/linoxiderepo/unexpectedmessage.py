from sipconstants import CRLF, SipHeaders
from sipmessage import SipMessage
import transport
from parserandbuilder import buildMessage, parseHeaders
import util
import copy
from uasession import UASession

def handleUnexpectedIndialogRequest(uaSession, message):
    message = message.split(CRLF+CRLF)
    sig_msg = message[0]
    content_msg = message[1] if len(message) > 1 else ""        
    unexp_req = parseHeaders(sig_msg)
    unexpreq_200 = copy.deepcopy(unexp_req)
    respline = f'SIP/2.0 200 OK'
    unexpreq_200.setResponseLine(respline)
    my_ip = util.getMyHostIP()
    user_name = uaSession.getUserName()
    contact_hdr = f'<sip:{user_name}@{my_ip}>'
    unexpreq_200.replaceHeader(SipHeaders.CONTACT.value, contact_hdr)
    unexpreq_200.replaceHeader(SipHeaders.CONTENTLENGTH.value, 0)
    raw_msg = buildMessage(unexpreq_200, "")
    sock_obj = uaSession.getSigSocket()
    sock_obj.sendMessage(raw_msg)
        
def handleUnexpectedOODmessage(message:SipMessage):
    resp_err = copy.deepcopy(message)
    resp_err.setResponseLine(f'SIP/2.0 403 Forbidden')
    resp_err.replaceHeader(SipHeaders.CONTENTLENGTH.value, 0)
    resp_err.removeHeader(SipHeaders.CONTACT.value)
    
    return resp_err

def handleOption(message:SipMessage):
    resp_200 = copy.deepcopy(message)
    resp_200.setResponseLine(f'SIP/2.0 200 OK')
    resp_200.replaceHeader(SipHeaders.CONTENTLENGTH.value,0)
    resp_200.removeHeader(SipHeaders.CONTACT.value)
    to_hdr = message.getHeader(SipHeaders.TO.value)[0]
    to_hdr = f'{to_hdr};tag=T_123'
    resp_200.replaceHeader(SipHeaders.TO.value, to_hdr)
        
    return resp_200
        
def handleUnexpectedIndialogResponse(uaSession:UASession, message):
    message = message.split(CRLF + CRLF)
    sig_msg = message[0]
    content_msg = message[1] if len(message) > 1 else ""
    unexp_resp = parseHeaders(sig_msg)
    method = unexp_resp.getMethod()
    resp_code = unexp_resp.getResponseCode()
    if method == "INVITE" and util.isInErrorResponseCode(resp_code):
        sendAck(uaSession, unexp_resp)
    else:
        return


def sendAck(uaSession, err_msg:SipMessage):
    msg_inv = uaSession.getMsgObj("INVITE")
    cseq = err_msg.getCSeq()
    msg_ack = copy.deepcopy(msg_inv)
    msg_ack.replaceHeader(SipHeaders.CSEQ.value, f'{cseq} ACK')
    to_hdr = err_msg.getHeader(SipHeaders.TO.value)[0]
    msg_ack.replaceHeader(SipHeaders.TO.value, to_hdr)
    raw_msg = buildMessage(msg_ack,"")
    sock_obj = uaSession.getSigSocket()
    sock_obj.sendMessage(raw_msg)



   