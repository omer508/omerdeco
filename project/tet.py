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
            print(f"Contacts merged: {num2} → {num1}")
        else:
            print("One or both numbers not found in contacts.")

    @classmethod
    def store_contacts(cls, phone_number,name):
        if not ContactBook.contacts:  
            print("No contacts stored yet.")
            return  
        print("Contacts stored:")
        for phone_number, name in ContactBook.contacts.items():
            print(f"{name}: {phone_number}")
    @classmethod    
    def edit_contact(cls, phone_number,name):
        for  phone_number,name in cls.contacts:
            if phone_number and name in cls.contacts:
                name = input("Enter new name: ")
                phone_number = input("Enter new number: ")
                cls.contacts[phone_number] = name 

            print(f"The contact has been edited: {name} ({phone_number}) ")
            print("Contact edited successfully.")
        else:
            print("Number not found in contacts.")


print("welcome to contact book app you can:")
print("add contact")
print("delete contact")
print("edit")
print("make call")
print("get history")
print("store")
print("merge")
print("done")
print("Enter a command to continue.")       

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
            
        elif command == "edit":
            phone_number = input("Enter number to edit: ")
            name=input("enter the name to edit ")
            ContactBook.edit_contact(phone_number, name)


        elif command == "make call":
            phone_number = input("What the number you wante to call: ")
            ContactBook.make_call(phone_number)    

        elif command == "get history":
            phone_number = input("Enter number to view call history: ")
            if phone_number in ContactBook.contacts:
             ContactBook.get_history(phone_number) 

            else:
                print("Number not found in contacts please  make a call first.")
                
        elif command == "store":
           
            phone_number = input("Enter number : ")
            name=input("enter the name :")
            print(ContactBook.store_contacts( phone_number,name)) 


        elif command == "merge":
            num1 = input("Enter second number: ")
            name2 = input("Enter second name: ")
            contact2=ContactBook.add_person(name2, num1)
            old_num = input("Enter first number: ")

            ContactBook.merge_contacts(old_num,contact2 )

    
        elif command == "done":
            print("Contact book closed.")
            break

        else:
            print("Invalid command, try again.")

    except ValueError:
        print("Error: The number must be a valid integer.")


        