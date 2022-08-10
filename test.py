d = 0
i = 20
j = 23
k = 6
for k in range(i,j+1):
    if abs(l - int(str(l)[::-1])) % k == 0:
        d += 1
print(d)