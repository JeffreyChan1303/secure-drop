import json
from src.tcpClientFIle import tcpClientFile

def sendMessage(userEmail):
    targetEmail = ''
    
    with open("./data/nearbyContacts.json", "r") as NCfp:
        nearbyContacts= json.load(NCfp)
        if len(nearbyContacts) is 0:
            return

        # find targetIP by passing in userName for the input
        while targetEmail not in nearbyContacts:
            inputName = input("Type a name to send file to them: ").strip()
            for contact in nearbyContacts:
                contactName = nearbyContacts[contact]["fullName"]
                if contactName == inputName:
                    targetEmail = contact

            if targetEmail not in nearbyContacts:
                print("'" + inputName + "' is not online.\n")

        targetIP = nearbyContacts[targetEmail]["ip"]
        print(targetIP)
        tcpClientFile(userEmail, targetIP, inputName)