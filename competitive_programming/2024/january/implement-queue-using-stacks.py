"""
Created Date: 2024-01-29
Qn: Implement a first in first out (FIFO) queue using only two stacks. The
    implemented queue should support all the functions of a normal queue (push,
    peek, pop, and empty).

    Implement the MyQueue class:

        - void push(int x) Pushes element x to the back of the queue. 
        - int pop() Removes the element from the front of the queue and returns it. 
        - int peek() Returns the element at the front of the queue. 
        - boolean empty() Returns true if the queue is empty, false otherwise.

    Notes:

        - You must use only standard operations of a stack, which means only
          push to top, peek/pop from top, size, and is empty operations are
          valid. 
        - Depending on your language, the stack may not be supported natively.
          You may simulate a stack using a list or deque (double-ended queue)
          as long as you use only a stack's standard operations.
Link: https://leetcode.com/problems/implement-queue-using-stacks/
Notes:
    - use 2 stacks and rotate one over the other to achieve queue behaviour
"""
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:
        self.stack1.append(x)
    def rotate(self) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
    def pop(self) -> int:
        if not self.stack2: self.rotate()
        return self.stack2.pop()
    def peek(self) -> int:
        if not self.stack2: self.rotate()
        return self.stack2[-1]
    def empty(self) -> bool:
        if not self.stack2: self.rotate()
        return len(self.stack2) == 0
    def __str__(self) -> str:
        return f'{self.__class__.__name__}(s1: {self.stack1!r}, s2: {self.stack2!r})'
    def __repr__(self) -> str:
        return self.__str__()

if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())
    print(q.pop())
    print(q.empty())
