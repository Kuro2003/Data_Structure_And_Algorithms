from ast import walk
from cgitb import reset
from telnetlib import WILL
from winreg import QueryInfoKey


class Empty(Exception):
    pass

class ArrayQueue:
    """ FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10
    def __init__(self):
        """ Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        """ Return True if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """ Return (but do not remove) the element at the front of the queue.
        
        Raise Empty exception if the qieie is empty."""
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._data[self._front]

    def dequeue(self):
        """ Remove and return the firse element of the queue
        
        Raise Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty("Queue is Empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

    def enqueue(self,e):
        """ Add an element to the back of queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    
    def _resize(self,cap):
        """ Resize to a new list of capacity"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(self._data)
        self._front = 0
if __name__ == '__main__':
    queue = ArrayQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue._data)
