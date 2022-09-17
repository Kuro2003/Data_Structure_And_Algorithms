""" Method 1: Implementation of QuickSort using the end element as a pivot:"""
# Function to find partition position
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],pivot = pivot,arr[i+1]
    return i +1
# Function to ferform quicksort
def quicksort(arr,low,high):
    if low < high :
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1, high)

arr = [1,2,3,5,6,0,12,42,23,65]
print("Mang khoi tao:\n",arr)
quicksort(arr,0,len(arr)-1)
print("Mang sau khi sap xep:\n",arr)
