class Empty(Exception):
    pass

class LinkedStack:
    """ LIFO Stack implement using a singly linked list  for storage."""

    #------------------- create node -----------------------
    class _Node:
        __slot__ = '_element','_next' 
        def __init__(self,element,next):
            self._element = element
            self._next = next
    
    #----------------------- Stack method ------------------

    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        """ Return number of element in the stack """
        return self._size
    def is_empty(self):
        return self._size == 0
    def push(self,e):
        self._head = self._Node(e,self._head)
        self._size += 1
    def top(self):
        if self.is_empty:
            raise Empty("Stack is empty")
        return self._head._element 

    def pop(self):
        if self.is_empty:
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

if __name__ == "__main__":
    l = LinkedStack()
    l.push(2)
    l.push(2)
    print(l.top())
    