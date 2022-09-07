def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [1,2,3,5,6,0,12,42,23,65]
print("Mang khoi tao:\n",arr)
bubblesort(arr)
print("Mang sau khi sap xep:")
print(arr)