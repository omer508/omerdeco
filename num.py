num=[]
not_num=[]
while True:
    b=input()
    if b=="stop":
        break
    try:
       

            
        num.append(int(b))

        
        

    except ValueError:
       not_num.append(b)

print(num)
print (not_num)