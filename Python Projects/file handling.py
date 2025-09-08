# Reading a file
f=open("G:\Study\Python\Python Projects\student-grades-project.py","r")
print(f.read())
f.close()

# Writing to a file
#there are three modes to write a file
#  1. Write mode (w) - This mode is used to write data to a file.
#  If the file already exists, it will be overwritten(trancate).
#  If the file does not exist, a new file will be created.
# *** be carfull this mode will delete all the content of the file 
#     and write the new content***

'''
fileWrite=open("G:\Study\Python\Python Projects\student-grades-project.py","w")
fileWrite.write('finally:\n\tprint("Thank you for using the student grades program.")')
fileWrite.close()'''

#  2. Append mode (a) - This mode is used to append data to the end of a file.
#  If the file does not exist, a new file will be created.  
#  *** This mode is the best for this use 
#       to append the finally block to the end of the file*** 

'''
fileWrite=open("G:\Study\Python\Python Projects\student-grades-project.py","a")
fileWrite.write('\n')
fileWrite.write('finally:\n\tprint("Thank you for using the student grades program.")')
fileWrite.close()
'''

#  3. Exclusive creation mode (x) - This mode is used to create a new file.
#  If the file already exists, an error will be raised. 

"""try:
    with open("G:\Study\Python\Python Projects\student-grades-project1.py","x") as fileWrite:
        fileWrite.write('finally:\n\tprint("Thank you for using the student grades program.")')
        fileWrite.close()
except FileExistsError:
    print("File already exists.")"""