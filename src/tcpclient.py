import socket
import json

# establish tcp connection with specific host and port number
def tcpClient(userEmail, targetIP, msgType):
    # sets up the options and address for the TCP socket
    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = targetIP
    port = 25565
    TCPsocket.connect((host,port))

    # if sending a "List Request", send the user's email
    if msgType == "List Reply":
        print(f"Sent a 'List Reply' to ({host}, {port})")
        TCPsocket.send(bytes(f"List Reply,{userEmail}", "utf-8"))

    # receive the "List Request #2"
    msg = TCPsocket.recv(1024)
    msg = msg.decode("utf-8").split(",")

    # check if the other user's email is in this user's contacts, if it is, then send a confirmation message
    if msg[0] == "List Request #2":
        print(f"Received a 'List Request #2' from {host} (ADD PORT)")
        with open("./data/contacts.json", "r") as Cfp:
            allContacts = json.load(Cfp)
            if msg[1] in allContacts:
                print(f"Sent a 'Both Contacts Verified' to ({host}, {port})")
                TCPsocket.send(bytes(f"Both Contacts Verified", "utf-8"))        
            else:
                print(f"Sent a 'Contact Not Verifeid' to ({host}, {port})")
                TCPsocket.send(bytes(f"Contact Not Verified", "utf-8"))
        TCPsocket.close()


