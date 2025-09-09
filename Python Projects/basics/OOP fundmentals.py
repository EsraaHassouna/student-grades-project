# OOP
# instance attributes and methods
# class attributes and methods can be accessd inside constructor and instance methods using self keyword
class Student:
    
    notAllowedNames= ["admin","user","null"]
    deleteUser=0

    def __init__(self,fName,lName,gender,age):
        self.fName=fName
        self.lName=lName
        self.gen=gender
        self.age=age
        self.notAllowedNames=fName
        Student.deleteUser+=1

    
    def removeNotAllowedNames(self):
        if self.fName in Student.notAllowedNames:
            Student.deleteUser-=1
        return f'{self.fName} is not allowed name, user deleted'        

    
    def fullName(self):
        return f"{self.fName} {self.lName}"

    def IsAdult(self):
        return self.age>=18

    def allInfo(self):
        if self.IsAdult():
            return f"Adult, then your full name is {self.fullName()} and you are {self.gen}"
        elif not self.IsAdult():
            return f"{self.fName}, you are under age under your dad's supervision, {self.lName}"




print(Student.deleteUser)

stu1= Student("Esraa","Hassouna","female",22)
stu2= Student("Omar","Mohamed","Male",24)
stu3= Student("Mariam","Omar","Female",2)
stu4= Student("null","catroon","Female",95)

print(Student.deleteUser)

print(Student.removeNotAllowedNames(stu4))

print(Student.deleteUser)
        
print(stu1.allInfo())
print(stu2.allInfo())
print(stu3.allInfo())