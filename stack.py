
def checkOp(op):
    if op == '+' or op == '-' or op == '*' or op == '/':
        return True
    return False

def cal(s):
    s = s.split(' ')
    i = 0
    st = []
    t = 0
    while(len(s) != i):
        if checkOp(s[i]):
            b = int(st.pop())
            a = int(st.pop())
            if s[i] == '+':
                t = a + b
            elif s[i] == '-':
                t = a - b
            elif s[i] == '*':
                t = a * b
            else:
                t = a / b

            st.append(t)
        else:
            st.append(s[i])
        i += 1
    return t
def main():
    s = '5 10 + 2 * 3 /'
    res = cal(s)
    print(res)
main()
