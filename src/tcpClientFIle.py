import socket
import json

def toBytes16(msg):
    if len(msg.encode('utf-8')) > 16:
        print("This is not possible!")
    else:
        str2 = '{0: <16}'.format(msg)    # adds needed space to the beginnig of str
        return str2.encode('utf-8')
    return ''

# establish tcp connection with specific host and port number
def tcpClientFile(userEmail, targetIP):
    # sets up the options and address for the TCP socket
    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = targetIP
    port = 25575
    TCPsocket.connect((host,port))

    directory = input("Enter the location of the file you wish to send: ")
    fileType = "." + directory.split(".")[-1]

    with open(directory, "rb") as DIRfp:
        fileContent = DIRfp.read()
    
    byteMsg = toBytes16("File Send")
    byteMsgType = toBytes16(fileType)

    TCPsocket.send(b''.join([byteMsg, byteMsgType, fileContent]))

    print(f"Sent a 'File sent!' to ({host}, {port})")
    return