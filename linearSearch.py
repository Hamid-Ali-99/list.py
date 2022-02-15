# # Linear Search in Python

# def linearSearch(arr, n, x):
#     #This code is copyed from the internet.
#     # Going through arr sequencially
#     for i in range(0, n):
#         if (arr[i] == x):
#             return i
#     return -1


# arr = [2, 4, 0, 1, 9]
# x = 6
# n = len(arr)
# result = linearSearch(arr, n, x)
# if(result == -1):
#     print("Element not found")
# else:
#     print("Element found at index: ", result)



def linearSearch(arr,n,x):
    for i in range(0,n):
        if(arr[i]==x):
            return i
    return -1

arr=[2,0,1,34,51,23,32]
n=len(arr)
x=0
result=linearSearch(arr,n,x)
if(result==-1):
    print("The Number Not found:")
else:
    print("The Number is Found on index :",result)