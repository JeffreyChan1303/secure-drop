import socket
from os.path import exists
import ssl

def toBytes16(msg):
    if len(msg.encode('utf-8')) > 16:
        print("This is not possible!")
    else:
        str2 = '{0: <16}'.format(msg)    # adds needed space to the beginnig of str
        return str2.encode('utf-8')
    return ''

def toBytes32(msg):
    if len(msg.encode('utf-8')) > 32:
        print("This is not possible!")
    else:
        str2 = '{0: <16}'.format(msg)    # adds needed space to the beginnig of str
        return str2.encode('utf-8')
    return ''

# establish tcp connection with specific host and port number
def tcpClientFile(userEmail, targetIP):
    context=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context = ssl._create_unverified_context()
    context.load_verify_locations("./certs/pki/issued/samuelvilt.crt")
    # sets up the options and address for the TCP socket
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as TCPsocket:
        TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        host = targetIP
        port = 25575
        TCPsocket.connect((host,port))
        ssock = context.wrap_socket(TCPsocket, server_hostname = "localhost")

        directory = input("Enter the location of the file you wish to send: ")
        fileName = "." + directory.split(".")[-1]
        while not exists(directory):
            directory = input(f"Bad file path {directory} \nEnter the location of the file you wish to send: ")
            fileName = "." + directory.split(".")[-1]

        with open(directory, "rb") as DIRfp:
            fileContent = DIRfp.read()
        
        byteMsg = toBytes16("File Send")
        byteMsgName = toBytes32(fileName)

        ssock.send(b''.join([byteMsg, byteMsgName, fileContent]))

        print(f"Sent a 'File sent!' to ({host}, {port})")
        return