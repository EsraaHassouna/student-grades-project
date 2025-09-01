from math import prod
from functools import reduce


'''
#print("Welcom eng. Esraa now we can say this is your first step in your carrer")
#print("Good luck") 
'''


'''
greating, name, age =input("Enter Hello: your name: your age: ").split() 
print( greating+"\t" + name+"\t" + age +"\t" +" cuty girl ")
sum=int(age)+5
print(sum)
'''

''' formate of float   {:.5f}
amount = 150.75
print("Amount: ${:.5f}".format(amount))
'''

'''
# end with 
print("Esraa Hassouna Saleh 2025" , end="$")
print("Computer and Systems Engineering")
'''

'''
#separate the input with 

print ("Esraa", "software developer", "26 years old" , sep=" @ ")
'''

'''
# for formatting a date
print('09', '12', '2016', sep='-')
'''

'''
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")
'''




'''
# important to be bake once more 
#%d –integer
#%f – float
#%s – string
#%x –hexadecimal
#%o – octal


# Taking input from the user
num = int(input("Enter a value: "))

add = num + 5

# Output
print("The sum is %d" ,%add) # % must be added before variable name as an error for converting to string will occur
'''


'''
# small Calculator
num1,num2 = int(input("Enter first number: ")),int(input("Enter second number: "))

sum = (num1) + (num2)
print("The sum is: %d" %sum)

sub = (num1) - (num2)
print("The sub is: %d" %sub)

mul = int(num1) * int(num2)
print("The mul is: %d" %mul)

div = int(num1) / int(num2)
print("The div is: %d" %div)
'''

'''
# swap two numbers

a, b = 5, 10
a, b = b, a
print(a, b)
'''

#multiline str """ """ triple double qouts but comment ''' ''' trible single qouts 

'''
x = "Hello"
print(x[2:5])# from index 2 to 5 but not include 5
'''
'''
x = 5
y = 2
print(x // y)# floor division nearest integer
'''
'''
num1 = "5"
num2 = 3
result = num1 * num2
print(result) # "555" 5 three times
print(type(result)) # str

#only * can be used between str and int not + or - or / or // or % or **

'''
'''
bool1="10 > 5 and 5 < 3" # this is str not boolean if it is boolean it will be True or False not this expression
print(bool1) # 10 > 5 and 5 < 3
print(bool(bool1))  # True because str is not empty but the geeks say false because the expression is false
print(type(bool1)) # str

'''

'''
str = "GFG"
print(not (not(str and ""))) #empty str is false so output is False then not false will be true and not true will be false
# Output: True

'''
#print("GFG ") 
#print("Hello")
'''
x = input()
y = input()
print(x+5) # error because x is str and 5 is int
'''
'''
x = int(input())
print(x)#ValueError: invalid literal for int() with base 10: '1.5'  
'''   

'''
print(input("Enter message: "))
print("Enter message: ", input())
'''
'''
#short handed if conditional statement or ternary conditional statment
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")# == print("Result: %d" % res)  == print("Result: " + res) == print("Result: {}".format(res)

'''
'''
# match case statement python 3.10 and above
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")

# Output: Two or Three'''

'''
num = int(input("Please enter your number to be tested: "))

print("even") if num % 2 == 0 else print("odd") 

'''

'''
# for loop with enumerate function
#enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. index and value

li = ["eat", "sleep", "repeat"]
for i, j in enumerate(li):
    print (i, j)
# Output:
# 0 eat
# 1 sleep
# 2 repeat
'''
'''
#for i in range(5):

if i == 2:
    pass  
    print(i)

#Output: 0 1 2 3 4

for i in range(5):
    if i == 2:
        continue  
    print(i)
# Output: 0 1 3 4
 '''

'''
a = ["shirt", "sock", "pants", "sock", "towel"]
b = []
for i in a:
    if i == "sock":
        continue
    else:
        print(f"Washing {i}")
b.append("socks")
print(f"Washing {b}")
print(f" {b}")

'''

'''
for i in range(1, 100):
    if i%2==0:
        print( f"even number {i}") 
    else:
        continue
        
'''
'''
    n = int(input())
    li=[]
    if 1<=n<=20:
        for i in range (n):
            li.append(i)
            print(i**2) # i need to print every number square in a new line so i didn't use list in the print 
'''
'''
def is_leap(year):
    leap = False
    if 1900<=year<=10**5:
        if  year%4==0:
            leap= True
    return leap

''''''
# right code
year = int(input())
print(is_leap(year))
def is_leap(year):
    leap = False
    if 1900<=year<=10**5:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    leap= True
                else:
                    leap= False
            else:
                leap= True
        else:
            leap=False            
    return leap

year = int(input())
print(is_leap(year))
'''
'''
X=5;

while X>0:

      X=X-1;

      print(X)

'''
'''      
# Lambda function with if, elif, and else
# Example: Check if a number is positive, negative, or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))   
print(n(-3))  
print(n(0))


'''
'''
#def vs lambda
# Function to calculate the area of square
# Using lambda
sq = lambda x: x ** 2
print(sq(3))

# Using def
def sqdef(x):
    return x ** 2
print(sqdef(3))
'''
'''
print('+'*100)

li=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2==0,li)))

print('+'*100)

print (list(map(lambda x: x**2,li)))

print('+'*100)
 
print(prod(li)) # multiply all elements in the list 
print(reduce(lambda x,y:x*y,li))# lambda to multiply all elements in the list
'''
