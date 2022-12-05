import socket
import json


# establish tcp connection with specific host and port number
def tcpClientFile(userEmail, targetIP):
    # sets up the options and address for the TCP socket
    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = targetIP
    port = 25575
    TCPsocket.connect((host,port))

    TCPsocket.send(bytes("File sent!", "utf-8"))
    print(f"Sent a 'File sent!' to ({host}, {port})")
    return