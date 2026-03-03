from enum import Enum, auto
CR = '\r'
LF = '\n'
CRLF = '\r\n'
# Add any respcode and text at the end of the list only.
SipRespCode = ['100','180','181','182','183','200','202','301','302','380','400','401','402','403','404','405','406','407','408','410','413','414','415','416',
'420','421','423','480','481','482','483','484','485','486','487','488','491','500','501','502','503','504']

SipRespText = ['Trying','Ringing','Call Is Being Forwarded','Queued','Session Progress','OK','Accepted','Moved Permanently','Moved Temporarily',
'Alternative Service','Bad Request','Unauthorised','Payment Required','Forbidden','Not Found','Method Not Allowed','Not Acceptable',
'Proxy Authentication Required','Request Timeout','Gone','Request Entity Too Large','Request-URI Too Large','Unsupported Media Type',
'Unsupported URI Scheme','Bad Extension','Extension Required','Interval Too Brief','Temporary Not Avaialable','Call Leg Does Not Exist',
'Loop Detected','Too Many Hops','Address Incomplete','Ambiguous','Busy Here','Request Terminated','Not Acceptable Here','Request Pending',
'Internal Server Error','Not Implemented','Bad Gateway','Service Unavailable','Server Timeout']

SipRespCodeMap = {SipRespCode[i]:SipRespText[i] for i in range (len(SipRespCode))}

class SipRequest(Enum):  
    NONE = 0  
    REGISTER = 'REGISTER'
    INVITE = 'INVITE'        
    CANCEL = 'CANCEL'
    PRACK = 'PRACK'    
    ACK = 'ACK'
    BYE = 'BYE'        
    REFER = 'REFER'    
    NOTIFY = 'NOTIFY'
    SUBSCRIBE = 'SUBSCRIBE'
    UPDATE = 'UPDATE'


class SipHeaders(Enum):
    CALLID = 'Call-ID'
    FROM = 'From'
    TO = 'To'
    CSEQ = 'CSeq'
    VIA = 'Via'
    RECORDROUTE = 'Record-Route'
    ROUTE = 'Route'
    CONTACT = 'Contact'
    MAXFORWARDS = 'Max-Forwards'
    CONTENTTYPE = 'Content-Type'
    CONTENTLENGTH = 'Content-Length'
    SUPPORTED = 'Supported'
    WWWAUTHENTICATE = 'WWW-Authenticate'
    AUTHORIZATION = 'Authorization'
    PROXYAUTHENTICATE = 'Proxy-Authenticate'
    PROXYAUTHORIZATION = 'Proxy-Authorization'
    REFERTO = 'Refer-To'
    REFERREDBY = 'Referred-By'
    EXPIRES = 'Expires'
    REQUIRE = 'Require'
    RSEQ = 'RSeq'
    RACK = 'RAck'
    ALLOW = 'Allow'
    EVENT = 'Event'
    SUBSCRIPTIONSTATE = 'Subscription-State'

class SipCallState(Enum):
    IDLE = 'IDLE'
    INVTIE_SENT = 'INVITE_SENT'
    INVITE_RCVD = 'INVTIE_RCVD'
    PROVRESP_SENT = 'PROVRESP_SENT'
    PROVRESP_RCVD = 'PROVRESP_RCVD'
    PRACK_SENT = 'PRACK_SENT'
    PRACK_RCVD = 'PRACK_RCVD'
    OK200_SENT = 'OK200_SENT'
    OK200_RCVD = 'OK200_RCVD'
    ACK_SENT= 'ACK_SENT'
    ACK_RCVD = 'ACK_RCVD'
    BYE_SENT = 'BYE_SENT'
    BYE_RCVD = 'BYE_RCVD'
    COMPLETE = 'COMPLETE'


class SDPState(Enum):
    IDLE = 0
    SDP_SENT = 'SDP_SENT'
    SDP_RCVD = 'SDP_RCVD'
    COMPLETE = 'COMPLETE'
    SDP_ERROR = 'SDP_ERROR'
    
class Transport(Enum):
    TCP = 'tcp'
    UDP = 'udp'

class Direction(Enum):
    SEND = 'send'
    RECV = 'recv'
    

    