import socket
from src.tcpClientList import tcpClientList


def udpServer(userEmail):
  # sets up the options and address for the UDP socket
  UDPsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  host = ''
  port = 25555 # UDP port number
  userHostName = socket.gethostname()
  userIP = socket.gethostbyname(userHostName)
  UDPsocket.bind((host,port))

  # listening for "List Request"
  while True:
    data,addr = UDPsocket.recvfrom(1024)
    msg = data.decode("utf-8").split(",")

    # if another user sends "List Request", it will send "List Reply"
    if msg[0] == "List Request" and not(str(addr[0]) == str(userIP)):
      # start tcp client and transfer email
      tcpClientList(userEmail, addr[0])