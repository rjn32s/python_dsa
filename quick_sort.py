
# Finction to find the partition position
def partition(arr , low, high):
    # Choose the rightmost element for the pivot
    pivot = arr[high]
    # pointer for the greatest element
    i = low -1
    
    # traverse through all elements
    # Compare each element with the pivot

    for j in range(low,high):
        if arr[j] <= pivot:
            i = i+1

            # swapping elemnt at i with element at j
            arr[i] , arr[j] = arr[j] , arr[i]
        # swapping the pivot element with the greates element 
    arr[i+1] , arr[high] = arr[high] , arr[i+1]

    return i+1

def qucikSort(arr,low, high):
    if low < high:
        pi = partition(arr,low,high)

        qucikSort(arr,low,pi-1)
        qucikSort(arr,pi+1,high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

qucikSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

