def add_contact(contacts):
    """Adds a new contact to the contact list."""
    email = input("Email (unique): ").strip().lower()
    # Check for duplicate emails
    for contact in contacts:
        if contact['email'] == email:
            print("A contact with this email already exists.")
            return
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    phone = input("Phone: ").strip()
    city = input("City: ").strip()
    contacts.append({
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email,
        'city': city
    })
    print("Contact added successfully!")

def remove_contact(contacts):
    """Removes a contact by email address."""
    email = input("Enter the email of the contact to remove: ").strip().lower()
    for contact in contacts:
        if contact['email'] == email:
            contacts.remove(contact)
            print("Contact removed.")
            return
    print("Contact not found.")

def update_contact(contacts):
    """Updates a contact's information by email address."""
    email = input("Enter the email of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact['email'] == email:
            print(f"Current info: {contact}")
            field = input("Enter field to update (first_name, last_name, phone, city): ").strip().lower()
            if field in ['first_name', 'last_name', 'phone', 'city']:
                contact[field] = input(f"Enter new {field.replace('_', ' ')}: ").strip()
                print("Contact updated.")
            else:
                print("Invalid field name.")
            return
    print("Contact not found.")

def list_contacts(contacts):
    """Displays all contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        print("\nAll Contacts:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['first_name'].title()} {contact['last_name'].title()}, "
                  f"Phone: {contact['phone']}, Email: {contact['email']}, "
                  f"City: {contact['city'].title()}")

def main():
    contacts = []
    while True:
        print("\nContact Book Menu: add / remove / update / list / quit")
        choice = input("Choose an option: ").strip().lower()
        if choice == 'add':
            add_contact(contacts)
        elif choice == 'remove':
            remove_contact(contacts)
        elif choice == 'update':
            update_contact(contacts)
        elif choice == 'list':
            list_contacts(contacts)
        elif choice == 'quit':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
