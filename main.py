print("CONTACT MANAGEMENT SYSTEM")

contacts = {}


def show_menu():
    print("\nMenu:")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")


def add_contact():
    name = input("Enter contact name: ").strip().lower()

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts List:")
    for name in sorted(contacts):
        info = contacts[name]
        print(f"Name : {name.title()}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("-" * 20)


def search_contact():
    name = input("Enter name to search: ").strip().lower()

    if name in contacts:
        info = contacts[name]
        print(f"\nName : {name.title()}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter contact name to update: ").strip().lower()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email address: ").strip()

    contacts[name]["phone"] = phone
    contacts[name]["email"] = email

    print("Contact updated successfully.")


def delete_contact():
    name = input("Enter contact name to delete: ").strip().lower()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


while True:
    show_menu()
    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
