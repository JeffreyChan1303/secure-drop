import socket
import json
import ssl

# open tcp server on a specific host, and port number.
def tcpServerList(userEmail):
    emailReply = ""
    context=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("./certs/pki/issued/ca.crt","./certs/pki/private/ca.key", 'secure-dropSJJ')

    # sets up the options and address for the TCP socket
    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '0.0.0.0'
    port = 25565
    TCPsocket.bind((host,port))
    TCPsocket.listen(10)
    TCPsocket.settimeout(1)

    # listening for "List Reply" or "Both contacts verified"
    with context.wrap_socket(TCPsocket,server_side=True) as ssock:
        while True:
            try:
                server, addr = ssock.accept()
            except TimeoutError:
                return
            msg = server.recv(1024)
            msg = msg.decode("utf-8").split(",")

            # if the message is "List Reply"
            if msg[0] == "List Reply":
                emailReply = msg[1]
                with open("./data/contacts.json", "r") as Cfp:
                    allContacts = json.load(Cfp)
                    if userEmail in allContacts and emailReply in allContacts[userEmail]:
                        server.send(bytes(f"List Request #2,{userEmail}", "utf-8"))
                    else:
                        server.send(bytes(f"Contact Not Verified", "utf-8"))
            
            msg = server.recv(1024)
            msg = msg.decode("utf-8")

            # if the message is "Both contacts verified"
            if msg == "Both Contacts Verified":
                with open("./data/nearbyContacts.json", "r") as NCfpR:
                    nearbyContacts = json.load(NCfpR)
                    with open("./data/nearbyContacts.json", "w") as NCfpW:
                        with open("./data/contacts.json", "r") as Cfp:
                            contacts = json.load(Cfp)
                            nearbyContacts[emailReply] = {
                                "fullName": contacts[userEmail][emailReply]["fullName"],
                                "ip": addr[0]
                            }
                            json.dump(nearbyContacts, NCfpW, indent=2)