import json
import socket
import aioice


def start_server_ice_session():
    localIP = "127.0.0.1"
    localPort = 20001
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip

    UDPServerSocket.bind((localIP, localPort))

    print("UDP server up and listening")

    bytesAddressPair = UDPServerSocket.recvfrom(2048)

    message = bytesAddressPair[0].decode()
    address = bytesAddressPair[1]
    print(message)

    sendMessage = json.dumps(
            {
                "candidates": ["e2642c5546f8bd6b772346bab8b1130b 1 udp 2130706431 10.0.75.1 52388 typ host"],
                "password": "F9SlfxeSAzSwjs1eL5fwkT",
                "username": "uoK9",
            }
        )

    UDPServerSocket.sendto(sendMessage.encode('utf-8'),address)


if __name__ == '__main__':
    start_server_ice_session()
