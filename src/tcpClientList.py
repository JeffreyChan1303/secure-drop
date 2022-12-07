import socket
import json
import ssl


# establish tcp connection with specific host and port number
def tcpClientList(userEmail, targetIP):

    context=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context = ssl._create_unverified_context()

    with open("./data/users.json", "r") as usersfp:
         user = json.load(usersfp)
         cert = user[userEmail]["certificate"]

    context.load_verify_locations("data\issued\\" + cert)


    # sets up the options and address for the TCP socket
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as TCPsocket:
        TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        host = targetIP
        port = 25565
        TCPsocket.connect((host,port))
        ssock = context.wrap_socket(TCPsocket, server_hostname = userEmail)

        print(f"Sent a 'List Reply' to ({host}, {port})")
        ssock.send(bytes(f"List Reply,{userEmail}", "utf-8"))

        # receive the "List Request #2"
        msg = ssock.recv(1024)
        msg = msg.decode("utf-8").split(",")

        # check if the other user's email is in this user's contacts, if it is, then send a confirmation message
        if msg[0] == "List Request #2":
            print(f"Received a 'List Request #2' from {host} (ADD PORT)")
            with open("./data/contacts.json", "r") as Cfp:
                allContacts = json.load(Cfp)
                if msg[1] in allContacts:
                    print(f"Sent a 'Both Contacts Verified' to ({host}, {port})")
                    ssock.send(bytes("Both Contacts Verified", "utf-8"))  
                    ssock.close()
                else:
                    print(f"Sent a 'Contact Not Verifeid' to ({host}, {port})")
                    ssock.send(bytes("Contact Not Verified", "utf-8"))
                    ssock.close()