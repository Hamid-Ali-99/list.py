from math import ceil, floor, trunc


a=12.3456
b=(a)
# print(b)
list=[1,2,3,4,5]
# here we use the shallow copy method to both has the different memory address. using the "copy.copy".
# list1=copy(list)

help(copy.copy)
print("list  : ",id(list))
# print("list1 : ",id(list1))