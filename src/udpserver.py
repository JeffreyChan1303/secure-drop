import socket
import threading
from src.tcp import tcpClient, tcpServer

def udpserver():
  ## AF_INET is family of protocols. SOCK_DGRAM is a type that for connectionless protocols
  UDPsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  host = ''
  port = 25565 #port number
  UDPsocket.bind((host,port)) # binds address:(hostname,port#) to socket 

  while True:
    print("ready to receive message")
    data,addr = UDPsocket.recvfrom(1024) # this method receives UDP message , 1024 means the # of bytes to be read from the udp socket.
    # check if use is looking to transfer to you
    print(data.decode("utf-8"))
    if data.decode("utf-8") == "Looking for file transfer":
      tcpAddress = ('', 5001)
      # open TCP connection
      tcpServerThread = threading.Thread(target=tcpServer, args=tcpAddress)
      tcpServerThread.start()
      # send UDP response saying where the tcp connection is located, address and port.
      msg = b'TCP Destination,0.0.0.0,5001'
      UDPsocket.sendto(msg, addr)


    print("message received")
    

    UDPsocket.sendto(b"I am online", addr)
    if data.decode() == "quit":
      break
    print("'" + data.decode("utf-8") + "'", " is from ", addr)