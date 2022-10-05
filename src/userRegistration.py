import crypt

def userRegistration():
  users = {} # stores users in this format { email: [fullName, password] }

  fp = open("./src/users.txt", "r+")
  # loops through the txt file for all the user data
  for line in fp:
    fullName, email, password = line.split(" ")
    users[email] = [fullName, password]

  # check if there are any existing users
  if len(users) <= 0:
    print("No users are registered with this client.")
    registerNewUser = input("Do you want to register a new user (y/n)? ").strip()
    while registerNewUser.lower() != 'y' and registerNewUser.lower() != 'n':
      print("Invalid input")
      registerNewUser = input("Do you want to register a new user (y/n)? ")
    
    if registerNewUser.lower() == 'n':
      # this is a place holder for now
      exit(0)

  fullName = input("Enter Full Name: ").strip()
  email = input("Enter Email Adress: ").strip()

  # check if the email is already taken
  while email in users:
    print("This email is already registered, login or use another email. ")
    email = input("Enter Email Adress (type 'exit' to quit): ").strip()
    if email == "exit":
      exit(1)

  password = input("Enter Password: ").strip()
  confirmPassword = input("Re-enter Password: ").strip()

  # check if the passwords match
  while password != confirmPassword:
    print("\nPasswords do not match")
    password = input("Enter Password: ").strip()
    confirmPassword = input("Re-enter Password: ").strip()
    
  print("\nPasswords match.")

  # add user into the txt file
  fp.write(fullName + " " + email + " " + password + "\n")

  print("User registered. \nExiting SecureDrop")
  exit(0)

  


