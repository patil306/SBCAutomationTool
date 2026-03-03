from uasession import UASession
from sipmessage import SipMessage, getHeaderName
from sipconstants import SipHeaders, CRLF
from util import createBranchID, getMyHostIP
from parserandbuilder import parseHeaders, parseContent
import authenticate
import re
import copy

def sendRefer(uaSession:UASession, transfer_target, other_uaSession:UASession):
    msg_refer = buildRefer(uaSession, transfer_target, other_uaSession)
    return msg_refer


def buildRefer(uaSession:UASession, transfer_target, prev_uaSession:UASession):
    refer_msg = SipMessage()
    refer_msg.setRequestLine(f'REFER {uaSession.getRemoteURL()} SIP/2.0')
    hdr_callid = uaSession.getCallID()
    refer_msg.addHeader(SipHeaders.CALLID.value,hdr_callid)
    hdr_frm = uaSession.getFromHeader()
    refer_msg.addHeader(SipHeaders.FROM.value, hdr_frm)
    hdr_to = uaSession.getToHeader() 
    refer_msg.addHeader(SipHeaders.TO.value, hdr_to) 
    branch_id= createBranchID()
    hdr_via = f'SIP/2.0/{uaSession.getTransport()} {getMyHostIP()};branch={branch_id}'
    refer_msg.addHeader(SipHeaders.VIA.value, hdr_via)
    port = 5060
    if uaSession.getUserType() in ["RW", "INT"]:
        port = uaSession.getSigSocket().getEphemeralPort()
    hdr_contact = f'<sip:{uaSession.getUserName()}@{getMyHostIP()}:{port};transport={uaSession.getTransport()}>'
    refer_msg.addHeader(SipHeaders.CONTACT.value, hdr_contact)
    hdr_refer_to = ''
    if prev_uaSession:   # AttendedTransfer
        hdr_refer_to = f'<{prev_uaSession.getRemoteURL()}?Replaces={prev_uaSession.getCallID()}%3B'
        hdr_refer_to += f'to-tag%3D{prev_uaSession.getRemoteTag()}%3Bfrom-tag%3D{prev_uaSession.getLocalTag()}>'  
    else:                   # BlindTransfer
        hdr_refer_to = f'<sip:{transfer_target}@{uaSession.getDomain()}>'
    refer_msg.addHeader(SipHeaders.REFERTO.value, hdr_refer_to)
    hdr_refBy = f'<{uaSession.getScheme()}:{uaSession.getUserName()}@{uaSession.getDomain()}>'
    refer_msg.addHeader(SipHeaders.REFERREDBY.value, hdr_refBy)
    if uaSession.getProxyAuth():
        hdr_auth = authenticate.calcDigestResp(uaSession, uaSession.getUserName(), uaSession.getPassword(), 'REFER')
        refer_msg.addHeader(SipHeaders.PROXYAUTHORIZATION.value,hdr_auth)
    refer_msg.addHeader(SipHeaders.MAXFORWARDS.value, '70')
    cseq = uaSession.getLastCSeq() + 1
    hdr_cseq = f'{cseq} REFER'
    refer_msg.addHeader(SipHeaders.CSEQ.value, hdr_cseq)
    uaSession.setCSeq(cseq)
    refer_msg.addHeader(SipHeaders.CONTENTLENGTH.value, 0) 
    return refer_msg

def recvRefer(uaSession:UASession, raw_msg):
    raw_msg = raw_msg.split(CRLF + CRLF)
    refer_msg = parseHeaders(raw_msg[0])
    hdr_refer_to = refer_msg.getHeader(SipHeaders.REFERTO.value)[0]
    refer_replaces = (re.search('Replaces=(.*)>',hdr_refer_to).group(1)).split('&')[0] if re.search('Replaces=(.*)',hdr_refer_to) else ""
    refer_replaces = refer_replaces.replace('%3D', '=').replace('%3B', ';').replace('%40', '@')
    refer_to = hdr_refer_to.split('?')[0].strip('<')
    refrd_by = refer_msg.getHeader(SipHeaders.REFERREDBY.value)[0]

    uaSession.setReplaces(refer_replaces)
    uaSession.setReferTo(refer_to)
    uaSession.setReferredBy(refrd_by)
    return refer_msg

def recv202Accepted(uaSession:UASession, raw_msg):
    raw_msg = raw_msg.split(CRLF+CRLF)
    sip_hdrs = raw_msg[0]
    recv_202Refer = parseHeaders(sip_hdrs)
    
    return recv_202Refer


def recvNotify(uaSession:UASession, raw_msg):
    raw_msg = raw_msg.split(CRLF+CRLF)
    sip_hdrs = raw_msg[0]
    recv_notify = parseHeaders(sip_hdrs)    
    
    return recv_notify

def send200Notify(uaSession:UASession):
    notify_msg = uaSession.getMsgObj('NOTIFY')
    notify200 = copy.deepcopy(notify_msg)
    notify200.setResponseLine(f'SIP/2.0 200 OK')
    hdr_contact = f'<{uaSession.getScheme()}:{uaSession.getUserName()}@{getMyHostIP()};transport={uaSession.getTransport()}>'   
    notify200.replaceHeader(SipHeaders.CONTACT.value, hdr_contact)
    notify200.replaceHeader(SipHeaders.CONTENTLENGTH.value, 0)
    
    return notify200