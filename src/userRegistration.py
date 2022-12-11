import bcrypt
import json


def checkPassword():
  specialCharacters = { "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", 
    "{", "[", "]", "}", "\\", "|", ":", ";", "'", "<", ",", ">", ".", "/", "?"}
  # declare checking value
  passwordCheck = False

  # check if the passwords match
  while passwordCheck != True:
    passwordCheck = True

    # input the password and confirm the password
    password = input("Enter Password: ").strip()
    confirmPassword = input("Re-enter Password: ").strip()

    # check the length of the password
    if len(password) < 8:
      passwordCheck = False
      print("\nPassword needs to have 8 or more characters.")

    # check if the password contains a special character
    containsSpecial = False
    for c in password:
      if c in specialCharacters:
        containsSpecial = True
    
    if containsSpecial == False:
        print("\nPassword does not contain a special character.")
        passwordCheck = False
            
    # check if the password and confirm password are the same
    if password != confirmPassword:
        passwordCheck = False
        print("\nPasswords do not match.")

  return password

def userRegistration(users):
    print("Creating New User... (enter 'exit' to quit):")
    fullName = input("Enter Full Name: ").strip()
    if fullName == 'exit':
      return
    email = input("Enter Email Adress: ").strip()
    
    # check if the email is already taken
    while email in users:
        print("This email is already registered, login or use another email. ")
        email = input("Enter Email Adress (type 'exit' to quit): ").strip()
        if email == "exit":
            return "Failed"

    password = checkPassword()
    bPassword = password.encode("utf-8")

    print("\nPassword is valid.")
    
    # add user into the json file
    users[email] = {
        "fullName": fullName,
        "password": bcrypt.hashpw(bPassword, bcrypt.gensalt()).decode("utf-8")
    }
    with open("./data/users.json", "w") as fp:
        json.dump(users, fp, indent=2)

    print("User registered.\n")