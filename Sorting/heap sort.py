def heapify(arr,n,i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def heapsort(arr):
    n = len(arr)
    # build max heap
    for i in range(n//2 -1,-1,-1):
        heapify(arr,n,i)
    
    for i in range(n-1,-1,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

if __name__ =='__main__':
    arr = [1,2,3,5,6,0,25,12]
    print("Mang khoi tao:\n",arr)
    heapsort(arr)
    print("Mang sau khi sap xep:\n",arr)