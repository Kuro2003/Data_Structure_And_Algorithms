import os
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

def menu():
    print("-------------------Menu--------------------")
    print("| 1.add node at index head                  |")
    print("| 2.add node at index end                   |")
    print("| 3.remove at index head                    |")
    print("| 4.remove at index end                     |")
    print("| 5.remove at index k                       |")
    print("| 6.insert at index head                    |")
    print("| 7.insert at index end                     |")
    print("| 8.insert at index k                       |")
    print("| 0. Exit                                   |")
    print("-------------------------------------------")

def check(promp,begin,end):
    while True:
        menu()
        option = int(input("Enter option you want: "))
        if option < begin or option > end:
            print("You wrong enter")
        else:
            return option
        os.system('cls')

if __name__ == '__main__':
    llist = LinkedStack()
    while True:
        promp = "Enter option you want: "
        option = check(promp,0,8)
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            pass
        elif option == 7:
            pass
        elif option == 8:
            pass
        else:
            break




