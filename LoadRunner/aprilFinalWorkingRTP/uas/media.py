from sdp import SDP
from util import Util
#from testreport import TestReport
#from sipconstants import TestCaseResult
import threading
import socket, sys
import base64
from pylibsrtp import Policy, Session
import time
import socket,sys, errno

class Media:
    def __init__(self,loc_ip,loc_port,rem_ip,rem_port):
        #self.__recvSockId = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sendSockId = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
        self.__hostIP = loc_ip
        self.__hostPort = int(loc_port)
        self.__remoteIP = rem_ip
        self.__remptePort = int(rem_port) 
        self.__stopMedia = False
        self.__inactivateMedia = False        
        self.__buffSize = 2048
        self.__senderThrd = None
        self.__receiverThrd = None
    
    def initiateMedia(self, direction, prefaudiocodec, txKey, rxKey):
        self.__inactivateMedia = False if direction == "sendrecv" else True
        #self.__receiverThrd = threading.Thread(target=self.startReceivingMedia, args=(prefaudiocodec, rxKey))
        #self.__receiverThrd.start()
        self.__senderThrd = threading.Thread(target=self.startSendingMedia, args=(prefaudiocodec, txKey))        
        self.__senderThrd.start()
        #self.__senderThrd.join()
                  
    def startSendingMedia(self, prefaudiocodec, txKey):
        prefaudiocodec = int(prefaudiocodec)         
        sequence_number = 1
        time_stamp = 300  
        #print("!!!! in Start Sending Media!!!!") 
        
        end_tme = time.time() + 180
        #while sequence_number < 1000:
        while time.time() < end_tme:
            if self.__stopMedia:   
                #print("****stop sending Media***")               
                break
            if self.__inactivateMedia:
                continue             
            payload = ""            
            if prefaudiocodec == 0: #G711-A
                payload = "d5"*160
            elif prefaudiocodec == 8: #G711-U
                payload = "f3"*160
            elif prefaudiocodec == 18: #G711-U
                payload = "d5"*160

                     
            rtp_params = {'version' : 2, 'padding' : 0, 'extension' : 0, 'csi_count' : 0, 
                              'marker' : 1, 'payload_type' : prefaudiocodec, 'sequence_number' : sequence_number, 
                              'timestamp' : time_stamp, 'ssrc' : 1234567, 'payload' : payload}   
            rtp_packet = generateRTPpacket(rtp_params) 
            data = bytes.fromhex(rtp_packet)
            #if txKey:
            #    key = base64.b64decode(txKey)
            #    tx_policy = Policy(key=key, ssrc_type=Policy.SSRC_ANY_OUTBOUND)
            #    tx_session = Session(policy=tx_policy)
            #    data = tx_session.protect(data)

            remote_server = (self.__remoteIP, self.__remptePort)
            try:
                self.__sendSockId.sendto(data, remote_server)
            except socket.error as e:
                #print("socket error in sending media ", e)
                pass
            except IOError as e:
                if (e.errno == errno.EPIPE):
                    print("IO error in sending media ignoring :-", e)
                    pass
            except:
                print("sending media exception")
            #rtp_count += 1
            #print("!!!!!RTP Packet Sent to remote Server", remote_server)
            sequence_number += 1
            if sequence_number == 65536:
                sequence_number = 1
            time_stamp += 160
            time.sleep(0.005)

        self.__sendSockId.close()
               
     
    def startReceivingMedia(self, prefaudiocodec, rxKey):
        prefaudiocodec = int(prefaudiocodec)
        self.__recvSockId.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        local_host = (self.__hostIP, self.__hostPort)
        self.__recvSockId.bind(local_host)        
        #test_report = TestReport.getInstance()
        #print("=====Receiving Media====")
        recv_count = 0
        end_tme = time.time() + 180
        rtp_count = 0
        while time.time() < end_tme:
            if self.__stopMedia:                
                break
            if self.__inactivateMedia:
                continue
            self.__recvSockId.settimeout(2)
            try:
                rtp_packet, address = self.__recvSockId.recvfrom(self.__buffSize)
                #rtp_string = rtp_packet.hex() if not rxKey else rtp_packet
                if rxKey:
                    key = base64.b64decode(rxKey)
                    rx_policy = Policy(key=key, ssrc_type=Policy.SSRC_ANY_INBOUND)
                    rx_session = Session(policy=rx_policy)
                    #rtp_string = rx_session.unprotect(rtp_string).hex()
                '''payload_string = getPayloadFromRtpString(rtp_string)
                if payload_string:
                    #print(payload_string)
                    pass
                    #test_report.setMediaReport(TestCaseResult.PASS.value)
                else:
                    pass'''
                    #test_report.setMediaReport(TestCaseResult.FAIL.value)
                # rtp_map = decodeRTPpacket(rtp_string)
                # rcvd_payload = rtp_map.get('payload')
                # print("###### payload recevied", rcvd_payload)
                # my_payload = ""
                # if prefaudiocodec == 8:
                #     my_payload = "f3"*160
                # elif prefaudiocodec == 0:
                #     my_payload = "d5"*160
                #
                # if  rcvd_payload == my_payload:
                #     # print("MEDIA TEST PASS")
                #     test_report.setMediaReport(TestCaseResult.PASS.value)
                # else:
                #     test_report.setMediaReport(TestCaseResult.FAIL.value)
                    # print("MEDIA TEST FAIL")
                # recv_count += 1
                # if recv_count == 5:
                #     print("5 packets received successfully")
                #     break
            except socket.timeout as e:
                err = e.args[0]
                if err == 'timed out':
                    #print("Recv Socket timeout, retry after 1sec")
                    time.sleep(1)
                    continue
                else:
                    print("SOCKET TIMEOUT ++++++")
                    print(e)
                    sys.exit(1)

    def setRemoteMediaAddress(self, rem_ip, rem_port) :
        self.__remoteIP = rem_ip
        self.__remptePort = rem_port                    
    def resumeMedia(self):
        self.__inactivateMedia = False
    def stopMedia(self):
        self.__stopMedia = True 
    def inactivateMedia(self):
        self.__inactivateMedia = True
    def closeSocket(self):
        self.__recvSockId.close()
        self.__sendSockId.close()
    def getSenderThread(self):
        return self.__senderThrd
    def getReceiverThread(self):
        return self.__receiverThrd
   
def procSDPAndGetMediaParams(sdp:SDP):
    #print("procSDPAndGetMediaParams")
    mediaIP = sdp.getClineIP()
    mediaport = 0
    mediadir = 'sendrecv'
    srtpkey = ""
    mlines = sdp.getMlines()
    prefaudiocodec = mlines[0].getPreferCodec() if mlines else 0
    for mline in mlines:
        mediaIP = mline.getMediaIP() if mline.getMediaIP() else sdp.getClineIP()
        mediaport = mline.getMediaPort()
        mediadir = mline.getMediaDirection()
        srtpkey = mline.getSRTPKey()
    #print("procSDPAndGetMediaParams")
    return mediaIP, mediaport, mediadir, prefaudiocodec, srtpkey

def procSDPAndGetMedDirection(sdp:SDP):
    mlines = sdp.getMlines()
    direction = 'sendrecv'
    for mline in mlines:
        direction = mline.getMediaDirection()
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
    byte1 = format(int((version + padding + extension + csi_count), 2), 'x').zfill(2)  #Convert binary values to an int then format that as hex with 2 bytes of padding if requiredprint(byte1)

    #Generate second byte of header as binary string:
    marker = str(rtp_params['marker'])                                          #Marker (Typically false)
    payload_type = str(format(rtp_params['payload_type'], 'b').zfill(7))        #7 bit Payload Type (From https://tools.ietf.org/html/rfc3551#section-6)
    byte2 = format(int((marker + payload_type), 2), 'x').zfill(2)               #Convert binary values to an int then format that as hex with 2 bytes of padding if required
    sequence_number = format(rtp_params['sequence_number'], 'x').zfill(4)       #16 bit sequence number (Starts from a random position and incriments per packet)
    timestamp = format(rtp_params['timestamp'], 'x').zfill(8)                   #(Typically incrimented by the fixed time between packets)
    ssrc = str(format(rtp_params['ssrc'], 'x').zfill(8))                        #SSRC 32 bits (Typically randomly generated for each stream for uniqueness)
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
def getPayloadFromRtpString(rtp_string):
    return str(rtp_string[24:])

