import socket
import json


def tcpServerFile(stop_threads):
    # sets up the options and address for the TCP socket
    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '0.0.0.0'
    port = 25575
    TCPsocket.bind((host,port))
    TCPsocket.listen(10)
    server,addr = TCPsocket.accept()

    while True:
        msg = server.recv(1024)
        print(f"Received a 'File Send' from '{addr[0]}, {addr[1]}'")

        # decode the 2 part message
        msgHeader = msg[:16].decode("utf-8").strip()
        content = msg[16:]

        if stop_threads == True:
            server.close()
            break

        if msgHeader == "File Send":
            with open("./storage/output.txt", "wb") as OUTfp:
                OUTfp.write(content)
            server.close()
            break

    print("tcpServerFile closed")
    return