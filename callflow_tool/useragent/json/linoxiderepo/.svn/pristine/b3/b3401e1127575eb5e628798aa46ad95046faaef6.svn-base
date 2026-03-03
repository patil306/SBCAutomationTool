from uasession import UASession
from registration import UARegistration
from util import genCNonce
from parserandbuilder import parseHeaders
from sipconstants import SipHeaders, CRLF
from hashlib import md5

def recv407ProxyAuth(uaSession:UASession, raw_message):
    sip_msg = raw_message.split(CRLF+CRLF)
    sig_msg = sip_msg[0]
    msg_407 = parseHeaders(sig_msg)    
    authenticate = msg_407.getHeader(SipHeaders.PROXYAUTHENTICATE.value)
    list = authenticate[0].split(',')
    nonce = [idx for idx in list if idx.lower().startswith('nonce'.lower())][0].split("=")[1]
    nonce = nonce.strip('"')
    uaSession.setNonce(nonce)
    uaSession.setProxyAuth(True)
    return msg_407

def calcDigestResp(obj, usr_name, password, method:str):
    usr_name = str(usr_name)
    password = str(password)    
    obj.setCNonce(genCNonce())
    
    A1 = md5("{}:{}:{}".format(usr_name,obj.getRealm(),password).encode('utf-8')).hexdigest()
    A2 = md5("{}:{}".format(method,obj.getURI()).encode('utf-8')).hexdigest()
    
    A3 = md5("{}:{}:{}:{}:{}:{}".format(A1,obj.getNonce(),obj.getNCAuth(),obj.getCNonce(),obj.getQOP(),A2).encode('utf-8')).hexdigest()
    
    response = f'"{A3}"'

    hdr_proxy_authorization = f'Digest realm="{obj.getRealm()}",nonce={obj.getNonce()},uri="{obj.getURI()}",opaque="{obj.getOpaque()}"'
    hdr_proxy_authorization += f',qop={obj.getQOP()},response={response}'
    hdr_proxy_authorization += f',username="{obj.getUserName()}",cnonce="{obj.getCNonce()}",nc={obj.getNCAuth()}'

    obj.setUserName(usr_name)
    obj.setResponse(response)
    
    return hdr_proxy_authorization

def recv401Unauthorised(regSession:UARegistration, raw_message):
    sip_msg = raw_message.split(CRLF+CRLF)
    sig_msg = sip_msg[0]
    # sdp_msg = sip_msg[1]
    sipMessage = parseHeaders(sig_msg)
    authenticate = sipMessage.getHeader(SipHeaders.WWWAUTHENTICATE.value)
    list = authenticate[0].split(',')
    nonce = [idx for idx in list if idx.lower().startswith('nonce'.lower())][0].split("=")[1]
    nonce = nonce.strip('"')
    regSession.setNonce(nonce)
