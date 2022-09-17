def mergesort(a):
    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i +=1 
            else:
                a[k] = R[j]
                j += 1
            k += 1
        
        if i < len(L):
            a[k] = L[i]
            k += 1
            i += 1
        
        if j < len(R):
            a[k] = R[j]
            k += 1
            j += 1

if __name__ == '__main__':
    arr = [1,2,3,5,6,0,12,42,23,65]
    print("Mang khoi tao:\n",arr)
    mergesort(arr)
    print("Mang sau khi sap xep:\n",arr)