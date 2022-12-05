import json

from src.tcpClientFIle import tcpClientFile
# PGP, Generate private and public RSA key when creating an acount
# Generate AES Key when generating message with noince, and tag.

# How do we use TLS along with Certificate Authorities for this
def sendMessage(userEmail):
    # 1. go to nearbyUsers and tell user to choose a user
    # 2. send a UDP message telling other device to open a TCP Server, 
    #    and reply with a UDP response with the address, and port number
    # 4. establish the TCP client as this device
    # 5. Encrypt and send the file
    #       use PGP (pretty good privacy) for the file encryption
    # 6. Close the connection

    with open("./data/nearbyContacts.json", "r") as NCfp:
        nearbyContacts= json.load(NCfp)
        if len(nearbyContacts) is not 0:
            targetEmail = input("type email to send file to: ").strip()
        else:
            return

    while targetEmail not in nearbyContacts:
        print("'"+targetEmail+"' is not online. Please enter a valid email: ")
        targetEmail = input("type email to send file to: ").strip()

    targetIP = nearbyContacts[targetEmail]["ip"]
    tcpClientFile(userEmail, targetIP)

    return