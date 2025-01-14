c=1   
while c<10:
    if c%2==0:
        print(c)
    if c==8:
        c=1
        for c in range(9):
            if c%2!=0:
                print(c)
    
    c=c+1