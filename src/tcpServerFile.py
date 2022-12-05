import socket

def tcpServerFile(stop_threads):
    # sets up the options and address for the TCP socket
    TCPsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    TCPsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '0.0.0.0'
    port = 25575
    TCPsocket.bind((host,port))
    TCPsocket.listen(10)
    TCPsocket.settimeout(3)

    try: 
        server,addr = TCPsocket.accept()
    except TimeoutError:
        print("---TIMEOUT ERROR--- tcpServerFile()")
        return

    server,addr = TCPsocket.accept()

    while True:
        msg = server.recv(1024)

        if stop_threads == False:
            break

        if msg == "File sent!":
            print("Received file")
            server.close()
            break

    print("tcpServerFile closed")
    return