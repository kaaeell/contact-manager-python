print("CONTACT MANAGEMENT SYSTEM")

contacts = {}

while True:
    print("\nMenu:")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        name = input("Enter contact name: ").strip()

        if name in contacts:
            print("Contact already exists.")
        else:
            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()

            contacts[name] = {
                "phone": phone,
                "email": email
            }

            print("Contact added successfully.")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContacts List:")
            for name, info in contacts.items():
                print(f"Name : {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print("-" * 20)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
