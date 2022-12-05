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

    directory = input("Enter the location of the file you wish to send: ")
    plainText = ''

    with open(directory, "rb") as DIRfp:
        plainText = DIRfp.read()
    
    TCPsocket.send(bytes("File Send", "utf-8"))
    TCPsocket.send(bytes(plainText))

    print(f"Sent a 'File sent!' to ({host}, {port})")
    return