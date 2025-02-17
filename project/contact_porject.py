class ContactBook:
    contacts = {}  
    history = {} 
    num_call = 0 
    store=[]
    new_contact ={}

    def init(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number 
        ContactBook.contacts[phone_number] = name
        ContactBook.history[phone_number] = []
        ContactBook.store.append(name,phone_number)

    def str(self):
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
    def contact_book(cls ,name,phone_number):
       for name,phone_number in cls.store:
           if name and phone_number in cls.store:
                #print(f"{name}: {phone_number}")
                return f"{name}: {phone_number}"
           else:
                print("Number not found in contacts.")
           

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
    def merge_contacts(cls):
        for name, phone_number in cls.new_contact.items():
                cls.contacts[name] = phone_number
                print(cls.contacts)
                print(f"Contacts merged successfully")

    @classmethod
    def store_contacts(cls):
        if not ContactBook.contacts:  
            print("No contacts stored yet.")
            return  
        print("Contacts stored:")
        for phone_number, name in ContactBook.contacts.items():
            print(f"{name}: {phone_number}")

    @classmethod
    def view_contacts(cls):
        
        for number, name in cls.contacts.items():
                
                print(f"{name}: {number}")

    


    @classmethod    
    def edit_contact(cls, phone_number,name):
        for  phone_number,name in cls.contacts:
            if phone_number and name in cls.contacts:
                print("Contact found.")

                name = input("Enter new name: ")
                phone_number = int(input("Enter new number: "))

                cls.contacts[phone_number] = name 

            print(f"The contact has been edited: {name} ({phone_number}) ")
           
        else:
            print("Number not found in contacts.")


print("welcome to contact book app you can:")
print("add")
print("delete")
print("edit")
print("make call")
print(" history")
print("store")
print("merge")
print("view")
print("done")
print("Enter a command to continue.")       

while True:
    try:
        
       

        command = input("What do you want: ")

        if command == "add":
            name = input("Enter name: ")
            phone_number = input("Enter number: ")
            ContactBook.add_person(name, phone_number)
  
        elif command == "delete ":
            phone_number = input("Enter number to delete: ")
            ContactBook.remove_contact(phone_number)
            
        elif command == "edit":
            phone_number = input("Enter number to edit: ")
            name=input("enter the name to edit ")
            ContactBook.edit_contact(phone_number, name)


        elif command == "make call":
            phone_number = input("What the number you wante to call: ")
            ContactBook.make_call(phone_number)    

        elif command == "history":
            phone_number = input("Enter number to view call history: ")
            if phone_number in ContactBook.contacts:
             ContactBook.get_history(phone_number) 

            else:
                print("Number not found in contacts please  make a call first.")
                
        elif command == "store":
           
            ContactBook.store_contacts()


        elif command == "merge":
            name = input("Enter name: ")
            phone_number = input("Enter number: ")
            ContactBook.new_contact[name] = phone_number
            ContactBook.merge_contacts()


        elif command == "view":
            show={} 
            show=ContactBook.view_contacts() 
            print(show)
    
        elif command == "done":
            print("Contact book closed.")
            break

        else:
            print("Invalid command, try again.")

    except ValueError:
        print("Error: The number must be a valid integer.")