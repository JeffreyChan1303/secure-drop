import json

def addContact(userEmail):
  # read all the contacts in the database
  with open("./data/contacts.json", "r") as fp:
    allUserContacts = json.load(fp)
    if userEmail in allUserContacts:
      userContacts = allUserContacts[userEmail]
    else:
      userContacts = {}


  fullName = input("  Enter Full Name: ").strip()
  email = input("  Enter Email: ").strip()

  # check the database to see it the email is a valid contact
  with open("./data/users.json", "r") as allUsersFp:
    allUsers = json.load(allUsersFp)
    while email not in allUsers:
      print(f"Email is not valid. No {email} in our database. ")
      fullName = input("  Enter Full Name: ").strip()
      email = input("  Enter Email: ").strip()

  # add contact into the user's contacts
  userContacts[email] = {
    "fullName": fullName,
    "email": email,
  }
  allUserContacts[userEmail] = userContacts
  with open("./data/contacts.json", "w") as fp:
    json.dump(allUserContacts, fp)
    print(f"  Successfully added contact {email} as {fullName}.")

  return "Success"