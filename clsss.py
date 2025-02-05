try:
    class studant:
    
        def __init__(self,name,adge):
            self.name=name 
            self.adge=adge
        def __str__(self):
            return f"{self.name},{self.adge}"
        def get_info(self):
             print(f"this is : {self.name} his adge is :{self.adge} ")
    std=[]
    while True: 
        x= input("enter bthe key _")
        
        if x=="create":

            d=input("ENTER STD_NAME :- ") 
            c=int(input("entar adge :- "))
            y=studant(d,c)
            std.append(y)
            

        elif x=="get_info":
            name=input("enter yhe std name :")
            for i in std:
                 if i.name==name :
                      i.get_info()
        elif x=="done":
             break
        
        else:
             print("wrong ")
            

except ValueError:
        print("pleas enter a integer in adge ")