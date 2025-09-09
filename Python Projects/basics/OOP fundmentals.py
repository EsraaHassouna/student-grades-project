# OOP
# instance attributes and methods
# class attributes and methods can be accessd inside constructor
# and instance methods using class name

class Student:
    
    notAllowedNames= ["admin","user","null"]# any first name in this list is not allowed
    users=0 # to count how many users 

    def __init__(self,fName,lName,gender,age):
        self.fName=fName
        self.lName=lName
        self.gen=gender
        self.age=age
        self.notAllowedNames=fName
#class attribute accessed all over the class using class name
        Student.users+=1

# **deleteUser**
# if it is instance attribute there will be no change
# remains 0
# if it is class attribute it will be changed (changble through all over the class methods)  
    
    def removeNotAllowedNames(self):
        if self.fName in Student.notAllowedNames:
            Student.users-=1
            return f'{self.fName} is not allowed name, user deleted'
        else:
            return f'{self.fName} is allowed name, user added'        

    
    def fullName(self):
        return f"{self.fName} {self.lName}"

    def IsAdult(self):
        return self.age>=18

    def allInfo(self):
        if self.IsAdult():
            return f"Adult, your full name is {self.fullName()} and you are {self.gen}"
        elif not self.IsAdult():
            return f"{self.fName}, you are under age under your dad's supervision, {self.lName}"

print("number of students",Student.users) # 0 there are no objects (users)

stu1= Student("Esraa","Hassouna","female",22)
stu2= Student("Omar","Mohamed","Male",24)
stu3= Student("Mariam","Omar","Female",2)
stu4= Student("null","catroon","Female",95)
allStudents=[stu1,stu2,stu3,stu4]


print("number of students",Student.users)# 4 objects are created from Student class 

for student in allStudents:
    print(student.removeNotAllowedNames())

print("number of students",Student.users)# 1of the usres are deleted so there are now 3 usres only
        
print(stu1.allInfo())
print(stu2.allInfo())
print(stu3.allInfo())