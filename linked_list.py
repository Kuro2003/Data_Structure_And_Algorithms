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
            print("Stack is empty")
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
        # Check empty list
        if self._size == 0:
            self.push(e)
            self._size += 1
            return

        # Check index == 0
        if index == self._size:
            self.insert_at_end(e)
            return
        
        # Check index == len(list)
        if index == 0:
            self.push(e)
            return 
        
        # else
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

    # Remove at index
    def remove_at(self,index):
        # Check list empty
        if self._size == 0:
            print("Stack is empty")
            return

        # Check index == 0
        if index == 0:
            self._head = self._head._next
            self -= 1
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
    print("\t\t-------------------Menu----------------------")
    print("\t\t| 1.Print list                              |")
    print("\t\t| 2.insert at index head                    |")
    print("\t\t| 3.insert at index end                     |")
    print("\t\t| 4.insert at index k                       |")
    print("\t\t| 5.remove at index head                    |")
    print("\t\t| 6.remove at index end                     |")
    print("\t\t| 7.remove at index k                       |")
    print("\t\t| 0. Exit                                   |")
    print("\t\t---------------------------------------------")

def check(promp,begin,end):
    while True:
        option = int(input(promp))
        if option < begin or option > end:
            print("You wrong enter")
        else:
            return option
        

if __name__ == '__main__':
    llist = LinkedStack()
    while True:
        menu()
        promp = "Enter option you want: "
        option = check(promp,0,8)
        
        # Print list
        if option == 1:
            llist.print()

        # insert at index head
        elif option == 2:
            k = int(input("Enter data: "))
            llist.push(k)
            os.system('cls')  
            
        # insert at index end
        elif option == 3:
            k = int(input("Enter data: "))
            llist.insert_at_end(k)
            os.system('cls')  

        # insert at data and index m
        elif option == 4:
            k = int(input("Enter data: "))
            promp = "Enter index you want insert: "
            if llist._size == 0:
                llist.push(k)
            else:
                m = check(promp,0,llist._size + 1)
                llist.insert_at(k,m)
                os.system('cls')  

        # remove at index head
        elif option == 5:
            if llist._size == 0:
                llist.pop()
            else:
                llist.pop()
                os.system('cls')  

        #remove at index end
        elif option == 6:
            if llist._size == 0:
                llist.remove_at_end()
            else:
                llist.remove_at_end()
                os.system('cls')  

        # remove at index k
        elif option == 7:
            promp = "Enter index you want remove: "
            k = check(promp,0,llist._size)
            if llist._size == 0:
                llist.remove_at(k)
            else:
                llist.remove_at(k)
                os.system('cls')  

        # Exit 
        else:
            os.system('cls')  
            break




