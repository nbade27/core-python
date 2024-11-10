# from math import *
#
#
# # print("   /|")
# # print("  / |")
# # print(" /  |")
# # print("/___|")
#
# # variables and data types in python
#
# # If you want to change the name in below code you need to manually change the name.
#
# # character_name = "Tom"
# # character_age = "25"
# # print("there was a man named "+character_name+", ")
# # print("he was "+character_age+" years old")
# # print("He really liked the name "+character_name+", ")
# # print("but didn't like being "+character_age)
#
# # there are mainly three types of data types in python
# #  string,number,boolean
# #  it will always start with capital letter eg : False,True
# # working with strings
# print("Giraffe\nAcademy")
#
# print("Giraffe\" Academy")
#
#
#
#
# phrase = "Giraffe Academy"
# # converting into upper case
# print(phrase.upper())
# print(phrase.lower())
# print(phrase.isupper())
# print(len(phrase))
# print(phrase[3])
# print(phrase.index("G"))
# print(phrase.index("Acad"))
# # below line throws error because it doesn't contain character z
# # print(phrase.index("z"))
# print(phrase.replace("Giraffe","Elephant"))
#
# # numbers in python
# print(2)
# print(2.098748)
# print(3 * (5+8))
# print(3 * 4 + 5) # 17
# #  below statement will give remainder
# print(10%3)
# number = 5
# print(str(number)+ " is my favourite number")
#
# # print(number + " is my favourite number")
# number = -5
# print(abs(number))
# print(pow(number,4))
# print(max(1,2,3,4,5,6,7,8,9,10))
# print(min(1,2,3,4,5,6,7,8,9,10))
# print(round(3.4))
# print(round(3.6))
#
# print("floor function -> "+str(floor(3.6)))
# print("ceil function -> "+str(ceil(3.4)))
# print(sqrt(36))
#
# # reading runtime values from user
# name = input("Enter your name : ")
# age = input("Enter your age : ")
# print("Hello " + name + "! you are "+age)
#
# Calculator APP
# num1 = input("Enter a number : ")
# num2 = input("Enter another number : ")
# by default when python reading anything from user it will treat as String. Irrespective of users entered data type
# result = int(num1) + int(num2)
# result = float(num1) + float(num2)
# int() function will always looking for a whole number
#  we cna use float() as alternative for integer
# print(result)

# Mad Libs Game
# print("Welcome to mad libs game")
# color = input("Enter color : ")
# plural_noun = input("Enter plural noun : ")
# celebrity = input("Enter celebrity : ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# Lists in python
friends = ["Siro", "Sindoor", "Sampath", "Lavanya", "Murali", "KP"]
# print(friends[3])
#  you can also use negative numbers as index if you need to count from back
# print(friends[-2])
# the index of last element is -1
# if you want to get all elements starting from 2nd position then we can use like below
# print(friends[2:])
# if you want to get a portion of it you can do it by specifying them like below
# but this won't select 3rd index, but it will select before element of it.
# print(friends[1:3])
#  List functions
friends.append(["Jacob", "Teja"])
# ['Siro', 'Sindoor', 'Sampath', 'Lavanya', 'Murali', 'KP', ['Jacob', 'Teja']]
# friends.append("Jacob")
# print(friends)
# friends.insert(4,"Teja")
# print(friends)
friends.remove(["Jacob", "Teja"])
# we can remove array inside array or an string element in list
print(friends)
# we can clear the list by using method clear()
# friends.clear()
print(friends)
# pop() method is used to get the last element in the list like stack datastructure
# it also removes the elements inside of it.
last_object = friends.pop()
print(last_object)
last_object = friends.pop()
print(last_object)
print(friends)
# to check the specific element in the list
print(friends.index("Sindoor"))
# to get count of number of repeated elements
print(friends.count("Sindoor"))
print(friends.append("Sindoor"))
print(friends.count("Sindoor"))  # this will give 2 count because Sindoor is two times in the list.
# friends.sort()
print(friends)
friends.reverse()

print(friends)
friends2 = friends
print(friends2)
coordinates = (4, 5)
print(coordinates)
# we can access the elements in a tuple using tuple_name[<index>]
print(coordinates[1])
# coordinates[1]=10
atuple = (100,)
print(atuple * 2)

age_value = 17
if age_value >= 18:
    print("you are major")
else:
    print("You are minor")

is_male = False
is_tall = False
if is_male and is_tall:
    print("you are a tall male")
elif is_tall and not (is_male):
    print("you are tall but not male")
elif not (is_tall) and is_male:
    print("You are male but not tall")
else:
    print("you are eighter not male not tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(500, 666666, 999))
