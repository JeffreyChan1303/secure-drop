import socket
from src.tcpClientList import tcpClientList

'''
This is a background thread that runs and continuously picks broadcasts and thier respective ip adresses
'''

def udpServer(userEmail, stop_threads):
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

  print("userIP is " + userIP)

  # listening for "List Request"
  while True:
    print("UDP server listening at ", UDPsocket.getsockname())
    data,addr = UDPsocket.recvfrom(1024)
    msg = data.decode("utf-8").split(",")

    print("----- Incoming IP: " + addr[0] + " | Server IP: " + userIP + " -----")
    # if another user sends "List Request", it will send "List Reply"
    if msg[0] == "List Request" and not(str(addr[0]) == str(userIP) or str(addr[0]) == "127.0.0.1"):
      print(f"Received a 'List Request' from ({addr[0]}, {addr[1]})")
      # start tcp client and transfer email
      tcpClientList(userEmail, addr[0])
    else:
      print("----- Received a broadcast from myself -----")

    if stop_threads == False:
      break