def heapify(arr,n,i):

    # Build Heap 
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l<n and arr[largest] < arr[r]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i] , arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def heapSirt(arr):
    n = len(arr)

    for i in range(n//2 , -1 , -1):
        heapify(arr,n,i)
    for i in range(n-1 , 0 , -1):
        heapify(arr,n,i)
    
