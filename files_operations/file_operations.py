# while dealing with files
# we can open them in two ways 1. Read 2. Write modes
# We need to pass as second arguments r , w , a - append to file, r+ read and write
employee_file = open("employees.txt", "r")
print(employee_file.read())
# employee_file.close()
print(employee_file.read())
# if we close the file we are unable to read the file without opening it
employee_file = open("employees.txt","r")
print(employee_file.read())
employee_file.close()
# we can check the access of the file by using function
# employee_file = open("employees.txt","w")
# # below line will give false because it is in writable mode
# # print(employee_file.readable())

employee_file = open("employees.txt","r")
# below line will give false because it is in writable mode
# print(employee_file.readable())
# below line will give false because it is in writable mode
# print(employee_file.readline())
# print(employee_file.read())
# print(employee_file.read())
employee_file.close()


# now we are adding some content to the file
employee_file = open("employees.txt","a")
# employee_file.write("Timothy - Software Engineer")
employee_file.close()

employee_file = open("employees.txt","a")
# print(employee_file.read())
# to add elements with new line you need to use \n to the string
employee_file.write("\n Timothy - Software Engineer")
employee_file = open("employees.txt","r")

print(employee_file.read())

"""
    The argument with w indicates that it will override the all content in the file.    
"""
# employee_file = open("employees.txt","w")

# print(employee_file.write("Hello world!!!"))
# employee_file.close()

# employee_file = open("employees.txt","r")

# print(employee_file.read())

"""
we can write html files with files.

"""

employee_file = open("employees.html","w")

print(employee_file.write("<p>Hello world!!!<p>"))
employee_file.close()

