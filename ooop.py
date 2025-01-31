class hotel:
 #class properties
    a=0
    room=[]
    def __init__(self,name ,num_room):
        self.name =  name 
        self.num_room= num_room
    @classmethod
    def gest(cls):
        cls.room.append(5) 
        return cls.room

                   
   

    @staticmethod
    def static_method(co,co2,co3):
        print(f'the blookced room account : ', {co + co2 + co3})
        print(0000000000000)

print(hotel.gest())
hotel.static_method(3,4,5)

