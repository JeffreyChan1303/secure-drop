import socket
import json

'''
This is a background thread that runs and continuously picks broadcasts and thier respective ip adresses
'''
def udpserver(userEmail, stopThreads):
  nearbyUsers = {}
  ## AF_INET is family of protocols. SOCK_DGRAM is a type that for connectionless protocols
  UDPsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  host = ''
  port = 25555 #port number
  UDPsocket.bind((host,port)) # binds address:(hostname,port#) to socket 

  while True:
    if not stopThreads:
      print("running")
      data,addr = UDPsocket.recvfrom(1024) # this method receives UDP message , 1024 means the # of bytes to be read from the udp socket.
      msg = data.decode("utf-8").split(",")
      print(msg)

      # if another user sends "List Request", it will send "List Reply"
      if msg[0] == "List Request":
        print(f"Received a 'List Request' from {addr}")
        UDPsocket.sendto(f"List Reply,{userEmail}".encode('utf-8'), (addr[0], 25555))

      # if another user sends "List Request" and receives "List Reply", it will run this block of code
      if msg[0] == "List Reply":
        print("Received a 'List Reply'")
        with open("./data/contacts.json", "r") as Cfp:
          allContacts = json.load(Cfp)
          if userEmail in allContacts:
            userContacts = allContacts[userEmail]
          else:
            userContacts = {}
          if msg[1] in userContacts:
            nearbyUsers[msg[1]] = {
            "ip": addr[0],
            "port": addr[1],
            } 

        with open("./data/nearbyUsers.json", "w") as fp:
          json.dump(nearbyUsers, fp, indent=2)

      if data.decode() == "quit":
        break

    else:
      print("Stopped threads.\n")
      break