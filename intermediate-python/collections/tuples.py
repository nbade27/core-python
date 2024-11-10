# Tuple: Ordered, immutable, allows duplicate elements
# tuple cannot be changed after creation.

myTuple = ["max", 28, "boston"]
myTuple = "max", 28, "boston"
print(myTuple)

# below line python will recognize as string
tup = ("max")
print(type(tup))

#  but below line it will recognize as tuple
tup = ("max"),
print(type(tup)) # comma will make string to a tuple

#  you can use tuple function to create a tuple from a iterable
tup = tuple(("Max", 28, "Boston"))
tup = tuple(["Max", 28, "Boston"])
print(tup)

item = tup[2]
print(item)

# changing elemets in tuple
# tup[0] = "Tim"  We cannot change elements in tuple

# iterating tuple
for x in tup:
    print(x)

if "Max" in tup:
    print("Yes")
else:
    print("No")

#  no of elelemts in tuple
print(len(tup))

# count matched elements in the tuple
print(tup.count("Max"))

# index of tuple
print(tup.index("Max"))

# getting list out of tuple
list = list(tup)
print(list)

# slicing tuple
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[:5]
b = a[::-1] # reversing the tuple
print(b)

#  seperating elemts in tuple
#  elemetns should match the left and right side elements
name, age, city = tup
print(name)
print(age)
print(city)

#  packing elemnts from tuple
my_tup = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tup
#  the elements between first and last indexes will be stored into i2
print(i1)
print(i3)
print(i2)

#  copmaring tuple and list
tuple 
    # 1. immutable - internal optimizations (good for large data )

