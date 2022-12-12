import socket
import json
import ssl


# establish tcp connection with specific host and port number
def tcpClientList(userEmail, targetIP):
    with open("./data/users.json", "r") as Cfp:
        data = json.load(Cfp)
        userCert = data[userEmail]["fullName"]
        userCert = userCert.lower()
        userCert = userCert.replace(" ", "")

    location = "./certs/pki/issued/" + userCert + ".crt"

    context=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context = ssl._create_unverified_context()
    context.load_verify_locations(location)
    # sets up the options and address for the TCP socket
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as TCPsocket:
        TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        host = targetIP
        port = 25565
        TCPsocket.connect((host,port))
        ssock = context.wrap_socket(TCPsocket, server_hostname = "localhost")

        ssock.send(bytes(f"List Reply,{userEmail}", "utf-8"))

        # receive the "List Request #2"
        msg = ssock.recv(1024)
        msg = msg.decode("utf-8").split(",")

        # check if the other user's email is in this user's contacts, if it is, then send a confirmation message
        if msg[0] == "List Request #2":
            with open("./data/contacts.json", "r") as Cfp:
                allContacts = json.load(Cfp)
                if userEmail in allContacts and msg[1] in allContacts[userEmail]:
                    print(f"Sent a 'Both Contacts Verified' to ({host}, {port})")
                    ssock.send(bytes("Both Contacts Verified", "utf-8"))  
                    ssock.close()
                else:
                    print(f"Sent a 'Contact Not Verifeid' to ({host}, {port})")
                    ssock.send(bytes("Contact Not Verified", "utf-8"))
                    ssock.close()