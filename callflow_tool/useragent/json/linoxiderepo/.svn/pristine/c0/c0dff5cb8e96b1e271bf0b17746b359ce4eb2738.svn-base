# from sipconstants import SipHeaders, CRLF
# from sipmessage import SipMessage, getHeaderName
# from util import buildMessage
# import json

# def parseMessage(raw_message):
#     rcvd_message = raw_message.decode('utf-8')
#     print(rcvd_message)
#     sip_msg = rcvd_message.split(CRLF+CRLF)
#     sig_msg = sip_msg[0]
#     sdp_msg = sip_msg[1]
    
#     sig_msg = sig_msg.split(CRLF)
#     sipMessage = SipMessage()
#     if sip_msg[0].startswith('SIP/2.0'):
#         sipMessage.setResponseLine(sig_msg[0])
#     else:
#         sipMessage.setRequestLine(sig_msg[0]) 
#     headers = sig_msg[1:]    
#     for hdrs in headers:             
#         hdr = hdrs.split(':',1)        
#         hdr_name = hdr[0]
#         hdr_value = hdr[1]
#         if hdr_name.startswith('Call-ID'):
#             hdr_name = SipHeaders.CALLID.value
#         elif hdr_name.startswith('From'):
#             hdr_name = SipHeaders.FROM.value
#         elif hdr_name.startswith('To'):
#             hdr_name = SipHeaders.TO.value
#         elif hdr_name.startswith('Via'):
#             hdr_name = SipHeaders.VIA.value
#         elif hdr_name.startswith('CSeq'):
#             hdr_name = SipHeaders.CSEQ.value
#         elif hdr_name.startswith('Max-Forwards'):
#             hdr_name = SipHeaders.MAXFORWARDS.value
#         elif hdr_name.startswith('Contact'):
#             hdr_name = SipHeaders.CONTACT.value
#         elif hdr_name.startswith('Content-Type'):
#             hdr_name = SipHeaders.CONTENTTYPE.value
#         elif hdr_name.startswith('Content-Length'):
#             hdr_name = SipHeaders.CONTENTLENGTH.value
#         elif hdr_name.startswith('Supported'):
#             hdr_name = SipHeaders.SUPPORTED.value
#         elif hdr_name.startswith('WWW-Authenticate'):
#             hdr_name = SipHeaders.WWWAUTHENTICATE.value
#         sipMessage.addHeader(hdr_name,hdr_value)
#     return sipMessage

# def parseJSONCallFlow():
#     data = None
#     with open('data.json') as file:
#         data = json.load(file)
#     return data

# def parseCallFlow(data):
#     key_len = len(data)
#     msg_len = key_len - 6
#     map = {}
#     for i in range(msg_len):
#             map[data.get(str(i)).get("message")] = data.get(str(i))            
#     return map

    