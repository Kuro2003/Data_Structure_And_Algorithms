""" Lesson 1: calculate n! """
def cal_les_1(n):
    if n == 0:
        return 1
    return n * cal_les_1(n-1)

n = int(input("Enter n = "))
print(cal_les_1(n))