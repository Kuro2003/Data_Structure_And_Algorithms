class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data,end= ' ')
        if self.right:
            self.right.PrintTree()

if __name__ == '__main__':
    n = int(input("Enter number node: "))
    root = Node(30)
    root.insert(15)
    root.insert(40)
    root.insert(35)
    root.insert(12)
    root.insert(20)
    root.PrintTree()