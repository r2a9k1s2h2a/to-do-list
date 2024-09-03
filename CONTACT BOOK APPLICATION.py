# Contact book using Python

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact['name']} - {contact['phone']}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        else:
            print("No contact found with that search term.")

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                print("Updating contact details:")
                name = input("Enter new name (leave blank to keep current): ") or contact['name']
                phone = input("Enter new phone number (leave blank to keep current): ") or contact['phone']
                email = input("Enter new email (leave blank to keep current): ") or contact['email']
                address = input("Enter new address (leave blank to keep current): ") or contact['address']
                contact.update({'name': name, 'phone': phone, 'email': email, 'address': address})
                print(f"Contact '{name}' updated successfully!")
                return
        print("No contact found with that search term.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                self.contacts.remove(contact)
                print(f"Contact '{contact['name']}' deleted successfully!")
                return
        print("No contact found with that search term.")

    def user_interface(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                search_term = input("Enter name or phone number to search: ")
                self.search_contact(search_term)
            elif choice == '4':
                search_term = input("Enter name or phone number to update: ")
                self.update_contact(search_term)
            elif choice == '5':
                search_term = input("Enter name or phone number to delete: ")
                self.delete_contact(search_term)
            elif choice == '6':
                print("Exiting the Contact Book. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.user_interface()
