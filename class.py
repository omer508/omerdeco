class doctors():
    number=0
    spe=[]

    def __init__(self,name,sepc):
        self.name=name
        self.spec=sepc
        doctors.number+=1
        doctors.spe.append(sepc)
    @classmethod
    def decotor_spec(cls):
       return cls.spe
          
        


        #method
    
    def decotor_info(self):
        print(f"DOCTOR:-{self.name},{self.spec}")

    def __str__(self):
        return f"{self.name},{self.spec}"
    


    
dr=doctors('AHMED','e')
dr2=doctors('MOHAMMED','h')
dr3=doctors('ALI','gs')

dr.decotor_info()
dr2.decotor_info()

print(doctors.spe)

sepc=doctors.decotor_spec()
for i in sepc:
    print(i)

print(doctors.number)
doctors.decotor_spec()

print(dr)