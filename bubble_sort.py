

# Bubble Sort 

def bubbleSort(arr):

    # Using two for loops 
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):

            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1],arr[j]


data = [-2, 45, 0, 11, -9]
print(data)

bubbleSort(data)
print(data)