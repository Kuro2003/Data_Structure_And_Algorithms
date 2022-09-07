def selectionsort(a,n):
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx],a[i]

a = [1,2,3,5,6,0,12,42,23,65]
print(a)
selectionsort(a,len(a))
print(a)