import re
from typing import List
from sipconstants import SipHeaders

class SipMessage:
    def __init__(self):        
        self.__headers = {}
        self.__reqLine = None
        self.__respLine = None
        self.__sdpBody = None
        self.__isRequest = True
    
    def setMessageType(self, isRequest):
        self.__isRequest = isRequest
        
    def isRequest(self):
        return self.__isRequest
                
    def setRequestLine(self, reqline):
        self.__reqLine = reqline
        self.__respLine = None
        self.__isRequest = True
        
    def getRequestLine(self):
        return self.__reqLine
    
    def getRequestURL(self):
        url = self.__reqLine if self.__isRequest else self.__respLine
        return url.split(" ")[1]

    def replaceRequestURI(self, url):
        if not self.__isRequest:
            return
        req_line = self.__reqLine
        urls = req_line.split(" ")
        new_url = f'{urls[0]} {url} {urls[2]}'
        self.__reqLine = new_url
   
    def getRequestURLParam(self):
        url = self.getRequestURL()
        return url.split(';')[1]
    
    def getReqURIUserPart(self):
        url = self.getRequestURL()
        uri = url.split(';')[0]
        return uri.split(':',1)[1].split('@')[0]
    
    def getReqURIHostPart(self):
        url = self.getRequestURL()
        uri = url.split(';')[0]
        return uri.split(':',1)[1].split('@')[1].split(':')[0]
    
    def setResponseLine(self, respline):
        self.__respLine = respline
        self.__reqLine = None
        self.__isRequest = False
        
    def getResponseLine(self):
        return self.__respLine

    def addHeader(self,hdr_name,hdr_value): 
        hdr_name = getHeaderName(hdr_name)                       
        if hdr_name not in self.__headers:
            self.__headers[hdr_name] = [hdr_value]
        else:
            self.__headers[hdr_name].append(hdr_value)

    def removeHeader(self,hdr_name):
        hdr_name = getHeaderName(hdr_name)
        if hdr_name in self.__headers:
            self.__headers.pop(hdr_name)

    def removeAllHeadersExcept(self, hdr_list:List):
        keys = list(self.__headers.keys())
        [self.__headers.pop(hdr) for hdr in keys if hdr not in hdr_list]

    def replaceHeader(self, hdr_name, hdr_value):
        hdr_name = getHeaderName(hdr_name)
        self.removeHeader(hdr_name)
        self.addHeader(hdr_name, hdr_value)
            
    def getAllHeaders(self):
        return self.__headers
    
    def getHeader(self, Hdr_name):
        return self.__headers.get(Hdr_name)
    
    def getCallID(self):
        return self.getHeader(SipHeaders.CALLID.value)[0]

    def getCSeq(self):
        cseqVal = self.getHeader(SipHeaders.CSEQ.value)
        return int(cseqVal[0].split(" ")[0])
    
    def getRSeq(self):
        rseqval = self.getHeader(SipHeaders.RSEQ.value)
        return int(rseqval[0].strip()) if rseqval else 0
    
    def getFromTag(self):
        frm_hdr = self.getHeader(SipHeaders.FROM.value)[0]        
        tag = re.search('tag=(.*)', frm_hdr)
        return tag.group(1) if tag else ""        
        
        
    def getToTag(self):
        to_hdr = self.getHeader(SipHeaders.TO.value)[0]
        tag = re.search('tag=(.*)', to_hdr)
        return tag.group(1) if tag else ""
        
    
    def getMethod(self):
        cseq = self.getHeader(SipHeaders.CSEQ.value)[0]
        cseq = cseq.split(' ')
        return cseq[-1]
    
    def getRemoteURL(self):
        hdr_contact = self.__headers[SipHeaders.CONTACT.value][0]
        remote_url = None
        # if hdr_contact.startswith('"') or hdr_contact.startswith('<'):
        #     remote_url = re.search(r"\<([A-Za-z0-9_.@:]+)\>", hdr_contact).group(1)
        # else:        
        remote_url = re.search('<(.*)>', hdr_contact).group(1)
        print("&&&&&&&&&&&&", remote_url)
        return remote_url           
         
    def getResponseCode(self):
        resp_line = self.__respLine
        return resp_line.split(" ")[1]
    
    def getResponseText(self):
        resp_line = self.__respLine
        return resp_line.split(" ",2)[2]
    
    def addContent(self, sdp):
        self.__sdpBody = sdp
        
    def getContent(self):
        return self.__sdpBody
    
    def isResponseReliable(self):       
       supported = self.getHeader(SipHeaders.SUPPORTED.value)[0]
       if supported:
           supported = supported.split(',')
       require = self.getHeader(SipHeaders.REQUIRE.value)[0]
       require = require.split(',')
       rseq = self.getHeader(SipHeaders.RSEQ.value)[0]
       if '100rel' in supported or '100rel' in require and rseq:
           return True
       else:
           return False       
    
    def getRecordRoutes(self, isDlgOwner) -> list:
        routeset = self.getHeader(SipHeaders.RECORDROUTE.value)
        if not routeset:            
            routeset =  []
        if isDlgOwner:            
            routeset.reverse()
        return routeset
        
        
    def isHeaderPresent(self,hdr_name):
        val = self.getHeader(hdr_name)
        return True if val else False

    def getEvent(self):
        return self.getHeader(SipHeaders.EVENT.value)[0]
    
def getHeaderName(hdr_name):
    if hdr_name.startswith('Call-ID'):
        hdr_name = SipHeaders.CALLID.value
    elif hdr_name.startswith('From'):
        hdr_name = SipHeaders.FROM.value
    elif hdr_name.startswith('To'):
        hdr_name = SipHeaders.TO.value
    elif hdr_name.startswith('Via'):
        hdr_name = SipHeaders.VIA.value
    elif hdr_name.startswith('CSeq'):
        hdr_name = SipHeaders.CSEQ.value
    elif hdr_name.startswith('Max-Forwards'):
        hdr_name = SipHeaders.MAXFORWARDS.value
    elif hdr_name.startswith('Contact'):
        hdr_name = SipHeaders.CONTACT.value
    elif hdr_name.startswith('Content-Type'):
        hdr_name = SipHeaders.CONTENTTYPE.value
    elif hdr_name.startswith('Content-Length'):
        hdr_name = SipHeaders.CONTENTLENGTH.value
    elif hdr_name.startswith('Supported'):
        hdr_name = SipHeaders.SUPPORTED.value
    elif hdr_name.startswith('WWW-Authenticate'):
        hdr_name = SipHeaders.WWWAUTHENTICATE.value
    elif hdr_name.startswith('Allow'):
        hdr_name = SipHeaders.ALLOW.value
    elif hdr_name.startswith('Require'):
        hdr_name = SipHeaders.REQUIRE.value
    elif hdr_name.startswith('Record-Route'):
        hdr_name = SipHeaders.RECORDROUTE.value
    elif hdr_name.startswith("Route"):
        hdr_name = SipHeaders.ROUTE.value
    elif hdr_name.startswith('RSeq'):
        hdr_name = SipHeaders.RSEQ.value
    elif hdr_name.startswith('RAck'):
        hdr_name = SipHeaders.RACK.value
    elif hdr_name.startswith('Event'):
        hdr_name = SipHeaders.EVENT.value
        #unknown headers
        pass
        
    return hdr_name
