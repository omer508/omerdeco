import random

names = []
try:
    for i in range(9):
        x = input("enter name : ")
        names.append(x)
    
    selected_names = []
    for i in range(3):
        c=[]
        while len(selected_names) < 3:
            ind = random.randint(0, len(names) - 1)
        if names[ind] not in selected_names:
            c= names[ind]
            selected_names.append(names[ind])
    
            print(c)
except ValueError:
    print("wrong data type ")

    import random

names = []
try:
    for i in range(9):
        x = input("enter a name: ")
        names.append(x)
    
    groups = []
    while len(groups) < 3:
        group = []
        while len(group) < 3:
            ind = random.randint(0, len(names) - 1)
            if names[ind] not in group:
                group.append(names[ind])
                names.pop(ind)
        groups.append(group)
    
    print(groups)
except ValueError:
    print("wrong input")