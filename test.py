def recur(n,s):
    if n == 0:
        print(s)
    else:
        for i in range(2):
            recur(n-1,s + str(i))
s = ""
n = int(input())
recur(n,s)