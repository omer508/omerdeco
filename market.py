class market:

    def __init__(self,name , quan):
        self.name=name
        self.quan=quan
    def __str__(self):
        return f"{self.name} the quantity  is :- {self.quan}"
    def cheeck_stock(self):
        return  f"{self.name} whith quantity  is :- {self.quan}"
    def get_info(self):
                return f"{self.name} the quantity  is :- {self.quan}"


   
while True:
    try:
        add_item=[]
        sold_item=[]
        stock=[]
        x=input("ENTER THE KEY: ")

        if x=="add":
            n=input("ENTER TEH NAME OF PRODCUT: ")
            q=int(input("ENTYER THE QUANTITY: "))
            y=market(n,q)
            add_item.append(y)
            stock.append(y)
            print("ADD SUCSSE")

        elif x=="sell":
            name=input("ENTER THE PRODUCT: ")
            for i in add_item:
                if i.name==name:
                    i.get_info()
                    print(i)
                elif i.name !=name :
                    sold_item.append(name)
                    stock.pop()
                    print(sold_item)

                    t=input("how match you need : ")
                    co=int(input())
                if i.co==market.quan:
                    i.get_info()
               
                       

        elif x=="ck":
            print(market.cheeck_stock())
        elif x=="cheeckout":
            break



    except ValueError:
        print("WRONG COMMAND TRY AGAIN ")              