import crypt
import json

def userRegistration(users):
   # users are stored in this format { email: [fullName, password] }


  print("Creating New User... ")

  fullName = input("Enter Full Name: ").strip()
  email = input("Enter Email Adress: ").strip()

  # check if the email is already taken
  while email in users:
    print("This email is already registered, login or use another email. ")
    email = input("Enter Email Adress (type 'exit' to quit): ").strip()
    if email == "exit":
      return "Failed"

  password = input("Enter Password: ").strip()
  confirmPassword = input("Re-enter Password: ").strip()

  # check if the passwords match
  while password != confirmPassword:
    print("\nPasswords do not match")
    password = input("Enter Password: ").strip()
    confirmPassword = input("Re-enter Password: ").strip()
    
  print("\nPasswords match.")

  # add user into the json file
  users[email] = {
    "fullName": fullName,
    "password": password,
  }
  with open("./data/users.json", "w") as fp:
    json.dump(users, fp)

  print("User registered. ")
  return "Success"

  


