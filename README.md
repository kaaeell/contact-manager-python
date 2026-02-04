# Contact Manager (Python)

This is a simple terminal-based contact manager written in Python.  
It lets you **add, view, search, update, delete, and save contacts**. All the data is stored in a JSON file, so your contacts stay saved even after you close the program.

I built this project to practice Python basics, like working with dictionaries, loops, functions, and file handling, and to make a small, real-world application.

---

## Features

- Add a contact (name, phone, email)  
- View all contacts  
- Search for a contact by name  
- Update contact information  
- Delete a contact  
- Clear all contacts  
- Data is saved automatically in `contacts.json`  
- Menu-driven interface that runs in the terminal  

---

## How to Run

1. Make sure you have **Python 3** installed.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run the program:

python main.py

5. Follow the menu prompts to manage your contacts.

> The program automatically creates a `contacts.json` file in the same folder to store your contacts.

---

## How It Works

- Contacts are stored in a Python dictionary while the program is running.  
- Whenever you add, update, delete, or clear contacts, the program saves the changes to `contacts.json`.  
- When you start the program, it automatically loads the contacts from the JSON file.  
- Searching is case-insensitive, so “Kael” and “kael” will be treated the same.

---

## Notes
- Basic input validation is included (empty names are not allowed).
- Contacts are stored locally in a JSON file.
- Avoid saving duplicate phone numbers.


## About

This project was made by **Yaser (Kael)** as a Python learning project.  
It’s simple, easy to understand, and a good example of a small, real-world CLI application.





