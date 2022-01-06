from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqeue(self,val):
        self.buffer.appendleft(val)
    def deqeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) ==0
    def size(self):
        return len(self.buffer)
    