# from math import ceil, floor, trunc


# a=12.3456
# b=(a)
# # print(b)
# list=[1,2,3,4,5]
# # here we use the shallow copy method to both has the different memory address. using the "copy.copy".
# # list1=copy(list)

# help(copy.copy)
# print("list  : ",id(list))
# print("list1 : ",id(list1))
def uppers(z):
    for i in range(0,len(z)):
        print("i : ",i)
        if i%2==0:
            return z[i].upper()
        else:
            # uppers(z)
            i=i+1

txt = "arfa is a good gril"
result=uppers(txt)
print(result)