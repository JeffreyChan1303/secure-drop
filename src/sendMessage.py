import json
from src.tcpClientFIle import tcpClientFile


def sendMessage(userEmail):
    targetEmail = ''
    # return if there are no contacts available
    with open("./data/nearbyContacts.json", "r") as NCfp:
        nearbyContacts= json.load(NCfp)
        if len(nearbyContacts) == 0:
            return

        # find targetIP by passing in userName for the input
        while targetEmail not in nearbyContacts:
            inputName = input("\nEnter the name of the person you wish to send a file to: ").strip()
            for contact in nearbyContacts:
                contactName = nearbyContacts[contact]["fullName"]
                if contactName == inputName:
                    targetEmail = contact

            if targetEmail not in nearbyContacts:
                print("'" + inputName + "' is not online.\n")

        # start a tcp connection with the specified user
        targetIP = nearbyContacts[targetEmail]["ip"]
        tcpClientFile(userEmail, targetIP, inputName)