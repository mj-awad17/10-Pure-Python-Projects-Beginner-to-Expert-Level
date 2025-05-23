import json
import os

CONTACTS_FILE = os.path.join(os.path.dirname(__file__), "contacts.json")


def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("📝 Name: ").strip()
    phone = input("📱 Phone: ").strip()
    email = input("📧 Email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    print("✅ Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("❌ No contacts found.")
        return
    print("📋 Contact List:")
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. 👤 {c['name']} | 📱 {c['phone']} | 📧 {c['email']}")

def search_contacts(contacts):
    term = input("🔍 Search by name: ").strip().lower()
    found = [c for c in contacts if term in c['name'].lower()]
    if not found:
        print("❌ No contacts found.")
    else:
        print("🔍 Search Results:")
        for c in found:
            print(f"👤 {c['name']} | 📱 {c['phone']} | 📧 {c['email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("✏️ Enter contact number to edit: ")) - 1
        if 0 <= idx < len(contacts):
            contact = contacts[idx]
            print(f"\nEditing contact: {contact['name']}")
            name = input("📝 New name (press Enter to keep current): ").strip()
            phone = input("📱 New phone (press Enter to keep current): ").strip()
            email = input("📧 New email (press Enter to keep current): ").strip()
            
            if name: contact['name'] = name
            if phone: contact['phone'] = phone
            if email: contact['email'] = email
            print("✅ Contact updated successfully!")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Invalid input.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("🗑️ Enter contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            removed = contacts.pop(idx)
            print(f"✅ Deleted {removed['name']}.")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Invalid input.")

def main():
    contacts = load_contacts()
    while True:
        print("\n📱 Contact Book 📱")
        print("1. ➕ Add Contact")
        print("2. 📋 View Contacts")
        print("3. 🔍 Search Contact")
        print("4. ✏️  Edit Contact")
        print("5. 🗑️  Delete Contact")
        print("6. 🚪 Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            edit_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("\n👋 Goodbye!\n Come back soon!\n")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()