"""
Created Date: 2024-09-28
Qn: Design your implementation of the circular double-ended queue (deque).

    Implement the MyCircularDeque class:

    - MyCircularDeque(int k) Initializes the deque with a maximum size of k.
    - boolean insertFront() Adds an item at the front of Deque. Returns true if
      the operation is successful, or false otherwise.
    - boolean insertLast() Adds an item at the rear of Deque. Returns true if
      the operation is successful, or false otherwise.
    - boolean deleteFront() Deletes an item from the front of Deque. Returns
      true if the operation is successful, or false otherwise.
    - boolean deleteLast() Deletes an item from the rear of Deque. Returns true
      if the operation is successful, or false otherwise.
    - int getFront() Returns the front item from the Deque. Returns -1 if the
      deque is empty.
    - int getRear() Returns the last item from Deque. Returns -1 if the deque
      is empty.
    - boolean isEmpty() Returns true if the deque is empty, or false otherwise.
    - boolean isFull() Returns true if the deque is full, or false otherwise.
Link: https://leetcode.com/problems/design-circular-deque/
Notes:
    - use fixed arr and variables for circular state
"""


class MyCircularDeque:
    def __init__(self, k: int):
        self.q = [0] * k
        self.front = 0
        self.rear = k - 1
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.q[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


if __name__ == '__main__':
    cd1 = MyCircularDeque(3)
    print(cd1.insertLast(1))
    print(cd1.insertLast(2))
    print(cd1.insertFront(3))
    print(cd1.insertFront(4))
    print(cd1.getRear())
    print(cd1.isFull())
    print(cd1.deleteLast())
    print(cd1.insertFront(4))
    print(cd1.getFront())
