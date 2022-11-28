import src
import threading


def main():
  stopThreads = False
  # login to application, stores the userEmail for future use
  # userEmail = src.userLogin()
  userEmail = "jeff@gmail.com"
  
  serverThread = threading.Thread(target=src.udpserver, args=(userEmail, stopThreads))
  serverThread.start()

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
      src.listContacts(userEmail)
    elif command == "send":
      src.sendMessage()
    elif command == "exit": 
      stopThreads = True
      serverThread.join()
      return
    else:
      print(f"\n'{command}' is not a valid command.\n")
      
main()