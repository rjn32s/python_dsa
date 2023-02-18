

def mergeSort(arr):

    if len(arr) > 1:
        r = len(arr)//2
        L = arr[:r]
        M = arr[r:]

        mergeSort(L)
        mergeSort(M)


        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = M[j]
                j+=1
            k+=1
        
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(M):
            arr[k] = M[j]
            j+=1
            k+=1

    
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10,]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)