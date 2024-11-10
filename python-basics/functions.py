"""
function should be declared with def keyword in python
in its definition it should end with colon
python will follow indentation so the code inside of it will always follow indentation after tab space

return statement : we can return any datatype in python

"""
def say_hi(user_name,age):
    print("Hello " + user_name + ", you are " + str(age))

say_hi("Naga",25)


def cube(number):
    return number * number * number

print(cube(99))