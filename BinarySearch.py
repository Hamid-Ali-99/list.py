# def binarySearch(array, x, low, high):

#     if high >= low:

#         mid = low + (high - low)//2

#         # If found at mid, then return it
#         if array[mid] == x:
#             return mid

#         # Search the left half
#         elif array[mid] > x:
#             return binarySearch(array, x, low, mid-1)

#         # Search the right half
#         else:
#             return binarySearch(array, x, mid + 1, high)

#     else:
#         return -1


# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4

# result = binarySearch(array, x, 0, len(array)-1)

# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")




def BinarySearch(arr,x,low,high):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return BinarySearch(arr,x,low,high-1)
        else:
            return BinarySearch(arr,x,mid+1,high)
    else:
        return -1

arr=sorted([1,2,3,6,7,9,0,8])
x=8
result=BinarySearch(arr,x,0,len(arr)-1)
if result==-1:
    print("The Number is not Found : ?")
else:
    print("The Number is Found on that Index : ",str(result))