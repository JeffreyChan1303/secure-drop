import json
import socket

def listContacts(userEmail):

  UDPsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) ## AF_INET is family of protocols. SOCK_DGRAM is a type that for connectionless protocols
  port = 25565
  msg = b"(Broadcast message): Please respond if you are online."
  UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  UDPsocket.sendto(msg, ("255.255.255.255",port))

  # with open("./data/contacts.json", "r") as fp:
  #   allContacts = json.load(fp)
  #   userContacts = allContacts[userEmail]
  #   print("\nFull Name | Email\n")
  #   for contact in userContacts.values():
  #     print(contact["fullName"], "|", contact["email"])