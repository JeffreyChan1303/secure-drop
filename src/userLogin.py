from userRegistration import userRegistration


def userLogin():
  users = {} # stores users in this format { email: [fullName, password] }

  fp = open("./src/users.txt", "r")
  # loops through the txt file for all the user data
  for line in fp:
    fullName, email, password = line.split(" ")
    users[email] = [fullName, password]

  # if there are no users, call the user registration function
  if len(users) == 0:
    userRegistration(users)
  
  
  


