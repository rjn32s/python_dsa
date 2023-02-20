import time

def countingSort(arr):

    size = len(arr)
    output = [0]*size


    count = [0]*10
    
    for i in range(0,size):
        count[arr[i]] +=1
    

    for i in range(1,10):
        print(f"The count[i]:{count[i-1]} and the cummulative Sum :{count[i]}   ")
        count[i] += count[i-1]
        #time.sleep(2)

    i = size-1

    while i>=0:
        output[count[arr[i]]-1] =arr[i]
        count[arr[i]] -=1
        i -=1
    for i in range(0 ,size):
        arr[i] = output[i]

data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)

