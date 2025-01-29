class student:
    def __init__(self,name,year,grades):
        self.name=name
        self.year=year
        self.grades=grades

    def info(self):
        print(f"my name :{self.name},I study in :{self.year},with result:{self.grades}")

    def deg(self):
        for i in range(len(self.grades)):
            if self.grades[i]>=50:
                print(f"student {self.name} secceeded")
            else:
                print(f"student {self.name} failed")

    def __str__(self):
        return f"{self.name},{self.year},{self.grades}"

    
        



x=student('omer',5,[50,45,55])
x.info()
x.deg()

print(x)   