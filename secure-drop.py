import src
import threading


def main():
  stop_threads = False
  # login to application, stores the userEmail for future use
  # userEmail = src.userLogin()
  userEmail = "jeff@gmail.com"
  
  serverThreadUDP = threading.Thread(target=src.udpServer, args=(userEmail, stop_threads))
  serverThreadTCPList = threading.Thread(target=src.tcpServerList, args=(userEmail,))
  serverThreadUDP.start()

  print("\n\nWelcome to Secure Drop")
  print("Type 'help' for commands\n")

  # Shell loop
  while True:
    command = input("secure_drop> ")

    if command == "help":
      displayCommands()

    elif command == "add":
      src.addContact(userEmail)

    elif command == "list":
      serverThreadTCPList.start()
      src.listContacts(userEmail)
      serverThreadTCPList.join()
      serverThreadTCPList = threading.Thread(target=src.tcpServerList, args=(userEmail,))

    elif command == "send":
      src.sendMessage()

    elif command == "exit": 
      stop_threads = True
      serverThreadUDP.join()
      return
      
    else:
      print(f"\n'{command}' is not a valid command")
      displayCommands()

def displayCommands():
  print("  'add' -> Add a new contact.")
  print("  'list' -> List all online contacts")
  print("  'send' -> Transfer file to contact")
  print("  'exit' -> Exit SecureDrop\n")

main()