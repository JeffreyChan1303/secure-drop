import socket
import json


# open tcp server on a specific host, and port number.
def tcpServerList(userEmail):
    print("TCP STARTED")
    emailReply = ""

    # sets up the options and address for the TCP socket
    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '0.0.0.0'
    port = 25565
    TCPsocket.bind((host,port))
    TCPsocket.listen(10)
    TCPsocket.settimeout(3)

    try: 
        server,addr = TCPsocket.accept()
    except TimeoutError:
        return
   
    # listening for "List Reply" or "Both contacts verified"
    while True:
        print("TCP server listening at ", TCPsocket.getsockname())
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
                    print(f"Sent a 'Contact Not Verified' to ({addr[0]}, {port})")
                    server.send(bytes(f"Contact Not Verified", "utf-8"))
                    server.close()
                    break

        # if the message is "Both contacts verified"
        if msg[0] == "Both Contacts Verified":
            print("Received a 'Both Contacts Verified'...Closing TCP server")
            with open("./data/nearbyContacts.json", "w") as NCfp:
                nearbyContacts = {}
                nearbyContacts[emailReply] = {
                    "ip": addr[0]
                }
                json.dump(nearbyContacts, NCfp)
            server.close()
            break
          
        # if the message is "Contact not verified"
        if msg[0] == "Contact Not Verified":
            print("Received a 'Contact Not Verified'...Closing TCP server")
            server.close()
            break

    print("tcpServerList closed")
    return

