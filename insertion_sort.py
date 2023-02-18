

def insertionSort(arr):


    for i ,ele in enumerate(arr):
        # key = ele
        j = i-1

        while j>=0 and ele < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = ele


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

