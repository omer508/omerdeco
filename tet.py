
class items:
    all_contact = {}
    
    def __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber
        items.all_contact[name] = phonenumber

    def __str__(self):
        return f"{self.name}, {self.phonenumber}"       

    @classmethod
    def cell(cls, name, phonenumber):
        for i in cls.all_contact:
            if i == name:
                if cls.all_contact[name] >= phonenumber:
                    cls.all_contact[name] -= phonenumber
                    return 0
                return 1
        return 2
    
    @classmethod
    def history(cls):
        i = 0
        for item in cls.all_contact.values():
            i += item
        return i

    @classmethod
    def inventory(cls):
        return str(cls.all_contact)

while True:
    try:
        command = input("How can I help you: ")
        if command == "add item":
            item_name = input("what is the item name: ")
            item_phonenumber = int(input("what is the number you want to add: "))
            new_item = 1
            for i in items.all_contact:
                if i == item_name:
                    items.all_contact[item_name] += item_phonenumber
                    new_item = 0
                    print("add to existing item")
            if new_item == 1:
                item = items(item_name, item_phonenumber)
                print("add new item")
        elif command == "cell number":
            item_name = input("what is the item name: ")
            item_phonenumber = int(input("what is the number you want to cell: "))
            i = items.cell(item_name, item_phonenumber)
            if i == 0:
                print("item sold successfully")
            elif i == 1:
                print("no sufficient number")
            elif i == 2:
                print("contant not found")
        elif command == "check stock":
            print(items.history())
        elif command == "check inventory":
            print(items.inventory())
        elif command == "done":
            break
        else:
            print("command not found")
    except ValueError:
        print("phonenumber must be a number")



       # ......................................