""" Method 1: Implementation of QuickSort using the end element as a pivot:"""
# Function to find partition position
# def partition(arr,low,high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low,high):
#         if arr[j] < pivot:
#             i += 1
#             arr[i],arr[j] = arr[j],arr[i]
#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return i +1
# # Function to ferform quicksort
# def quicksort(arr,low,high):
#     if low < high :
#         pi = partition(arr,low,high)
#         quicksort(arr,low,pi-1)
#         quicksort(arr,pi+1, high)

""" Method 2: Implementation of QuickSort using the first element as a pivot:"""
# Function to find partition position
# Function to find the partition position
def partition(arr, l, h):
    low, high = l, h
    if l != h and l < h:
        # Choose the leftmost element as pivot
        pivot = arr[l]
        low = low+1
    # Traverse through all elements
    # compare each element with pivot
    while low <= high:
        if arr[high] < pivot and arr[low] > pivot:
            arr[high], arr[low] = arr[low], arr[high]
        if not arr[low] > pivot:
            low += 1
        if not arr[high] < pivot:
            high -= 1
    arr[l], arr[high] = arr[high], arr[l]
    # Return the position from where partition is done
    return high
    

# Function to perform quicksort
def quicksort(arr,low,high):
    if low < high :
        pi = partition(arr,low,high)
        quicksort(arr,low,pi)
        quicksort(arr,pi+1, high)

# arr = [1,2,3,5,6,0,12,42,23,65]
arr = [6,7,2,9,3,5]
print("Mang khoi tao:\n",arr)
quicksort(arr,0,len(arr)-1)
print("Mang sau khi sap xep:\n",arr)
