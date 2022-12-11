import socket
import json
import ssl
import time
def tcpServerFile(userEmail):
    context=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("./certs/pki/issued/ca.crt","./certs/pki/private/ca.key", 'secure-dropSJJ')
    server = ''
    addr = ''
    # sets up the options and address for the TCP socket
    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '0.0.0.0'
    port = 25575
    TCPsocket.bind((host,port))
    TCPsocket.listen(10)
    
    with context.wrap_socket(TCPsocket,server_side=True) as ssock:
        while True:
            server, addr = ssock.accept()
            msg = server.recv(4096)

            # decode the 2 part message
            msgHeader = msg[:16].decode("utf-8").strip()
            msgFile = msg[16:48].decode("utf-8").strip()
            msgEmail = msg[48: 80].decode("utf-8").strip()
            timestamp = msg[80: 112].decode("utf-8").strip()
            content = msg[112:]

<<<<<<< HEAD
            print("length: ", len(msg))
            print("msg Header: ",msgHeader)
            print("msg Email: ", msgEmail)
            print("timestamp:", timestamp)

            curtime = time.time()

            if timestamp > curtime + 2 and timestamp < curtime - 2:
                print('Possible Replay Attack!')
                server.close()


=======
>>>>>>> bd4eced3e7bb4a7529c2e219888c24c282ed5036
            if msgHeader == "File Send":
                with open("./data/contacts.json", "r") as Cfp:
                    contacts = json.load(Cfp)
                    msgFullName = contacts[userEmail][msgEmail]["fullName"]

                # promp message for accepting file
                recInput = input(f"Contact '{msgFullName} <{msgEmail}>' is sending a file '{msgFile}'. Accept (y/n)?")
                while recInput.lower() != 'y' or recInput.lower() != 'n':
                    recInput = input(f"Invalid input. \nContact '{msgFullName} <{msgEmail}>' is sending a file '{msgFile}'. Accept (y/n)?")

                if recInput.lower() == 'y':
                    with open(f"./storage/{msgFile}", "wb") as OUTfp:
                        OUTfp.write(content)
                    server.send(b"File Accepted", (addr[0], port))
                else:
                    server.send(b"File Denied", (addr[0], port))

                server.close()