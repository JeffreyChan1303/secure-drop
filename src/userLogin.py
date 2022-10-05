from src.userRegistration import userRegistration


def userLogin():
  users = {} # stores users in this format { email: [fullName, password] }

  fp = open("./src/users.txt", "r")
  # loops through the txt file for all the user data
  for line in fp:
    fullName, email, password = line.split(" ")
    users[email] = [fullName, password.strip()] # strip is for the \n that is taken from the file

  # if there are no users, call the user registration function
  if len(users) == 0:
    userRegistration(users)
  
  # user login loop
  email = input("Enter Email Adress: ").strip()
  password = input("Enter Password: ").strip()
  while email not in users or users[email][1] != password:
    print("Invalid Email or Password.")
    email = input("Enter Email Adress: ").strip()
    password = input("Enter Password: ").strip()
  
  print("Loged in as " + users[email][0] + ".")

  return "Success"
  

  


