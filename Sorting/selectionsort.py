def selectionsort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx],arr[i]

arr = [1,2,3,5,6,0,12,42,23,65]
print("Mang khoi tao:\n",arr)
selectionsort(arr)
print("Mang sau khi sap xep:")
print(arr)