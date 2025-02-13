class ContactBook:
    contacts = {}  
    history = {} 
    num_call = 0 

    def _init_(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number 
        ContactBook.contacts[phone_number] = name
        ContactBook.history[phone_number] = []

    def _str_(self):
        return f"{self.name}: {self.phone_number}"   
    
    @classmethod
    def add_person(cls, name, phone_number):        
        if phone_number in cls.contacts:
            print("This number already exists.")
        else:
            cls.contacts[phone_number] = name
            cls.history[phone_number] = []  
            print(f"The number has been added: {name} ({phone_number}) ")

    @classmethod
    def remove_contact(cls, phone_number):
        if phone_number in cls.contacts:
            cls.contacts.pop(phone_number)
            cls.history.pop(phone_number)
            print("Contact deleted successfully.")
        else:
            print("Number not found in contacts.")

    @classmethod
    def get_history(cls, phone_number):
        if phone_number in cls.history:
            print(f" history for {cls.contacts[phone_number]} ({phone_number}): {len(cls.history[phone_number])}")

    @classmethod
    def make_call(cls, phone_number):
        if phone_number in cls.contacts:
            cls.history[phone_number].append("Call")
            print(f"Call made to {cls.contacts[phone_number]} ({phone_number}) successfully.")
        else:
            print("Number not found in contacts.")

    @classmethod
    def merge_contacts(cls, num1, num2):
        if num1 in cls.contacts and num2 in cls.contacts:
            cls.history[num1].append(cls.history.get(num2, []))
            #cls.remove_contact(num2)
            print(f"Contacts merged: {num2} → {num1}")
        else:
            print("One or both numbers not found in contacts.")




while True:
    try:
        command = input("What do you want: ") 
        if command == "add contact":
            name = input("Enter name: ")
            phone_number = input("Enter number: ")
            ContactBook.add_person(name, phone_number)
  
        elif command == "delete contact":
            phone_number = input("Enter number to delete: ")
            ContactBook.remove_contact(phone_number)

        elif command == "make call":
            phone_number = input("Enter number to call: ")
            ContactBook.make_call(phone_number)    

        elif command == "get history":
            phone_number = input("Enter number to view call history: ")
            ContactBook.get_history(phone_number)    

        

        elif command == "merge":
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            ContactBook.merge_contacts(num1, num2)

        elif command == "done":
            print("Contact book closed.")
            break


        else:
            print("Invalid command, try again.")

    except ValueError:
        print("Error: The number must be a valid integer.")