# collectins of key value pairs
myDict = {"name":"Max", "age": 28, "city":"new york"}
print(myDict)

# using dict keyword!
myDict2 = dict(name="Max", age=28, city= "Boston")
print(myDict2)

# gettign value
value = myDict2["name"]
print(value)

# adding or updating key values
myDict2["email"]= "max@xyz.com"
print(myDict2)

# delete items
del myDict2["email"]
print(myDict2)

# also we can use pop method or popitem method
myDict2.pop("age")
print(myDict2)

myDict2.popitem()
print(myDict2)

# conditional statements in dicts
if "name" in myDict2:
    print(myDict2["name"])
else:
    print("name is not available in the dict!!!")


# we can also use try except statements
try: 
    print(myDict2["lname"])
except:
    print("error")

# iterating the dicts
for key, value in myDict2.items():
    print(key, value)
    
# copying dicts
mydict_copy = myDict2
print(mydict_copy)
# mydict_copy["email"] = "max@xyz.com"
# print(myDict2)

# if we change the copied dict the original dict will also wil be changed!
# to avoid this you need to use the .copy function
mydict_copy = myDict2.copy()
print(mydict_copy)
mydict_copy["email"] = "max@xyz.com"
print(mydict_copy)
print(myDict2)

# updating the existing with new dict
myDict3 = {"name": "mary", "age":27}
# These values will be overriden by the new dict
myDict2.update(myDict3)
print(myDict2)

# we can use tuple as key in the dict
myDict4 = {3:9, 4:16, 5:25}
print(myDict4)

myTuple = (8,7)
myDict5 = {myTuple: 15}
print(myDict5)