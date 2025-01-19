o=[1,5,"omer",45,4.5]
h=0
for i in o:
 if isinstance(i,int ):
    h+=i
 elif isinstance(i,float):
   h+=i   
 else :
    print(f"This is not number :-  {i}" )
print(h)
