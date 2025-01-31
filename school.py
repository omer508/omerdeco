class school:
    #class properties
    num_students = 0
    std_classrooms = 0
    num_classrooms = []
    GBA=[]

    #properties

    def __init__(self, name, classroom, grade):
        self.name = name
        self.classroom = classroom
        self.grade = grade
        school.num_students += 1
        school.num_classrooms.append(classroom)
        school.GBA.append(grade)

    @classmethod

    def get_GBA(cls):
        return cls.GBA
    

    def count_classrooms(cls):
        for i in range(len( school.num_classrooms)):
            if school.num_classrooms[i] == 0:
                school.num_classrooms[i]+=1
            
            print(cls.num_classrooms[i])
   #method

    def info(self):
        print(f"MY Name :- {self.name},I study in :- {self.classroom},with result:- {self.grade}")

    def STD_GBA(self):
        for i in range(len(self.grade)):
            if self.grade[i]>=90:
                print(f"student {self.name} exsllent")

            if self.grade[i]>=80:
                print(f"student {self.name} very good")

            if self.grade[i]>=60:
                print(f"student {self.name} good")
            
            if self.grade[i]>=50:
                print(f"student {self.name} passed")

            else:
                print(f"student {self.name} failed")


    def __str__(self):

        return f"{self.name},{self.classroom},{self.grade}"
   
            

#output
 
c1=school('omer',5,[70,95,60])
c2=school('ali',4,[60,45,55])
c1.info()
print(f'<...........................................>')
c2.info()
print(f'<............................................>')

c1.STD_GBA()
print(f'<.............................................>')
c2.STD_GBA()
print(f'<.............................................>')

print(f'THE NUMBER OF STUDENT IS : ',school.num_students)

print(f'<.............................................>')

print (school.count_classrooms())
