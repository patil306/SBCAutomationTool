from sipconstants import CRLF, CR, LF, SipHeaders
from util import Util
from queue import Empty
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
        print("*****message added to String Buffer", data)
        self.__stringBuffer += data
        
    def isStopReading(self):
        return self.__stopReading
    '''
    def readFromStringBuffer(self):  
        print("****Reading from String Buffer")      
        buff_idx = 0        
        while True:            
            #print("**** len of stringbuffer:", len(self.__stringBuffer))
            if self.__stopReading:
                break
            if self.__stringBuffer[buff_idx:]: 
                print("*** Something rececived TO CAPTURE ***")                
                #temp_buff =  self.__stringBuffer[buff_idx:]       
                cur_idx = self.__stringBuffer.find(CRLF+CRLF, buff_idx)                
                if cur_idx == -1: 
                    print("*** CURR IDX NEGATIVE ***")
                    continue  
                cur_idx += 4                                     
                message = self.__stringBuffer[buff_idx:cur_idx]  
                headers = message.split(CRLF)
                cont_len = 0
                isContLenFound = False
                for hdr in headers:
                    if hdr.startswith(SipHeaders.CONTENTLENGTH.value):
                        isContLenFound = True
                        cont_len = int(hdr.split(":")[1].strip())
                        
                if not isContLenFound:
                    print("*** CONT LEN NOT FOUND ***")
                    continue
                cur_idx += cont_len
                self.appendMessage(self.__stringBuffer[buff_idx:cur_idx])                
                buff_idx = cur_idx                          
                    
            else:
                #time.sleep(2)
                continue    
        '''        
    def getStringBuffer(self):
        return self.__stringBuffer   
    def appendMessage(self, msg):
        #self.__msg_buffer.append(msg)
        print("*****Received message", msg)
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
            print("***fragmenting")
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


def readFromStringBuffer(msg_queue, queue):  
    print("****Reading from String Buffer")      
    buff_idx = 0 
    string_buffer = ""       
    while True:            
        if Util.stop_reading_msgBuff:
            return
        try:
            string_buffer += queue.get(True, 5)
            if string_buffer[buff_idx:]:
                print("*** Something rececived TO CAPTURE ***")
                #temp_buff =  self.__stringBuffer[buff_idx:]
                cur_idx = string_buffer.find(CRLF+CRLF, buff_idx)
                if cur_idx == -1:
                    print("*** CURR IDX NEGATIVE ***")
                    continue
                cur_idx += 4
                message = string_buffer[buff_idx:cur_idx]
                headers = message.split(CRLF)
                cont_len = 0
                isContLenFound = False
                for hdr in headers:
                    if hdr.startswith(SipHeaders.CONTENTLENGTH.value):
                        isContLenFound = True
                        cont_len = int(hdr.split(":")[1].strip())

                if not isContLenFound:
                    print("*** CONT LEN NOT FOUND ***")
                    continue
                cur_idx += cont_len
                msg_queue.put(getMessageEvtAndMessage(string_buffer[buff_idx:cur_idx]))
                buff_idx = cur_idx
            else:
                #time.sleep(2)
                continue
        except Empty:
            if string_buffer[buff_idx:]:
                print("*** Something rececived TO CAPTURE ***")
                #temp_buff =  self.__stringBuffer[buff_idx:]
                cur_idx = string_buffer.find(CRLF+CRLF, buff_idx)
                if cur_idx == -1:
                    print("*** CURR IDX NEGATIVE ***")
                    continue
                cur_idx += 4
                message = string_buffer[buff_idx:cur_idx]
                headers = message.split(CRLF)
                cont_len = 0
                isContLenFound = False
                for hdr in headers:
                    if hdr.startswith(SipHeaders.CONTENTLENGTH.value):
                        isContLenFound = True
                        cont_len = int(hdr.split(":")[1].strip())

                if not isContLenFound:
                    print("*** CONT LEN NOT FOUND ***")
                    continue
                cur_idx += cont_len
                msg_queue.put(getMessageEvtAndMessage(string_buffer[buff_idx:cur_idx]))
                buff_idx = cur_idx

            continue

def getMessageEvtAndMessage(msg):
    print("*****Received message", msg)
    fline = msg.split(CRLF,1)[0]
    evt = None
    var = fline.split(" ")
    if fline.startswith('SIP/2.0'):            
        evt = var[1]            
    elif var[-1].startswith("SIP/2.0"):
        evt = var[0]
    return [evt, msg]   
        