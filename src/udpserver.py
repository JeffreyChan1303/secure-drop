import socket
import json

'''
This is a background thread that runs and continuously picks broadcasts and thier respective ip adresses
'''
def udpserver(userEmail):
  nearbyUsers = {}
  ## AF_INET is family of protocols. SOCK_DGRAM is a type that for connectionless protocols
  UDPsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  host = ''
  port = 25555 #port number
  UDPsocket.bind((host,port)) # binds address:(hostname,port#) to socket 

  while True:
    data,addr = UDPsocket.recvfrom(1024) # this method receives UDP message , 1024 means the # of bytes to be read from the udp socket.
    msg, email = data.decode("utf-8").split(",")

    # if another user requests LIST, it will run this block of code
    if msg == "Looking for file transfer":
      if email not in nearbyUsers:
        print("Device Reply")
        UDPsocket.sendto(f"Looking for file transfer,{userEmail}".encode('utf-8'), addr)
      nearbyUsers[email] = {
        "ip": addr[0],
        "port": addr[1],
      }

      with open("./data/nearbyUsers.json", "w") as fp:
        json.dump(nearbyUsers, fp, indent=2)

    if data.decode() == "quit":
      break