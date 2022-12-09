import socket
import json


def tcpServerFile():
    server = ''
    addr = ''
    # sets up the options and address for the TCP socket
    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '0.0.0.0'
    port = 25575
    TCPsocket.bind((host,port))
    TCPsocket.listen(10)
    
    while True:
        server, addr = TCPsocket.accept()
        msg = server.recv(4096)
        print(f"Received a 'File Send' from '{addr[0]}, {addr[1]}'")

        # decode the 2 part message
        msgHeader = msg[:16].decode("utf-8").strip()
        msgType = msg[16:32].decode("utf-8").strip()
        content = msg[32:]

        print("length: ", len(msg))
        print("msg Header: ",msgHeader)
        # print("msg Content: ", content.decode("utf-8").strip())

        if msgHeader == "File Send":
            with open(f"./storage/output{msgType}", "wb") as OUTfp:
                OUTfp.write(content)
            server.close()
            break

    print("tcpServerFile closed")
    return