import socket
import json
import sys

# open tcp server on a specific host, and port number.
def tcpServer(userEmail):
    emailReply = ""

    # sets up the options and address for the TCP socket
    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '0.0.0.0'
    port = 25565
    TCPsocket.bind((host,port))
    TCPsocket.listen(5)

    # listening for "List Reply" or "Both contacts verified"
    while True:
        print("TCP server listening at ", TCPsocket.getsockname())
        server,addr = TCPsocket.accept()
        print("Accept connection from: ",addr)
        print("Connection built from ", server.getsockname(), " and ", server.getpeername())
        msg = server.recv(1024)
        print("The incoming message is : ", msg.decode("utf-8"))

        msg = msg.decode("utf-8").split(",")

        # if the message is "List Reply"
        if msg[0] == "List Reply":
            emailReply = msg[1]
            with open("./data/contacts.json", "r") as Cfp:
                allContacts = json.load(Cfp)
                if emailReply in allContacts:
                    server.send(bytes(f"List Request #2,{userEmail}", "utf-8"))
                else:
                    server.send(bytes(f"Contact not verified", "utf-8"))
                    server.close()

        # if the message is "Both contacts verified"
        if msg[0] == "Both contacts verified":
            with open("./data/nearbyUsers.json", "r+") as NUfp:
                nearbyUsers = json.load(NUfp)
                nearbyUsers[emailReply] = {
                    "ip": addr[0]
                }
        server.close()
          
        # if the message is "Contact not verified"
        if msg[0] == "Contact not verified":
            print("server replied, socket closed")

        
      