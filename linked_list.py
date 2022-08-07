class Node:
    def __init__(self,element,next):
        self._element = element
        self._next = next

class LinkedStack:
    def __init__(self):
        self._head = 0
        self._size = 0

    def push(self,e):
        self._head = Node(e,self._head)
        self._size += 1
    
    def top(self):
        if self._size == 0:
            print("Stack is empty")
        return self._head._element
    
    def pop(self):
        if self._size == 0:
            print("Stack is empty")
        
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    
    def insert_at_end(self,e):
        if self._head  == None:
            self._head = Node(e,None)
            self._size += 1
            return
        
        itr =  self._head
        while itr._next:
            itr = itr._next
        
        itr._next = Node(e,None)
        self._size += 1
    
    def insert_at(self,e,index):
        itr = self._head
        count = 0
        while itr:
            count += 1
            if count == index - 1:
                node = Node(e,itr._next)
                itr._next = node
                break
            itr = itr._next
        self._size += 1

    def print(self):
        if self._head is None:
            print("Stack is empty")
            return
        itr = self._head
        llstr = ''
        while itr:
            llstr += str(itr._element)+' --> ' if itr._next else str(itr._element)
            itr = itr._next
        print(llstr)

if __name__ == '__main__':
    llist = LinkedStack()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.print()

    llist.insert_at(69,3)
    llist.print()

    llist.insert_at_end(23)
    llist.print()

    print(llist.pop())
    llist.print()



