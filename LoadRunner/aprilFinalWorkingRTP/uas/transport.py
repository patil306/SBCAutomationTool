import socket
from messagebuffer import MessageBuffer
from sipconstants import Transport 
#from media import processMedia
import time
import sys, errno
class SignalingSocket:
    
    def __init__(self, localip, localport, remoteip, remoteport, transport:Transport):
        self.__rcvdBuffer = 2056        
        self.__remoteIP = remoteip
        self.__remotePort = remoteport
        self.__localIP = localip
        self.__localPort = localport
        self.___transport = transport
        self.___remoteAddress = None
        self.__sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) if transport == Transport.TCP.value else socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__connId = None
        
    def getRcvdAddress(self):
        return self.___remoteAddress
    def setSocket(self):
        if self.___transport == Transport.TCP.value:
            self.__sock =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        elif self.___transport == Transport.UDP.value:
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def  connectSocket(self):
        self.___remoteAddress = (self.__remoteIP, self.__remotePort)
        self.__sock.connect(self.___remoteAddress)
        
    def sendMessage(self, message:str):
       # print("Transport - SendMessage")
        if self.___transport == Transport.TCP.value:
            ret_code = True
            try:
              #  print ("Sending %s" % message)
                # print(message)
                message = message.encode('utf-8')
                if self.__connId:
                    self.__connId.send(bytes(message))
                 #   print("inside If")
                else:
                    self.__sock.sendall(bytes(message))
                #    print("inside else")
                # print("=====send Success!")
            except socket.error as e:
                print ("Socket error: %s" %str(e))
                ret_code = False
            except Exception as e:
                print ("Other exception: %s" %str(e))
                ret_code = False
            except IOError as e:
                print("IO error in transport ", e)
                if (e.errno == errno.EPIPE):
                    print("ignoring pipe error")
                    pass
                ret_code = False
            except:
                print("unknown exception in transport")
                ret_code = False
                pass
            finally:
                # print("return code is:" + f'{ret_code}')
                return ret_code
        elif self.___transport == Transport.UDP.value:
            pass
    def recvMessage(self):
        data = ""
        try:
            data = self.__sock.recv(self.__rcvdBuffer)
            return data
        except:
            print("exception in recvMessge transport")

        return data
    
    def closeSocket(self):
        self.__sock.close()
        
    def getSockId(self):
        return self.__sock

    def setConnectionId(self, conn_id):
        self.__connId = conn_id

    def getConnectionId(self):
        return self.__connId

    def getLocalAddress(self):
        return (self.__localIP, self.__localPort)
 

    
    
        
