import json
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

    with open("./data/nearbyUsers.json", "r") as fp:
        nearbyUsers= json.load(fp)
        print("\n Email | IP Address | Port \n")
        for email in nearbyUsers:
            print(email, "|", nearbyUsers[email]['ip'],"|", nearbyUsers[email]['port'])

        targetEmail = input("type email to send file to. ").strip()

        if targetEmail not in nearbyUsers:
            print("Not a valid email")
        else:
            targetIp = nearbyUsers[targetEmail]["ip"]
            # SEND TCP MESSAGE
            
        