from sipconstants import SipHeaders, CRLF
from sipmessage import SipMessage, getHeaderName
from uasession import UASession
from util import getMyHostIP
from sdp import SDP, SDPMLine
import json
import glob

def parseHeaders(sig_msg):        
    sig_msg = sig_msg.split(CRLF)
    sipMessage = SipMessage()
    if sig_msg[0].startswith('SIP/2.0'):
        sipMessage.setResponseLine(sig_msg[0])
    else:
        sipMessage.setRequestLine(sig_msg[0])         
    headers = sig_msg[1:]    
    for hdrs in headers:                     
        hdr = hdrs.split(':',1)        
        hdr_name = hdr[0]
        hdr_name = getHeaderName(hdr_name)
        hdr_value = hdr[1]      
        sipMessage.addHeader(hdr_name,hdr_value)
    return sipMessage

def parseContent(content):
    clen = len(content)
    content = content.split(CRLF)
    sdp = SDP()
    sdp.setContentLength(clen)
    hasMlineParsed = False       
    for hdr in content:
        if hdr.startswith('v='):
            sdp.setVline(hdr)
        elif hdr.startswith('o='):
            sdp.setOline(hdr)
        elif hdr.startswith('s='):
            sdp.setSline(hdr)
        elif hdr.startswith('t='):
            sdp.setTline(hdr)
        elif hdr.startswith('c='):
            if hasMlineParsed:
                mline = sdp.getLastMline()
                mline.setCline(hdr)
            else:
                sdp.setCline(hdr)
        elif hdr.startswith('a='):
            if hasMlineParsed:
                mline = sdp.getLastMline()
                mline.appendAline(hdr)
            else:
                sdp.appendALine(hdr)
        elif hdr.startswith('m='):
            hasMlineParsed = True
            mline = SDPMLine()
            try:
                mline.setMline(hdr,content)
                sdp.appendMline(mline)
            except:
                print("******could not set and append mline", hdr)
            
    return sdp            
      
    
def parseJson():
    data = None
    filepath = glob.glob('/root/useragent/json/*.json')[0]
    with open(filepath) as file:
        data = json.load(file)
    usr_input = None
    for key in data:
        usr_input = data.get(key)
    return usr_input

def parseCallFlow(data):
    key_len = len(data)
    msg_len = key_len - 8
    map = {}
    for i in range(msg_len):
            map[i] = [data.get(str(i)).get("event"),data.get(str(i)) ]                        
    return map

def parseInputAndModifyMessage(map, message:SipMessage):    
    for key, values in map.items():
        if key == "INS_HDR":
            for value in values:
                hdr_name = value.split(':')[0]
                hdr_name = getHeaderName(hdr_name)
                hdr_value = value.split(':')[1]
                message.removeHeader(hdr_name)
                message.addHeader(hdr_name, hdr_value)
        elif key == "REM_HDR":
            for value in values:
                hdr_name = value.split(':')[0]
                hdr_name = getHeaderName(hdr_name)
                message.removeHeader(hdr_name)
        elif key == "REP_HDR":
            for value in values:
                hdr_name = value.split(':')[0]
                hdr_name = getHeaderName(hdr_name)
                hdr_value = value.split(':')[1]
                message.replaceHeader(hdr_name, hdr_value)    
    
    
def buildContent(uaSession:UASession, port):
    content = ""
    sdp_version = 100

    content = f'v=0' + CRLF
    content += f'o=ua 1 {sdp_version} IN IP4 ua.automation.com' + CRLF
    content += f's= '+ CRLF
    content += f'c=IN IP4 {getMyHostIP()}' + CRLF
    content += f't=0 0' + CRLF

    mediadirection = "sendrecv"
    #audiocodecs = [0,8,18]
    audiocodecs = [18]
    content += f'm=audio '+str(port)+' RTP/AVP'
    for codec in audiocodecs:
        content += f' {int(codec)}'
    content +=  f' 101' + CRLF
    for codec in audiocodecs:
        if int(codec) == 0:
            content += f'a=rtpmap:0 PCMU/8000' + CRLF
        elif int(codec) == 8:
            content += f'a=rtpmap:8 PCMA/8000' + CRLF
        elif int(codec) == 18:
            content += f'a=rtpmap:18 G729/8000' + CRLF
    content += f'a=rtpmap:101 telephone-event/8000' + CRLF
    content += f'a=fmtp:101 0-15' + CRLF
    content += f'a={mediadirection}' + CRLF
    # if sdpmlines
    return content


def buildMessage(sipMessage:SipMessage, content:str) -> str:
    raw_message = ""
    if sipMessage.getRequestLine() != None:
        # Build Request                  
        raw_message = sipMessage.getRequestLine() + CRLF          
    else:
        raw_message = sipMessage.getResponseLine() + CRLF
    headers = sipMessage.getAllHeaders()    
    for header in headers:
        hdr_vals = headers[header]
        for hdr_val in hdr_vals:            
            raw_message += f'{header}:{hdr_val}' + CRLF
    raw_message += CRLF     
    raw_message += content           
    
    return raw_message 


def parseInputAndVerifyMessage(map, message:SipMessage):
    res = True
    for key, values in map.items():
        if key == "EXP_HDR":
            for hdr in values:
                res = message.isHeaderPresent(hdr)
        elif key == "EXP_HDRVALUE":
            for value in values:
                lst = value.split('=')
                hdr = lst[0]
                exp_val = lst[1]
                hdr_value = message.getHeader(hdr)[0]
                res = False if hdr_value.find(exp_val) == -1 else True
                
                
                
                
