# -*- coding: utf-8 -*-
import socket
import sys

# open tcp server on a specific host, and port number.
def tcpServer(host, port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    print("TCP SERVER host and port", host, port)
    s.bind((host,port)) # binds address:(hostname,port#) to socket 
    s.listen(5)
    while True:
        print("Listening at ", s.getsockname())
        server,addr = s.accept()
        print("Accept connection from: ",addr)
        print("Connection built from ", server.getsockname(), " and ", server.getpeername())
        message= server.recv(1024)
        print("The incoming message is : ", message.decode("utf-8"))
        server.send(bytes("Thanks for connecting","utf-8"))
        server.close()
        print("server replied, socket closed")

# establish tcp connection with specific host, and port number
def tcpClient(host, port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.connect((host,port))
    print("client has been assigned socket name: ", s.getsockname())
    message="THIS IS A TCP Connection"
    s.send(bytes(message,"utf-8"))
    message= s.recv(1024)
    print("The server replied: ",message.decode("utf-8"))
    s.close()