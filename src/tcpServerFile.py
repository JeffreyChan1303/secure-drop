import socket
import json
import ssl

def tcpServerFile():
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
            print(f"Received a 'File Send' from '{addr[0]}, {addr[1]}'")

            # decode the 2 part message
            msgHeader = msg[:16].decode("utf-8").strip()
            msgFile = msg[16:48].decode("utf-8").strip()
            content = msg[48:]

            print("length: ", len(msg))
            print("msg Header: ",msgHeader)
            # print("msg Content: ", content.decode("utf-8").strip())

            if msgHeader == "File Send":
                with open(f"./storage/{msgFile}", "wb") as OUTfp:
                    OUTfp.write(content)
                server.close()