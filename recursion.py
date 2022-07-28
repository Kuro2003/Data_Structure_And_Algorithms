def show_menu():
    print("\n                        Menu                        ")
    print("-----------------------------------------------------")
    print("| Lesson 1: calculate n!                            |")
    print("| Lesson 2: Fibo                                    |")
    print("| Lesson 3: C(n,0) = 1, C(n,n) = 1 n>=0             |")
    print("|           C(n,k)= C(n-1,k-1) + C(n-1,k) 0<k<n     |")
    print("| Lesson 4: Tower of Hanoi math problem             |")
    print("|             h1 = 1                                |")
    print("|             h(n) = 2h(n-1) + 1                    |")
    print("| Lessson 5: Reverse Array                          |")
    print("| Lessson 6: Drawing an English Ruler               |")
    print("| Enter 0 : Exit                                    |")
    print("----------------------------------------------------")

def cal_les_1(n):
    if n == 0:
        return 1
    return n * cal_les_1(n-1)

def les_1():
    """ Lesson 1: calculate n! """
    n = int(input("Enter n = "))
    print(cal_les_1(n))

def cal_les_2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return cal_les_2(n-1) + cal_les_2(n-2)

def les_2():
    """ Lesson 2: Fibo """
    n = int(input("Enter n = "))
    print(cal_les_2(n))

def cal_les_3(n,k):
    if k == 0 or k == n:
        return 1
    return cal_les_3(n-1,k-1) + cal_les_3(n-1,k)

def les_3():
    """ Lesson 3: C(n,0) = 1, C(n,n) = 1 n>=0 
        C(n,k)= C(n-1,k-1) + C(n-1,k) 0<k<n """
    n = int(input("Enter n = "))
    k = int(input("Enter k (0 <= k <= n) = "))
    print(cal_les_3(n,k))

def cal_les_4(n):
    if n == 1:
        return 1
    return 2 * cal_les_4(n-1) + 1
    
def les_4():
    """ Lesson 4: Tower of Hanoi math problem
        h1 = 1
        h(n) = 2h(n-1) + 1 """
    n = int(input("Enter n = "))
    print("least number of moves is: " + str(cal_les_4(n)))
    
#method 1
def cal_les_5_med1(a,i,j):
    if i < j:
        a[i] , a[j-1] = a[j-1], a[i]
        return cal_les_5_med1(a,i+1,j-1)
    else:
        return 

def cal_les_5_med2(a):
    if len(a) == 1:
        return [a[0]]
    else:
        return [a[-1]] + cal_les_5_med2(a[:-1])

def les_5():
    """ Lessson 5: Reverse Array"""
    a = [1,2,3,4,5,6,7,8,9]
    i = 0
    j = len(a)
    print(a[-1])
    # cal_les_5_med1(a,i,j)
    print(cal_les_5_med2(a))

def draw_line(tick_length,tick_label=''):
    """ Draw one line with given tick length (followed by optional label) """
    line = '-' * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches,major_length):
    """ Draw English ruler with given nuber of inches, major tick length."""
    draw_line(major_length,'0')
    for j in range(1,1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length,str(j))

def les_6():
    num_inches = int(input("Enter num inches: "))
    major_length = int(input("Enter major length: "))
    draw_ruler(num_inches,major_length)

def main():
    while True:
        show_menu()
        user_input = int(input("Enter lesson you want: "))
        if user_input == 1:
            les_1()
        elif user_input == 2:
            les_2()
        elif user_input == 3:
            les_3()
        elif user_input == 4:
            les_4()
        elif user_input == 5:
            les_5()
        elif user_input == 6:
            les_6()
        elif user_input == 0:
            break

main()