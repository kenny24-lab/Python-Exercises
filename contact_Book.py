contacts = {}

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact saved.")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts.")
        else:
            print("\nContacts")
            for name, phone in contacts.items():
                print(name, "-", phone)

    elif choice == "3":
        search = input("Enter name: ")

        if search in contacts:
            print("Phone:", contacts[search])
        else:
            print("Contact not found.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")