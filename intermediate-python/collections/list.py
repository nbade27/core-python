# Lists: ordered, mutable, allows duplicate elements

myList = [4, 3, 1, -1, -5, 10]
print(myList)

new_list = sorted(myList)
print(new_list)

myList1 = [0] * 5;
print(myList1)

myList2 = myList + myList1

print(myList2)

# slicing the list
a = myList2[1:5]
print(a)

# step index
# printing every second indexed element
a = myList2[::2] 
print(a)

#  copying the list
list_frut = ["banana", "cherry", "apple"]
# Three ways to copy
# 1
list_copy = list_frut
print(list_copy)

# 2
list_copy = list(list_frut)
print(list_copy)

# 3
list_copy = list_frut[:]
print(list_copy)


# copying with squared numbers in one line
num_list = [1, 2, 3,4, 5,6,7]
square_list = [num* num for num in num_list]
print(square_list)