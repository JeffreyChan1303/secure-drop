import json


def addContact(userEmail):
  # read all the contacts in the database
  with open("./data/contacts.json", "r") as Cfp:
    allUserContacts = json.load(Cfp)
    if userEmail in allUserContacts:
      userContacts = allUserContacts[userEmail]
    else:
      userContacts = {}

  # get the user's input for the contact
  print("Adding a contact (enter 'exit' to quit):")
  fullName = input("  Enter Full Name: ").strip()
  if fullName == 'exit':
    return
  email = input("  Enter Email: ").strip()

  # add contact into the user's contacts
  userContacts[email] = {
    "fullName": fullName,
    "email": email,
  }

  # dump the new contact into the contacts file
  allUserContacts[userEmail] = userContacts
  with open("./data/contacts.json", "w") as Cfp:
    json.dump(allUserContacts, Cfp, indent=2)
    print(f"Successfully added contact {email} as {fullName}.")