import sys

my_list = [0,1,2, "hello", True]
my_tuple = (0,1,2, "hello", True)
print(sys.getsizeof(my_list), bytes) 
print(sys.getsizeof(my_tuple), bytes)

#list  104 <class 'bytes'>
#tuple  80 <class 'bytes'>

