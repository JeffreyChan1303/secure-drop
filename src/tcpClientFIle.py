import socket
from os.path import exists
import ssl
import time
import json

# convert string to 16 byteString
def toBytes16(msg):
    if len(msg.encode('utf-8')) > 16:
        print("This is not possible!")
    else:
        str2 = '{0: <16}'.format(msg) 
        return str2.encode('utf-8')
    return ''

# convert string to 32 byteString
def toBytes32(msg):
    if len(msg.encode('utf-8')) > 32:
        print("This is not possible!")
    else:
        str2 = '{0: <32}'.format(msg) 
        return str2.encode('utf-8')
    return ''

# establish tcp connection with specific host and port number
def tcpClientFile(userEmail, targetIP, targetName):

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
        port = 25575
        TCPsocket.connect((host,port))
        ssock = context.wrap_socket(TCPsocket, server_hostname = "localhost")

        # select the file to send
        directory = input("Enter the name of the file you wish to send in the storage folder: ")
        fileName = directory.split("/")[-1]
        while not exists("./storage/" + directory):
            directory = input(f"Bad file path {directory} \nEnter the location of the file you wish to send: ")
            fileName = directory.split("/")[-1]

        with open("./storage/" + directory, "rb") as DIRfp:
            fileContent = DIRfp.read()
        
        byteMsg = toBytes16("File Send")
        byteMsgName = toBytes32(fileName)
        userEmail = toBytes32(userEmail)
        byteTime = toBytes32(time.time())

        ssock.send(b''.join([byteMsg, byteMsgName, userEmail, byteTime, fileContent]))

        msg = ssock.recv(1024)

        if msg == "File Denied":
            print(f"Your file '{directory}' was DENIED by '{targetName}'.")
        
        if msg == "File Accepted":
            print(f"Your file '{directory}' was ACCEPTED by '{targetName}'.")

        print(f"Sent a 'File sent!' to ({host}, {port})")
        return