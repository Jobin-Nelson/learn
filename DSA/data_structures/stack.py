from collections import deque

# basic class represenation in python 
class stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self, val):
        return self.container.pop()

class queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self, val):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
    
if __name__ == '__main__':
    stack = deque()
    stack.append('cnn')
    stack.append('cnn/world')
    stack.append('cnn/india')
    stack.append('cnn/china')
    print(stack)
    print('Popped last element of stack: ',stack.pop())

    q = deque()
    q.appendleft(5)
    q.appendleft(6)
    q.appendleft(8)
    q.appendleft(9)
    print(q)
    print('Popped last element of queue: ', q.pop())
