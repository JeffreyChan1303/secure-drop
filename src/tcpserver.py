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
        msg = server.recv(1024)
        msg = msg.decode("utf-8").split(",")

        # if the message is "List Reply"
        if msg[0] == "List Reply":
            print(f"Received a 'List Reply' from ({addr[0]}, {addr[1]})")
            emailReply = msg[1]
            with open("./data/contacts.json", "r") as Cfp:
                allContacts = json.load(Cfp)
                if emailReply in allContacts:
                    print(f"Sent a 'List Request #2' to ({addr[0]}, {port})")
                    server.send(bytes(f"List Request #2,{userEmail}", "utf-8"))
                else:
                    print(f"Sent a 'Contact Not Verifeid' to ({addr[0]}, {port})")
                    server.send(bytes(f"Contact Not Verified", "utf-8"))
                    server.close()
                    break

        # if the message is "Both contacts verified"
        if msg[0] == "Both Contacts Verified":
            print("Received a Both Contacts verified...Closing TCP server")
            with open("./data/nearbyContacts.json", "r+") as NCfp:
                nearbyContacts = json.load(NCfp)
                nearbyContacts[emailReply] = {
                    "ip": addr[0]
                }
            server.close()
            break
          
        # if the message is "Contact not verified"
        if msg[0] == "Contact Not Verified":
            print("Received a Contact not verified...Closing TCP server")
            server.close()
            break

        
      