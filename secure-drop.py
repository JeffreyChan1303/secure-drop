import src
import threading


def main():
  stop_threads = False
  # login to application, stores the userEmail for future use
  # userEmail = src.userLogin()
  userEmail = "jeff@gmail.com"
  
  serverThreadUDP = threading.Thread(target=src.udpServer, args=(userEmail, stop_threads))
  serverThreadTCPList = threading.Thread(target=src.tcpServerList, args=(userEmail,))
  serverThreadTCPSend = threading.Thread(target=src.tcpServerSend, args=(stop_threads))
  serverThreadUDP.start()
  serverThreadTCPSend.start()

  print("\n\nWelcome to Secure Drop.")
  print("Type 'help' for commands.\n")

  # Shell loop
  while True:
    command = input("secure_drop> ")

    if command == "help":
      print("  'add' -> Add a new contact")
      print("  'list' -> List all online contacts")
      print("  'send' -> Transfer file to contact")
      print("  'exit' -> Exit SecureDrop\n")
    elif command == "add":
      src.addContact(userEmail)

    elif command == "list":
      serverThreadTCPList.start()
      src.listContacts(userEmail)
      serverThreadTCPList.join()
      serverThreadTCPList = threading.Thread(target=src.tcpServer, args=(userEmail,))

    elif command == "send":
      serverThreadTCPList.start()
      src.listContacts(userEmail)
      serverThreadTCPList.join()
      serverThreadTCPList = threading.Thread(target=src.tcpServer, args=(userEmail,))
      src.sendMessage()

    elif command == "exit": 
      stop_threads = True
      serverThreadTCPSend.join()
      serverThreadUDP.join()
      return
    else:
      print(f"\n'{command}' is not a valid command.\n")
      
main()