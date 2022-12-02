import json
import socket
from time import sleep

def listContacts(userEmail):
  UDPsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) ## AF_INET is family of protocols. SOCK_DGRAM is a type that for connectionless protocols
  port = 25555
  msg = "List Request".encode("utf-8")
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  UDPsocket.sendto(msg, ("255.255.255.255",port))

  # Start tcp server
  
  
  print("Waiting 3 seconds for responses... ")
  sleep(3)

  # here print out the nearby users
  with open("./data/nearbyUsers.json", "r") as fp:
    nearbyUsers= json.load(fp)
    print("\n Email | IP Address | Port")
    if len(nearbyUsers) == 0:
      print("No Contacts Online.\n")
    for email in nearbyUsers:
      print(email, "|", nearbyUsers[email]['ip'],"|", nearbyUsers[email]['port'])


  return