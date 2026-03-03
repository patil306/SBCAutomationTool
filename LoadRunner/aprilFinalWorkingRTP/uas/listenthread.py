from messagebuffer import MessageBuffer
import socket, time, sys

from transport import SignalingSocket

class ListenThread:
    def __init__(self):
        self.__stopThread = False
    
    def setStopThread(self, st):
        self.__stopThread = st
        
    def startListening(self, sock:SignalingSocket, msg_buffer:MessageBuffer, isUAC):
        sockid = sock.getSockId()
        if not isUAC:
            #print("****Listening for UAS with sockId", sockid)
            local_address = sock.getLocalAddress()
            sockid.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sockid.bind(local_address)
            sockid.listen(5)
            while True:
                conn = None
                print("***waiting for new connection")
                try:
                    conn, addr = sockid.accept()
                    #print("****client Addr", addr)
                    if conn:
                        print("********Clinet Request Accepted", conn)
                        sock.setConnectionId(conn)
                        break
                except Exception as e:
                    print("******Accept exception",e)

        sockid.settimeout(2)
        while True: 
            
            if self.__stopThread:
                print("breaking from listen thread")
                break 
            else:
                try:
                    msg = ""
                    if sock.getConnectionId():
                        conn = sock.getConnectionId()
                        msg = conn.recv(4096).decode('utf-8')
                    else:
                        msg = sockid.recv(4096).decode('utf-8')
                    if len(msg) == 0:
                        print("far end server shutdown")
                        sys.exit(0)
                    else:
                        #print("======msg:",msg)
                        msg_buffer.addToStringBuffer(msg)
                except socket.timeout as e:
                    err = e.args[0] 
                    if err == 'timed out':
                        #print("Recv Socket timeout, retry after 1sec")
                        # time.sleep(1)
                        continue
                    else:
                        print(e)
                        sys.exit(1)
                except socket.error as e:
                    print(e)
                    sys.exit(0)


                    
            
        
