from messagebuffer import MessageBuffer
import socket, time, sys
from threading import Thread

from transport import SignalingSocket

class ListenThread:
    def __init__(self):
        self.__stopThread = False
    
    def setStopThread(self, st):
        self.__stopThread = st
    '''
    def acceptClientAndReceiveMessage(self, sock:SignalingSocket, msg_buffer:MessageBuffer):        
        local_address = sock.getLocalAddress()
        server_sockid = sock.getServerSockId()
        server_sockid.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sockid.bind(local_address)
        server_sockid.listen(5)
        connId = None
        while True:
            
            print("***waiting for client connection***")
            try:
                connId, addr = server_sockid.accept()
                print("***client accetped from ", addr)
                sock.setConnectionId(connId)
                break
            except Exception as e:         
                print("****connection request Exception:", e)

        while True:
            if self.__stopThread:
                break 
            msg = ""
            msg = connId.recv(4096).decode('utf-8')
            print("***message Received on Server Socket")
            msg_buffer.addToStringBuffer(msg)

               
    def startListening(self, sock:SignalingSocket, msg_buffer:MessageBuffer, isServer=False):
        print("****In Start Listening isServer", isServer)
        client_sockid = sock.getClientSockId() 
                 
        while True:             
            if self.__stopThread:
                break 
            else:
                try:
                   msg = client_sockid.recv(4096).decode('utf-8')
                   print("***message Received on Client Socket")
                   if len(msg) == 0:
                       print("far end server shutdown")
                       sys.exit(0)
                   else:
                       # print("======msg:",msg)
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
                else:
                    if len(msg) == 0:
                        print("far end server shutdown")
                        sys.exit(0)
                    else:
                        #print("======msg:",msg)
                        msg_buffer.addToStringBuffer(msg)     
                    
    '''
def startListening(sock:SignalingSocket, queue, sockclose_triger_queue):
    print("****In Start Listening isServer")
    #client_sockid = sock.getClientSockId()

    while True:
        if sock.isStopRecv():
            return
        if sock.isRemoteConnReset():
            continue
        client_sockid = sock.getClientSockId()
        if client_sockid:
            client_sockid.settimeout(2)
        try:
            msg = ""
            if client_sockid:
                msg = client_sockid.recv(4096).decode('utf-8')
                print("***received Message on Client Socket")
                if len(msg) == 0:
                    print("far end server shutdown, add trigger to queue")
                    client_sockid.close()
                    sockclose_triger_queue.put("true")
                    sock.setRemoteConnReset()
                else:
                    #print("======msg:",msg)
                    queue.put(msg)
        except socket.timeout:
            continue
        except socket.error as e:
            print("Exception in receiving from client socket",e)
            continue

            
def acceptClient(sock:SignalingSocket, queue):
    local_address = sock.getLocalAddress()
    server_sockid = sock.getServerSockId()
    server_sockid.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sockid.bind(local_address)
    server_sockid.settimeout(2)
    print("***listening to client request")
    server_sockid.listen(10)
    serv_threads = []
    try:
        while True:
            if sock.isStopRecv():
                break
            #print("***waiting for client connection***")
            try:
                connId, addr = server_sockid.accept()
                print("***Client accepted from address", connId)
                sock.setConnectionId(connId)
                th = Thread(target=recvMsgOnSeverConnection, args=(sock, connId, queue))
                th.start()
                serv_threads.append(th)
            except socket.timeout:
                continue
            except Exception as e:
                print("****connection request Exception:", e)
                continue
    finally:
        for th in serv_threads:
            th.join()
        print("****All Server Listening Threads joined")


def recvMsgOnSeverConnection(sock:SignalingSocket, connId, queue):
    connId.settimeout(2)
    try:
        while True:
            if sock.isStopRecv():
                break
            # if sock.isRemoteConnReset():
            #     print(
            #         "***waiting to receive on server connection, while remote conn is closed - break to start listening for new connection request")
            #     sock.setRemoteConnReset(False)
            #     break
            try:
                msg = ""
                msg = connId.recv(4096).decode('utf-8')
                # print("***received message on server Socket")
                queue.put(msg)
            except socket.timeout:
                continue
            except Exception as e:
                print("*****server connection receive error as", e)
                break
    finally:
        connId.close()


