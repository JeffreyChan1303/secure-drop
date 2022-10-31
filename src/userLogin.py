import json
import bcrypt
from src.userRegistration import userRegistration


def userLogin():
  users = {} # stores users in this format { email: [fullName, password] }

  with open("./data/users.json", "r") as fp:
    users = json.load(fp)

  # if there are no users, call the user registration function
  if len(users) == 0:
    userRegistration(users)
  else:
    # ask the user if they want to create a new user
    createNewUser = input("Enter 'y' to create new user. \nEnter 'n' to login. \n")
    while createNewUser.lower() != 'y' and createNewUser.lower() != 'n':
      print("Invalid input. ")
      createNewUser = input("Enter 'y' to create new user. \nEnter 'n' to login. \n")
    if createNewUser.lower() == 'y':
      userRegistration(users)

  # user login loop
  print("User Login...")
  email = input("Enter Email Adress: ").strip()
  password = input("Enter Password: ").strip()
  bPassword = password.encode("utf-8")

  while email not in users or not bcrypt.checkpw(bPassword, users[email]["password"].encode("utf-8")):
    print("Invalid Email or Password.")
    email = input("Enter Email Adress: ").strip()
    password = input("Enter Password: ").strip()
    bPassword = password.encode("utf-8")
  
  print("Loged in as " + users[email]["fullName"] + ".")

  return email
  

  


