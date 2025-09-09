# OOP
# instance attributes and methods
class Student:
    
    
    def __init__(self,fName,lName,gender,age):
        self.fName=fName
        self.lName=lName
        self.gen=gender
        self.age=age

    
    
    
    def fullName(self):
        return f"{self.fName} {self.lName}"

    def IsAdult(self):
        return self.age>=18

    def allInfo(self):
        if self.IsAdult():
            return f"Adult, then your full name is {self.fullName()} and you are {self.gen}"
        elif not self.IsAdult():
            return f"{self.fName}, you are under age under your dad's supervision, {self.lName}"


stu1= Student("Esraa","Hassouna","female",22)
stu2= Student("Omar","Mohamed","Male",24)
stu3= Student("Mariam","Omar","Female",2)

'''
for i in [stu1,stu2,stu3]:
    print("PArent Name is ",i.lName)
'''


        
print(stu1.allInfo())
print(stu2.allInfo())
print(stu3.allInfo())