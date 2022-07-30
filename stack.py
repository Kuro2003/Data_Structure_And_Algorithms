class Empty(Exception):
    pass
class ArrayStack:
    def __init__(self):
        """ Create an empty stack."""
        self._data = []

    def __len__(self):
        """ Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """ Return True if the stack is empty """
        return len(self._data) == 0

    def push(self,e):
        """ Add element e to the top of the stack"""
        self._data.append(e)
    
    def pop(self):
        """ Remove and return the element from the top of the stack
            Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def top(self):
        """ Return (but do not remove) the element at the top of the stack
            Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

def checkOp(op):
    if op == '+' or op == '-' or op == '*' or op == '/':
        return True
    return False

def cal(s):
    s = s.split(' ')
    i = 0
    st = ArrayStack()
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

            st.push(t)
        else:
            st.push(s[i])
        i += 1
    return t

def main():
    s = '5 10 + 2 * 3 /'
    res = cal(s)
    print(res)
main()
