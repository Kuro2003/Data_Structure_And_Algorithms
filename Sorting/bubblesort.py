a = [1,2,3,5,6,0,12,42,23,65]
def bubblesort(a,n):
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1] ,a[j]
print(a)
bubblesort(a,len(a))
print(a)