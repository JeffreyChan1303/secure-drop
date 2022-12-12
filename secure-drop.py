import src
import threading


def main():
  # login to application, stores the userEmail for future use
  userEmail = src.userLogin()
  if userEmail is None:
    return
  
  serverThreadUDP = threading.Thread(target=src.udpServer, args=(userEmail, ))
  serverThreadTCPList = threading.Thread(target=src.tcpServerList, args=(userEmail,))
  serverThreadTCPFile = threading.Thread(target=src.tcpServerFile, args=(userEmail,))
  serverThreadUDP.daemon = True
  serverThreadTCPFile.daemon = True
  serverThreadUDP.start()
  serverThreadTCPFile.start()

  print("\n\nWelcome to Secure Drop")
  print("Type 'help' for commands\n")

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
      serverThreadTCPList.start()
      src.listContacts(userEmail)
      serverThreadTCPList.join()
      serverThreadTCPList = threading.Thread(target=src.tcpServerList, args=(userEmail,))
      src.sendMessage(userEmail)

    elif command == "exit": 
      print("Exiting SecureDrop...\n")
      return

    elif command.lower() == 'y':
      print("Are you sure you want to accept the file? (y/n)")

    elif command .lower() == 'n':
      print("Enter 'n' again if you want to deny this file.")

    else:
      print(f"\n'{command}' is not a valid command")
      displayCommands()

def displayCommands():
  print("  'add' -> Add a new contact.")
  print("  'list' -> List all online contacts")
  print("  'send' -> Transfer file to contact")
  print("  'exit' -> Exit SecureDrop\n")

main()