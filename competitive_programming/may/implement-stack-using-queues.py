'''
Qn: Implement a last-in-first-out (LIFO) stack using only two queues. 
    The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
Link: https://leetcode.com/problems/implement-stack-using-queues/
Notes:
    - use queue and popleft n-1 times and append it, return the last element
'''
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()
    def push(self, x: int) -> None:
        self.queue.append(x)
    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()
    def top(self) -> int:
        return self.queue[-1]
    def empty(self) -> bool:
        return len(self.queue) == 0

if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    print(obj.empty())
    
