from sipconstants import CRLF, CR, LF, SipHeaders
import time

class MessageBuffer:
    def __init__(self):
        self.__stringBuffer = ""
        self.__msg_buffer = []
        self.__evtList = []
        self.__stopReading = False
    
    def stopReading(self):
        self.__stopReading = True
    def startReading(self):
        self.__stopReading = False
        self.readFromStringBuffer() 
    def addToStringBuffer(self, data:str):
        self.__stringBuffer += data
    def readFromStringBuffer(self):        
        buff_idx = 0
        isfirstCRLF = False
        issecondCRLF = False
        while True:
            
            #print("**** len of stringbuffer:", len(self.__stringBuffer))
            if self.__stopReading:
                break
            if self.__stringBuffer[buff_idx:]: 
                #print("*** STH TO CAPTURE ***")
                #print("****buff_idx:",buff_idx)
                #print("***stringBuff",self.__stringBuffer[buff_idx:] ) 
                #temp_buff =  self.__stringBuffer[buff_idx:]       
                cur_idx = self.__stringBuffer.find(CRLF+CRLF, buff_idx)
                #print("***cur_idx", cur_idx)
                if cur_idx == -1: 
                    #print("*** CURR IDX NEGATIVE ***")
                    continue  
                cur_idx += 4  
                #issecondCRLF = True if isfirstCRLF else False
                #isfirstCRLF = True                      
                message = self.__stringBuffer[buff_idx:cur_idx]  
                headers = message.split(CRLF)
                cont_len = 0
                isContLenFound = False
                for hdr in headers:
                    if hdr.startswith(SipHeaders.CONTENTLENGTH.value):
                        isContLenFound = True
                        cont_len = int(hdr.split(":")[1].strip())
                        #print("**** cont_len:", cont_len)
                if not isContLenFound:
                    #print("*** CONT LEN NOT FOUND ***")
                    continue
                cur_idx += cont_len
                self.appendMessage(self.__stringBuffer[buff_idx:cur_idx])
                #print("@@@@", self.__stringBuffer[buff_idx:cur_idx])
                buff_idx = cur_idx                          
                    
            else:
                #time.sleep(2)
                continue            
        
    def appendMessage(self, msg):
        #self.__msg_buffer.append(msg)
        
        fline = msg.split(CRLF,1)[0]
        evt = None
        var = fline.split(" ")
        if fline.startswith('SIP/2.0'):            
            evt = var[1]
            self.__msg_buffer.append([evt,msg])
        elif var[-1].startswith("SIP/2.0"):
            evt = var[0]
            self.__msg_buffer.append([evt,msg])
        else:            
            #print("***fragmenting")
            evt = 'fragment'
            self.__msg_buffer.append([evt,msg])     

        
        
    def popTopMessage(self):
        if self.__msg_buffer:            
            val = self.__msg_buffer.pop(0)            
            return (val[0],val[1])
        else:
            return ("","")
            
    def getEventList(self):
        return self.__evtList
            