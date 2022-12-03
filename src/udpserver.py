import socket
import json
from src.tcpclient import tcpClient

'''
This is a background thread that runs and continuously picks broadcasts and thier respective ip adresses
'''

def udpserver(userEmail):
  # resets nearby users on successful login
  nearbyUsers = {}

  # sets up the options and address for the UDP socket
  UDPsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  host = ''
  port = 25555 # UDP port number
  userHostName = socket.gethostname()
  userIP = socket.gethostbyname(userHostName)
  UDPsocket.bind((host,port)) # binds address:(hostname,port#) to socket 

  # listening for "List Request"
  while True:
    print("UDP server listening at ", UDPsocket.getsockname())
    data,addr = UDPsocket.recvfrom(1024) # this method receives UDP message , 1024 means the # of bytes to be read from the udp socket.
    msg = data.decode("utf-8").split(",")

    # if another user sends "List Request", it will send "List Reply"
    if msg[0] == "List Request" and addr[0] is not userIP:
      print(f"Received a 'List Request' from {addr}")

      # start tcp client and transfer email
      tcpClient(userEmail, addr[0], "List Reply")