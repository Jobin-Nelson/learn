"""
Created Date: 2024-09-30
Qn: Design a stack that supports increment operations on its elements.

    Implement the CustomStack class:

    - CustomStack(int maxSize) Initializes the object with maxSize which is the
      maximum number of elements in the stack. 
    - void push(int x) Adds x to the top of the stack if the stack has not
      reached the maxSize. 
    - int pop() Pops and returns the top of the stack or -1 if the stack is
      empty. 
    - void inc(int k, int val) Increments the bottom k elements of the stack by
      val. If there are less than k elements in the stack, increment all the
      elements in the stack.
Link: https://leetcode.com/problems/design-a-stack-with-increment-operation/
Notes:
    - use two stacks
"""


class CustomStack:
    def __init__(self, maxsize: int):
        self.arr = [0] * maxsize
        self.inc = [0] * maxsize
        self.tail = -1
        self.size = 0
        self.capacity = maxsize

    def push(self, x: int) -> None:
        if self.size < self.capacity:
            self.tail += 1
            self.arr[self.tail] = x
            self.size += 1

    def pop(self) -> int:
        if self.size > 0:
            res = self.arr[self.tail] + self.inc[self.tail]
            if self.tail > 0:
                self.inc[self.tail - 1] += self.inc[self.tail]
            self.inc[self.tail] = 0
            self.tail -= 1
            self.size -= 1
            return res
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.tail >= 0:
            ind = min(self.tail, k - 1)
            self.inc[ind] += val


if __name__ == '__main__':
    cs1 = CustomStack(3)
    print(cs1.push(1))
    print(cs1.push(2))
    print(cs1.pop())
    print(cs1.push(2))
    print(cs1.push(3))
    print(cs1.push(4))
    print(cs1.increment(5, 100))
    print(cs1.increment(2, 100))
    print(cs1.pop())
    print(cs1.pop())
    print(cs1.pop())
    print(cs1.pop())
