from sipconstants import CRLF
import ipaddress

class SDPMLine:
    def __init__(self):
        self.__mLine = ""
        self.__aLines = []
        self.__cLine = None
        self.__mediaType = 'audio'
        self.__mediaIP = ""
        self.__mediaPort = 0
        self.__prefCodec = 0
        self.__isSRTP = True        
        
    def setMline(self, mline):
        self.__mLine = mline
        mline = mline.split(' ')
        self.__mediaType = mline[0]
        self.__mediaPort = mline[1]
        self.__isSRTP = True if mline[2].startswith('SRTP') else False
        self.__prefCodec = mline[3]
        self.__mediadir = 'sendrecv'        
        
    def getMline(self):
        return self.__mLine
    
    def setCline(self, cline):
        self.__cLine = cline
        cline = cline.split(' ')
        self.__mediaIP = cline[-1]
    
    def appendAline(self, aline):
        attr = aline.split('=')[1].strip()
        if attr in ['sendonly','inactive','recvonly']:
            if attr == 'sendonly':
                self.__mediadir = 'recvonly'
            elif attr == 'recvonly':
                self.__mediadir = 'recvonly'
            elif attr == 'inactive':
                self.__mediadir = 'inactive'
            else:
                self.__mediadir = 'sendrecv'
        self.__aLines.append(aline)
        
    def getAlines(self):
        return self.__aLines 
    
    def getMediaType(self):
        return self.__mediaType
    def getMediaPort(self):
        return self.__mediaPort
    def getMediaIP(self):
        return self.__mediaIP
    def getPreferCodec(self):
        return self.__prefCodec 
    def getCLine(self):
        return self.__cLine
    def getMediaDirection(self):
        return self.__mediadir
    def isSRTP(self):
        return self.__isSRTP

class SDP:
    def __init__(self):
        self.__vLine = ""
        self.__oLine = ""
        self.__sLine = ""
        self.__tLine = ""
        self.__cLine = ""
        self.__aLine = []
        self.__mLines = []
        self.__contentLen = 0
        
    def setVline(self,vline):
        self.__vLine = vline
        
    def getVline(self):
        return self.__vLine
    
    def setOline(self, oline):
        self.__oLine = oline
        
    def getOline(self):
        return self.__oLine
    
    def setSline(self, sline):
        self.__sLine = sline
        
    def getSline(self):
        return self.__sLine
    
    def setTline(self, tline):
        self.__tLine = tline
        
    def getTline(self):
        return self.__tLine
    
    def setCline(self, cline):
        self.__cLine = cline
        
    def getCline(self):
        return self.__cLine
    
    def getClineIP(self):
        cline = self.__cLine
        if cline:
            clines = cline.split(' ')
            return clines[-1]
        else:
            return '0.0.0.0'
      
    def getMlines(self):
        return self.__mLines
    
    def getLastMline(self) -> SDPMLine:
        return self.__mLines[-1]
    
    def appendMline(self, mline:SDPMLine):
        self.__mLines.append(mline)
        
    def appendALine(self, aline):
        self.__aLine.append(aline)
        
    def setContentLength(self, len):
        self.__contentLen = len
        
    def getContentLength(self):
        return self.__contentLen
    
    def buildContentFromSDP(self) -> str:
        medialines = self.getMlines()
        content = self.getVline() + CRLF
        content += self.getOline() + CRLF
        content += self.getSline() + CRLF
        content += self.getCline() + CRLF
        content += self.getTline() + CRLF        
        for medialine in medialines:
            mline = medialine.getMline()
            content += mline + CRLF
            alines = medialine.getAlines()
            for aline in alines:
                content += aline + CRLF
    
        return content
        
        
    
        
def buildMlineAndAttributes(medialine:SDPMLine):    
    mediatype = medialine.getMediaType()
    codeclist = medialine.getCodecList()
    dtmf = medialine.getDTMF()
    ip = medialine.getMediaIP()
    port = medialine.getMediaPort()
    direction = medialine.getMediaDirection()
    rtpavp = 'RTP/AVP' if medialine.isRTPMedia() else 'SRTP/SAVP'
    mediaattrstring =  f'm= {mediatype} {port} {rtpavp} '
    for codec in codeclist:
        mediaattrstring += f'{codec} '
    mediaattrstring += f'{dtmf}'
    mediaattrstring += CRLF
    for codec in codeclist:
        attr = payloadNumToCodecAttrMappinging(codec)
        mediaattrstring += attr + CRLF
    fmtp = f'a= rtpmap:{dtmf} telephone-event/8000' + CRLF + f'a= fmtp:{dtmf} 0-16'
    mediaattrstring += fmtp + CRLF
    dirattr = f'a= {direction}'
    mediaattrstring += dirattr + CRLF
    
    return mediaattrstring    
    
        
def payloadNumToCodecAttrMappinging(payload):
    attr = ""
    if payload == 0:
        attr = f'a= rtpmap:{payload} PCMU/8000'
    elif payload == 8:
        attr = f'a= rtpmap:{payload} PCMA/8000'
    elif payload == 18:
        attr = f'a= rtpmap:{payload} G729/8000'
        
    return attr
        

    
   