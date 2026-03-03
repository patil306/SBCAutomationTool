import socket
from sipconstants import TransportType 

class SignalingSocket:
    
    def __init__(self, localip, localport, remoteip, remoteport, transtype) -> None:
        self.__rcvdBuffer = 2056
        self.__sock = None
        self.__remoteIP = None
        self.__remotePort = None
        self.__localIP = None
        self.__localPort = None
        self.___transType = None
        self.___rcvdAddr = None
        
    def getRcvdAddress(self):
        return self.___rcvdAddr
        
    def connectSocket(self):
        if self.___transType == TransportType.TCP.value:
            self.__sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.__sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
            local_address = (self.__localIP, self.__localPort)
            self.__sock.bind(local_address)
            remote_address = (self.__remoteIP, self.__remotePort)
            self.__sock.connect(remote_address)
            self.__sock.listen()
        elif self.___transType == TransportType.UDP.value:
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            local_address = (self.__localIP, self.__localPort)
            self.__sock.bind(local_address)
        
    def sendMessage(self, message):
        if self.___transType == TransportType.TCP.value:
            ret_code = True
            try:
                print ("Sending %s" % message)
                self.__sock.sendall(message.encode('utf-8'))
            except socket.error as e:
                print ("Socket error: %s" %str(e))
                ret_code = False
            except Exception as e:
                print ("Other exception: %s" %str(e))
                ret_code = False
            finally:
                return ret_code
        elif self.___transType == TransportType.UDP.value:
            pass
    def recvMessage(self):
        client, address = self.__sock.accept()
        self.___rcvdAddr = address
        data = client.recv(self.__rcvdBuffer)
        return data
    
    def closeSocket(self):
        self.__sock.close()
        
    
        