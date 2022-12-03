import json
import socket
from src.tcpclient import tcpClient
# PGP, Generate private and public RSA key when creating an acount
# Generate AES Key when generating message with noince, and tag.

# How do we use TLS along with Certificate Authorities for this
def sendMessage():
    # 1. go to nearbyUsers and tell user to choose a user
    # 2. send a UDP message telling other device to open a TCP Server, 
    #    and reply with a UDP response with the address, and port number
    # 4. establish the TCP client as this device
    # 5. Encrypt and send the file
    #       use PGP (pretty good privacy) for the file encryption
    # 6. Close the connection

    with open("./data/nearbyContacts.json", "r") as fp:
        nearbyContacts= json.load(fp)
    targetEmail = input("type email to send file to. ").strip()

    if targetEmail not in nearbyContacts:
        print("Not a valid email")
        return

    targetIP = nearbyContacts[targetEmail]["ip"]

    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = targetIP
    port = 25575
    TCPsocket.connect((host,port))

    # send file
    TCPsocket.send("File sent!", "utf-8")