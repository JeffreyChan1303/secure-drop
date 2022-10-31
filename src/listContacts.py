import json

def listContacts(userEmail):
  with open("./data/contacts.json", "r") as fp:
    allContacts = json.load(fp)
    userContacts = allContacts[userEmail]
    print("\nFull Name | Email\n")
    for contact in userContacts.values():
      print(contact["fullName"], "|", contact["email"])
