'''
Created Date: 2022-12-16
Qn: Implement a first in first out (FIFO) queue using only two stacks. The
    implemented queue should support all the functions of a normal queue 
    (push, peek, pop, and empty).

    Implement the MyQueue class:

        - void push(int x) Pushes element x to the back of the queue. 
        - int pop() Removes the element from the front of the queue and returns
          it. 
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
    - use 2 stacks
    - when popping append to second stack and pop and append it back to the
      first stack
'''
class MyQueue:
    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.aux.append(self.stack.pop())
        res = self.aux.pop()
        while self.aux:
            self.stack.append(self.aux.pop())
        return res

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack

if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())
    print(q.pop())
    print(q.empty())
