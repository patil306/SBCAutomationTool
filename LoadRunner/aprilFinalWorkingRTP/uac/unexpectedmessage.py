from sipconstants import CRLF, SipHeaders
import transport
from parserandbuilder import buildMessage, parseHeaders
import util
import copy

def handleUnexpectedMessage(sock, message):
    message = message.split(CRLF+CRLF)
    sig_msg = message[0]
    content_msg = message[1] if len(message) > 1 else ""
    if sig_msg.startswith('SIP/2.0'):
        return
    else:        
        unexp_req = parseHeaders(sig_msg)
        unexpreq_200 = copy.deepcopy(unexp_req)
        respline = f'SIP/2.0 200 OK'
        unexpreq_200.setResponseLine(respline)
        my_ip = util.getMyHostIP()
        contact_hdr = f'sip:{my_ip}'
        unexpreq_200.replaceHeader(SipHeaders.CONTACT.value, contact_hdr)
        raw_msg = buildMessage(unexpreq_200, "")
        sock.sendMessage(raw_msg)
        
    
   