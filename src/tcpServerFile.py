import socket
import json
import ssl
import time


def tcpServerFile(userEmail):
    # Using the certificate Authority to check the certificate of user
    context=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("./certs/pki/issued/ca.crt","./certs/pki/private/ca.key", 'secure-dropSJJ')

    # sets up the options and address for the TCP socket
    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '0.0.0.0'
    port = 25575 # tcp file port number
    TCPsocket.bind((host,port))
    TCPsocket.listen(10)
    
    # Protecting the connection with the Certificate
    with context.wrap_socket(TCPsocket,server_side=True) as ssock:
        while True:
            # accept the file send
            server, addr = ssock.accept()
            msg = server.recv(4096)

            # decode the message
            msgHeader = msg[:16].decode("utf-8").strip()
            msgFile = msg[16:48].decode("utf-8").strip()
            msgEmail = msg[48: 80].decode("utf-8").strip()
            timestamp = float(msg[80: 112].decode("utf-8").strip())
            content = msg[112:]

            # get the time that the message was received
            timeElapsed = time.time() - timestamp
            print(timeElapsed)

            # check if the message was sent within a reasonable time
            if timeElapsed > 5:
                print('Possible Replay Attack!')
                server.close()
                return

            if msgHeader == "File Send":
                # get the full name of the user sending the file
                with open("./data/contacts.json", "r") as Cfp:
                    contacts = json.load(Cfp)
                    msgFullName = contacts[userEmail][msgEmail]["fullName"]

                # prompt the user to accept or deny the incoming file
                print(f"Contact '{msgFullName} <{msgEmail}>' is sending a file '{msgFile}'. Accept (y/n)?")
                recInput = input()
                while recInput.lower() != 'y' and recInput.lower() != 'n':
                    print(f"Invalid input. \nContact '{msgFullName} <{msgEmail}>' is sending a file '{msgFile}'. Accept (y/n)?")
                    recInput = input()
                
                if recInput.lower() == 'y':
                    with open(f"./storage/{msgFile}", "wb") as OUTfp:
                        OUTfp.write(content)
                    server.send(b"File Accepted")
                    print(f"File '{msgFile}' has been ACCEPTED")
                else:
                    server.send(b"File Denied")
                    print(f"File '{msgFile}' has been DENIED")

                server.close()