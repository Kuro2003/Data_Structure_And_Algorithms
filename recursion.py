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

def main():
    """ Lesson 1: calculate n! """
    # n = int(input("Enter n = "))
    # print(cal_les_1(n))

    """ Lesson 2: Fibo """
    n = int(input("Enter n = "))
    print(cal_les_2(n))

main()