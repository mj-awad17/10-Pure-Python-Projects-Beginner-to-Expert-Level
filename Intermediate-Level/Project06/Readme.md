# 📱 Project 06: Contact Book – A Simple CLI Contact Manager in Python

Looking for a lightweight, no-fuss contact manager? Say hello to **Contact Book** – your new command-line buddy to store, view, edit, search, and delete contacts — all from your terminal!

No databases. No fluff. Just Python, JSON, and productivity. 🧠✨

---

## ✨ Why You'll Love This

- 🚀 **Fast**: Runs instantly on any machine with Python
- 🧠 **Simple**: Clean code and logic that beginners can understand
- 📦 **Portable**: Your contacts are stored locally in a `contacts.json` file
- 🎯 **Practical**: Learn file I/O, JSON handling, lists, and CLI menus

---

## 🛠 Features

| Feature           | Description                                  |
|-------------------|----------------------------------------------|
| ➕ Add Contact     | Name, phone, and email input with emojis 😎  |
| 📋 View Contacts   | See all your saved contacts, neatly listed  |
| 🔍 Search          | Search contacts by name (case-insensitive)  |
| ✏️ Edit Contact     | Update any field or leave it unchanged      |
| 🗑️ Delete Contact   | Remove a contact you no longer need         |
| 💾 Auto-Save       | Saves after each change                     |

---

## 🏗️ How It Works

Your contacts are stored in a simple `contacts.json` file. When you:

- Run the app, it loads the data
- Make changes, it auto-saves to the same file
- Add/Edit/Delete → It’s all tracked seamlessly

No third-party libraries required — just standard Python!

---

## 📦 File Structure

Intermediate-Level/
└── Project06/
├── contact_book.py
├── contacts.json ← auto-created on first use
└── README.md

Follow the menu prompts and start managing your contacts like a pro:
📱 Contact Book 📱
1. ➕ Add Contact
2. 📋 View Contacts
3. 🔍 Search Contact
4. ✏️  Edit Contact
5. 🗑️  Delete Contact
6. 🚪 Exit

---
## 🧠 What You’ll Learn

- 🔄 Reading & writing JSON files

- 💡 Validating user input with conditionals

- 🗃️ Storing data in Python lists and dictionaries

- 📁 Handling files safely with os.path

- Building interactive CLI menus with input() and loops

---
## 🚫 Error Handling Included

- ❌ File not found? → Auto-creates contacts.json
- 🔄 Bad inputs? → Gracefully handled with helpful messages
- 📭 No contacts? → Alerts the user when lists are empty

## 💡 Who Is This For?
Whether you're a beginner learning Python or a developer who loves terminal tools, this project gives you hands-on practice with real-world Python programming essentials.