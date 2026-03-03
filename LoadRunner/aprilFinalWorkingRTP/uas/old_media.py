from sdp import SDP
from util import Util
#from transport import MediaSocket
#from uasession import UASession
#from useragent import chThread_sendMedia, chThread_recvMedia
import threading
import socket
import time


class Media:
    def __init__(self,loc_ip,loc_port,rem_ip,rem_port):
        self.__sockID =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__hostIP = loc_ip
        self.__hostport = loc_port
        self.__remoteIP = rem_ip
        self.__remptePort = rem_port 
        self.__stopMedia = False
        self.__inactivateMedia = False
        self.__stopReceiving = False
        self.__buffSize = 2056
        self.__senderThrd = None
        self.__receiverThrd = None
    
    def initiateMedia(self, direction, prefaudiocodec):
        self.__inactivateMedia = False if direction == "sendrecv" else True
        self.__receiverThrd = threading.Thread(target=self.startReceivingMedia, args=(prefaudiocodec, self.__inactivateMedia))
        self.__receiverThrd.start()
        if prefaudiocodec == 8:
            self.__senderThrd = threading.Thread(target=self.startSendingMedia, args=(prefaudiocodec,self.__inactivateMedia))
            self.__senderThrd.start()
          
    def startSendingMedia(self, prefaudiocodec, isstop=False): 
        self.__stopMedia = isstop 
        sequence_number = 300
        time_stamp = 300       
        while True:             
            if self.__stopMedia:  
                break
            elif self.__inactivateMedia:
                continue 
            if prefaudiocodec == 0: #G711-A
                payload = "d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d555d5d555d55555d5d55555d555d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d555d555d45551d45051d553545557d4d5d7d4d7d1d5d6d655d7d455d4d555d5d5d555d55555d5545455545454545555d4d4d6d0d0d3d2d3d2d3d0d1d7d55456535d5c5e595e5e5f5d525155d7d3dedac1cdcef5c1cdc655d05d41454c4f4d43"
            elif prefaudiocodec == 8: #G711-U
                payload = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7fffff7fff7f7fffff7f7fff7ffffffffffffffffffffffffffffffffffefffffe7efd7dfd7e75fc7375fe717b7e7afcfdf9fbfbf6fff9f87cfafd7dfcff7efefefe7efd7e7dfe7c7c7d7a7b7b7c7d7ffdfbf8f5f4f1f0f1f0f2f5f7fbff7a76716e6d6b6b6b6b6c6e70757cf9f2ebe8e3dfdedbe3dfe47ef46f62665e5e5f60"
                    
            rtp_params = {'version' : 2, 'padding' : 0, 'extension' : 0, 'csi_count' : 0, 
                              'marker' : 0, 'payload_type' : prefaudiocodec, 'sequence_number' : sequence_number, 
                              'timestamp' : time_stamp, 'ssrc' : 1234567, 'payload' : payload}   
            rtp_packet = generateRTPpacket(rtp_params)      
            remote_server = (self.__remoteIP, self.__remptePort)       
            self.__sockID.sendto(rtp_packet, remote_server)
            sequence_number += 1
            time_stamp += 160
            time.sleep(1)
     
    def startReceivingMedia(self, prefaudiocodec, isstop=False):
        self.__stopMedia = isstop
        local_host = (self.__hostIP, self.__hostport)
        self.__sockID.bind(local_host)
        while True:
            if self.__stopMedia:
                break
            elif self.__inactivateMedia:
                continue            
            rtp_packet, address = self.__sockID. recvfrom(self.__buffSize) 
            decodeRTPpacket(rtp_packet)
              
    def setRemoteMediaAddress(self, rem_ip, rem_port) :
        self.__remoteIP = rem_ip
        self.__remptePort = rem_port                    
    def resumeMedia(self):
        self.__stopMedia = False
    def stopMedia(self):
        self.__stopMedia = True 
    def inactivateMedia(self):
        self.__inactivateMedia = True
    def closeSocket(self):
        self.__sockID.close()
    def getSenderThread(self):
        return self.__senderThrd
    def getReceiverThread(self):
        return self.__receiverThrd

def processMedia():    
    pass
    
def buildRTPAttributes(codec):
    data = ""
    return data.encode('utf-8')   

def initiateMediaFlow(mediaObj, direction):    
    stop_flag = False if direction == "sendrecv" else True
    Util.chThread_recvMedia = threading.Thread(target=mediaObj.startReceivingMedia, args=(stop_flag))
    Util.chThread_recvMedia.start()
    data = buildRTPAttributes()
    Util.chThread_sendMedia = threading.Thread(target=mediaObj.startSendingMedia, args=(data, stop_flag))
    Util.chThread_sendMedia.start()
        
def procSDPAndUpdateMediaFlow(loc_sdp:SDP, rem_sdp:SDP, mediaObj):  
    loc_dir = procSDPAndGetMedDirection(loc_sdp)
    rem_dir = procSDPAndGetMedDirection(rem_sdp)
    stop_flag = False if loc_dir == "sendrecv" and rem_dir == "sendrecv" else True    
    if stop_flag:
        mediaObj.stopMedia()
        
def procSDPAndGetMediaParams(sdp:SDP):    
    mediaIP = sdp.getClineIP()
    mediaport = 0
    mediadir = 'sendrecv'    
    mlines = sdp.getMlines()
    prefaudiocodec = mlines[0].getPreferCodec() if mlines else 0
    for mline in mlines:
        mediaIP = mline.getMediaIP() if mline.getMediaIP() else sdp.getClineIP()
        mediaport = mline.getMediaPort()
        mediadir = mline.getMediaDirection()                    
    print(mediaIP)
    print(mediaport)
    print(mediadir)
    print(prefaudiocodec)
    print("zzz")
    return mediaIP, mediaport, mediadir, prefaudiocodec

def procSDPAndGetMedDirection(sdp:SDP):
    mlines = sdp.getMlines()
    direction = 'sendrecv'
    for mline in mlines:
        direction = mline.ggetMediaDirection()
    return direction


def generateRTPpacket(rtp_params):

    ##Example Usage:
    #payload = 'd5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5'
    #packet_vars = {'version' : 2, 'padding' : 0, 'extension' : 0, 'csi_count' : 0, 'marker' : 0, 'payload_type' : 8, 'sequence_number' : 306, 'timestamp' : 306, 'ssrc' : 185755418, 'payload' : payload}
    #GenerateRTPpacket(packet_vars)             #Generates hex to send down the wire

  
    #The first twelve octets are present in every RTP packet, while the list of CSRC identifiers is present only when inserted by a mixer.
    #Generate first byte of header as binary string:
    version = str(format(rtp_params['version'], 'b').zfill(2))                  #RFC189 Version (Typically 2)
    padding = str(rtp_params['padding'])                                        #Padding (Typically false (0))
    extension = str(rtp_params['extension'])                                    #Extension - Disabled
    csi_count = str(format(rtp_params['csi_count'], 'b').zfill(4))              #Contributing Source Identifiers Count (Typically 0)
    byte1 = format(int((version + padding + extension + csi_count), 2), 'x').zfill(2)                           #Convert binary values to an int then format that as hex with 2 bytes of padding if requiredprint(byte1)

    #Generate second byte of header as binary string:
    marker = str(rtp_params['marker'])                                          #Marker (Typically false)
    payload_type = str(format(rtp_params['payload_type'], 'b').zfill(7))        #7 bit Payload Type (From https://tools.ietf.org/html/rfc3551#section-6)
    byte2 = format(int((marker + payload_type), 2), 'x').zfill(2)               #Convert binary values to an int then format that as hex with 2 bytes of padding if required

    sequence_number = format(rtp_params['sequence_number'], 'x').zfill(4)                               #16 bit sequence number (Starts from a random position and incriments per packet)
    
    timestamp = format(rtp_params['timestamp'], 'x').zfill(8)                   #(Typically incrimented by the fixed time between packets)
    
    ssrc = str(format(rtp_params['ssrc'], 'x').zfill(8))                        #SSRC 32 bits           (Typically randomly generated for each stream for uniqueness)

    payload = rtp_params['payload']

    packet = byte1 + byte2 + sequence_number + timestamp + ssrc + payload
    #print(packet)
    return packet    

def decodeRTPpacket(packet_bytes):
    ##Example Usage:
    #packet_bytes = '8008d4340000303c0b12671ad5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5d5'
    #rtp_params = DecodeRTPpacket(packet_bytes)
    #Returns dict of variables from packet (packet_vars{})
    packet_vars = {}
    byte1 = packet_bytes[0:2]           #Byte1 as Hex
    byte1 = int(byte1, 16)              #Convert to Int
    byte1 = format(byte1, 'b')          #Convert to Binary
    packet_vars['version'] = int(byte1[0:2], 2)     #Get RTP Version
    packet_vars['padding'] = int(byte1[2:3])        #Get padding bit
    packet_vars['extension'] = int(byte1[3:4])        #Get extension bit
    packet_vars['csi_count'] = int(byte1[4:8], 2)     #Get RTP Version

    byte2 = packet_bytes[2:4]

    byte2 = int(byte2, 16)              #Convert to Int
    byte2 = format(byte2, 'b').zfill(8) #Convert to Binary
    packet_vars['marker'] = int(byte2[0:1])
    packet_vars['payload_type'] = int(byte2[1:8], 2)

    packet_vars['sequence_number'] = int(str(packet_bytes[4:8]), 16)

    packet_vars['timestamp'] = int(str(packet_bytes[8:16]), 16)

    packet_vars['ssrc'] = int(str(packet_bytes[16:24]), 16)

    packet_vars['payload'] = str(packet_bytes[24:])
    return packet_vars

