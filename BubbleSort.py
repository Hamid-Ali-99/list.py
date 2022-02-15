# # Bubble sort in Python
# # This code is copyed from internet.

# def bubbleSort(array):
    
#   # loop to access each array element
#   for i in range(len(array)):

#     # loop to compare array elements
#     for j in range(0, len(array) - i - 1):
#       print(j)

#       # compare two adjacent elements
#       # change > to < to sort in descending order
#       if array[j] > array[j + 1]:
#         # swapping elements if elements
#         # are not in the intended order
#         temp = array[j]
#         array[j] = array[j+1]
#         array[j+1] = temp


# data = [-2, 45, 0, 11, -9]

# bubbleSort(data)

# print('Sorted Array in Ascending Order:',data)

def BubbleSort(arr):
    for i in range(len(arr)): 
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
              temp=arr[j]
              arr[j]=arr[j+1]
              arr[j+1]=temp

arr=[-12,0,12,11,-10,1]
BubbleSort(arr)
print(arr)