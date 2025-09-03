#my first small project in python
#print(stuList[0]['grades']['Math']) # to access any value in the list of dictionaries
stuList = [    
    {'name':'Omar','age':'15', 'grades':{'Math':90, 'Science':80, 'English':70}}, #stuList[0]
    {'name':'Sara','age':'17', 'grades':{'Math':85, 'Science':95, 'English':80}}, #stuList[1]
    {'name':'Ali','age':'16', 'grades':{'Math':78, 'Science':88, 'English':92}} , #stuList[2]
    {'name':'Lina','age':'15','grades':{'Math':92, 'Science':81, 'English':76}}, #stuList[3]

]
total=0     #to calc averege you need sum of all grages and the number of students
noOfStd=0   # len(stuList) will solve it easer 
            # noOfStd to count the number of students to calculate the average

for i in stuList:
    math=i['grades']['Math'] # to access the math grade for each student
    total+=math 
    noOfStd+=1   
    print (f"The math grade of {i['name']} is {math}")

try:
    if noOfStd==len(stuList)==0:
        raise ZeroDivisionError
    avg=float(total/noOfStd) # to calculate the average of math grades for each student
    print (f"The average of math grades is {avg}")

# Now, update Sara's age based on user input    
    sara = next((student for student in stuList if student['name'] == 'Sara'), None)
    if sara == None:#sara not found in the list 
        raise LookupError("Sara not found in the student list.")
    
    age=int(input())
    sara['age']=age
    if age<0:
        raise ValueError("age have to be positive number")
    print (sara)      

except ZeroDivisionError:
    print("No students in the list to calculate the average.")    
except ValueError as e:
        print(e)
except LookupError as e:    
        print(e)