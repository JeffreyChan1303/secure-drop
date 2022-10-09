import json

def addContact():
  with open("./data/contacts.json", "r+") as fp:
    userContacts = json.load(fp)

  print(type(userContacts))
  print(userContacts)
  # fullName = input("  Enter Full Name: ")
  # email = input("  Enter Email: ")

  return