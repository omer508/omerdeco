x={'first':[1,2,3,],'secnd':'me','third':50.4,'forth':0,'fifth':[4,5,6]}
y=list(x.values())
m=list(x.keys())
#for i in x.values():
for j in range(len(y)):
  for i in range(4,-1,-1):
    x[m[j]]=y[i]
  
print(x)
