class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("Contact list is empty.")

    def search_contact(self, search_key):
        found_contacts = []
        for contact in self.contacts:
            if search_key.lower() in contact.name.lower() or search_key in contact.phone_number:
                found_contacts.append(contact)
        if found_contacts:
            print("Search Results:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No contacts found matching the search key.")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                contact.phone_number = new_phone
                contact.email = new_email
                contact.address = new_address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Sea
