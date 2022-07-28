def cal_les_1(n):
    if n == 0:
        return 1
    return n * cal_les_1(n-1)

def cal_les_2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return cal_les_2(n-1) + cal_les_2(n-2)

def cal_les_3(n,k):
    if k == 0 or k == n:
        return 1
    return cal_les_3(n-1,k-1) + cal_les_3(n-1,k)

def cal_les_4(n):
    if n == 1:
        return 1
    return 2 * cal_les_4(n-1) + 1

def main():
    """ Lesson 1: calculate n! """
    # n = int(input("Enter n = "))
    # print(cal_les_1(n))

    """ Lesson 2: Fibo """
    # n = int(input("Enter n = "))
    # print(cal_les_2(n))

    """ Lesson 3: C(n,0) = 1, C(n,n) = 1 n>=0 
        C(n,k)= C(n-1,k-1) + C(n-1,k) 0<k<n """
    # n = int(input("Enter n = "))
    # k = int(input("Enter k (0 <= k <= n) = "))
    # print(cal_les_3(n,k))

    """ Lesson 4: Tower of Hanoi math problem
        h1 = 1
        h(n) = 2h(n-1) + 1 """
    n = int(input("Enter n = "))
    print("least number of moves is: " + str(cal_les_4(n)))


main()