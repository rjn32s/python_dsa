def bubbleSort(arr):

    swapped = False
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                #swapp
                arr[j],arr[j+1]= arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)

