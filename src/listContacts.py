import json
import socket
from time import sleep


def listContacts(userEmail):
  # creates a udp broadcast
  UDPsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  port = 25555
  msg = "List Request".encode("utf-8")
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  UDPsocket.sendto(msg, ("255.255.255.255",port))

  # empty out the nearby contacts from the previous list command
  with open("./data/nearbyContacts.json", "w") as NCfp:
    nearbyContacts = {}
    json.dump(nearbyContacts, NCfp)

  print("\nWaiting 1 second for responses... ")
  sleep(1)

  # print out the nearby users that were receieved
  with open("./data/nearbyContacts.json", "r") as NCfp:
    with open("./data/contacts.json", "r") as Cfp:
      nearbyContacts= json.load(NCfp)
      contacts = json.load(Cfp)
      print("\nFull Name | Email")
      if len(nearbyContacts) == 0:
        print("   No Contacts Online.\n")
      for email in nearbyContacts:
        fullName = contacts[userEmail][email]['fullName']
        print("   " + fullName, "|", email)
      
  return