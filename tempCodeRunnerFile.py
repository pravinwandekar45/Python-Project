class Contact:
    # constructor for name, phone, email
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
# Display FUnction For Displaing All Information
    def display(self):
        print(f"Name:{self.name}, Phone:{self.phone}, E-mail:{self.email}")

# contact Class For Add, display, search, delet contact

class ContactBook:
    def __init__(self):
        self.contacts = [] 
    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact) 
        print("contect added sucessfully.")
# Method For Display The all contacts
    def view_contacts(self):
        if not self.Contacts:
            print("Not In Contact")
        else:
            print("\n All Contact")
            for contact in self.contacts:
                contact.display()
# method for search a perticular contact
    def search_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\n Contaact Found")
                contact.display()
                found = True
                break
            if not found:
                print("Contact Not Found")
# Delete A contact
    def delet_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("contact not found")

book = ContactBook()

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Your Choice:")
    if choice == "1":
        name = input("Enter Name:")
        phone = input("Enter Phone:")
        email = input("Enter Email")
        book.add_contact(name, phone, email)
    elif choice == "2":
        book.view_contacts()
    elif choice == "3":
        search_name = input("Enter A Name to search")
        book.search_contact(search_name)
    elif choice == "4":
        delet_name = input("Enter A Name for a Delete")
        book.delet_contact(delet_name)
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid Choice. Please try Again")