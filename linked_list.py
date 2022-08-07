class Node:
    def __init__(self,element,next):
        self._element = element
        self._next = next

class LinkedStack:
    """ Initial List"""
    def __init__(self):
        self._head = 0
        self._size = 0

    """ Add element(e) at the head"""
    def push(self,e):
        self._head = Node(e,self._head)
        self._size += 1
    
    """ Get element head without remove"""
    def top(self):
        if self._size == 0:
            print("Stack is empty")
            return
        return self._head._element
    
    """ Get element head and remove """
    def pop(self):
        if self._size == 0:
            print("Stack is empty")
            return

        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    
    """ Add element(e) at the end"""
    def insert_at_end(self,e):
        if self._head  == None:
            self.push(e) 
            return
        
        itr =  self._head
        while itr._next:
            itr = itr._next
        
        itr._next = Node(e,None)
        self._size += 1

    """ Remove at the end"""
    def remove_at_end(self):
        # Check empty list
        if self._size == 0:
            return 
        count = 0
        itr = self._head
        while itr:
            if self._size - 2 == count:
                itr._next = itr._next._next
                self._size -= 1
                break
            itr = itr._next
            count += 1

    """ Add element(e) at index"""
    def insert_at(self,e,index):
        itr = self._head

        # Check index == 0
        if index == self._size:
            self.insert_at_end(e)
            return
        
        # Check index == len(list)
        if index == 0:
            self.push(e)
            return 
        
        # else
        count = 0
        while itr:
            count += 1
            if count == index - 1:
                node = Node(e,itr._next)
                itr._next = node
                break
            itr = itr._next
        self._size += 1

    # Remove at index
    def remove_at(self,index):
        # Check index == 0
        if index == 0:
            self._head = self._head._next
            return
        
        # Check index == size
        if index == self._size:
            self.remove_at_end()
            return

        # else
        count = 0
        itr = self._head
        while itr:
            if index - 1 == count:
                itr._next = itr._next._next
                self._size -= 1
                break
            itr = itr._next
            count += 1
        self._size -= 1

    """ Print list"""
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

    print("insert 69")
    llist.insert_at(69,0)
    llist.print()

    print("insert 23")
    llist.insert_at_end(23)
    llist.print()

    print("pop")
    print(llist.pop())
    llist.print()

    print("remove")
    llist.remove_at(4)
    llist.print()



