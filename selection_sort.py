def selectionSort(arr):
    size = len(arr)
    for step in range(size):
        min_idx = step

        for i in range(step+1,size):
            if arr[i] < arr[min_idx]:
                min_idx =i
        arr[step],arr[min_idx] = arr[min_idx],arr[step]

data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data)#, size)
print('Sorted Array in Ascending Order:')
print(data)
       