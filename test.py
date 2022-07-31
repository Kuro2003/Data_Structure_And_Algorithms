import re


class Empty(Exception):
    pass

class Stack:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0
    
    def push(self,e):
        self._data.append(e)
    
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data.pop()
    
    def top(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data[-1]
    
def checkOp(op):
    return op == '+' or op == '-' or op == '*' or op == '/'
    
def cal(s):
    s = s.split(' ')
    stack = Stack()
    i = 0 
    while len(s) != i:
        if checkOp(s[i]):
            b = int(stack.pop())
            a = int(stack.pop())
            if s[i] == '+' :
                res = a + b
            elif s[i] == '-':
                res = a - b
            elif s[i] == '*':
                res = a * b
            else:
                res = a / b
            stack.push(res)
        else:
            stack.push(s[i])
        i += 1
    return res

if __name__ == '__main__':
    s = "5 2 + 8 3 - * 4 /"
    print(cal(s))
    s1 = [4,5]
    s2 = [6,7,8,9]
    print(s2 + s1)