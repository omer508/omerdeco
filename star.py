while True:
    try:   
        x=input("frst number: ")
        y=input("second number :")
    
    
        for i in range(x):
            for j in range(y):
           
                print("*" ,end="")  
        print()
        break
    except ValueError:
        print("wrong data type ")