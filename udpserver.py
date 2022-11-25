import socket
import sys

def udpserver():
  ## AF_INET is family of protocols. SOCK_DGRAM is a type that for connectionless protocols
  UDPsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  host = '0.0.0.0'
  port = 25565 #port number
  UDPsocket.bind((host,port)) # binds address:(hostname,port#) to socket 

  while True:
    print("ready to receive message")
    data,addr = UDPsocket.recvfrom(1024) # this method receives UDP message , 1024 means the # of bytes to be read from the udp socket.
    print("message received")
    UDPsocket.sendto(b"I am online", addr)
    if data.decode() == "quit":
      break
    print("'" + data.decode("utf-8") + "'", " is from ", addr)