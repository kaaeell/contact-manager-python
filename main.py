import json

file_name = "contacts.json"
print("CONTACT MANAGEMENT SYSTEM")


def l_c():  # load contacts
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts():
    with open(file_name, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = l_c()  # Load contacts


def show_menu():
    print("\nMenu:")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Clear all contacts")
    print("7. Exit")


def get_valid_name(prompt):
    while True:
        name = input(prompt).strip().lower()
        if name:
            return name
        print("Name cannot be empty.")


def phone_exists(phone):
    for contact in contacts.values():
        if contact["phone"] == phone:
            return True
    return False


def add_contact():
    name = get_valid_name("Enter contact name: ")

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    if phone_exists(phone):
        print("This phone number is already saved.")
        return

    email = input("Enter email address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts()
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

    save_contacts()
    print("Contact updated successfully.")


def delete_contact():
    name = input("Enter contact name to delete: ").strip().lower()

    if name not in contacts:
        print("Contact not found.")
        return

    delete_confirmation = input(
        "Are you sure you want to delete this contact? (y/n): "
    ).strip().lower()

    if delete_confirmation != "y":
        print("Delete cancelled.")
        return

    del contacts[name]
    save_contacts()
    print("Contact deleted successfully.")


def clear_everything():
    global contacts
    contacts = {}
    save_contacts()
    print("All contacts cleared.")


while True:
    show_menu()
    choice = input("Choose an option (1-7): ").strip()

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
        clear_everything()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
