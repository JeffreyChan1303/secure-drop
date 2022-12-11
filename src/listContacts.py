import json
import socket
from time import sleep
from src.tcpServerList import tcpServerList

def listContacts(userEmail):
  UDPsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) ## AF_INET is family of protocols. SOCK_DGRAM is a type that for connectionless protocols
  port = 25555
  msg = "List Request".encode("utf-8")
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  UDPsocket.sendto(msg, ("255.255.255.255",port))
  print(f"Broadcasted a 'List Request' to (255.255.255.255, {port})")

  with open("./data/nearbyContacts.json", "w") as NCfp:
    nearbyContacts = {}
    json.dump(nearbyContacts, NCfp)

  print("Waiting 1 second for responses... ")
  sleep(1)

  # here print out the nearby users
  with open("./data/nearbyContacts.json", "r") as NCfp:
    with open("./data/contacts.json", "r") as Cfp:
      nearbyContacts= json.load(NCfp)
      contacts = json.load(Cfp)
      print("\nFull Name | Email | IP Address")
      if len(nearbyContacts) == 0:
        print("No Contacts Online.\n")
      for email in nearbyContacts:
        fullName = contacts[userEmail][email]['fullName']
        print(fullName, "|", email, "|", nearbyContacts[email]['ip'])
      
  return