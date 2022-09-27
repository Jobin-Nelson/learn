'''
Created Date: 2022-09-25
Qn: Design your implementation of the circular queue. The circular queue is a
linear data structure in which the operations are performed based on FIFO
(First In First Out) principle and the last position is connected back to the
first position to make a circle. It is also called "Ring Buffer".

    One of the benefits of the circular queue is that we can make use of the
    spaces in front of the queue. In a normal queue, once the queue becomes
    full, we cannot insert the next element even if there is a space in front
    of the queue. But using the circular queue, we can use the space to store
    new values.

    Implementation the MyCircularQueue class:

        - MyCircularQueue(k) Initializes the object with the size of the queue
          to be k.
        - int Front() Gets the front item from the queue. If the queue is
          empty, return -1. 
        - int Rear() Gets the last item from the queue. If the queue is empty,
          return -1. 
        - boolean enQueue(int value) Inserts an element into the circular
          queue. Return true if the operation is successful. 
        - boolean deQueue() Deletes an element from the circular queue. Return
          true if the operation is successful.
        - boolean isEmpty() Checks whether the circular queue is empty or not. 
        - boolean isFull() Checks whether the circular queue is full or not.
          You must solve the problem without using the built-in queue data
          structure in your programming language.
Link: https://leetcode.com/problems/design-circular-queue/
Notes:
    - use head & tail pointers
'''
class MyCircularQueue:
    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.length = k
        self.q = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.q[self.tail] = value
        self.size += 1
        self.tail = (self.tail + 1) % self.length
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.size -= 1
        self.head = (self.head + 1) % self.length
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.tail-1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.length

if __name__ == '__main__':
    cq = MyCircularQueue(3)
    print(cq.enQueue(1))
    print(cq.enQueue(2))
    print(cq.enQueue(3))
    print(cq.enQueue(4))
    print(cq.Rear())
    print(cq.isFull())
    print(cq.deQueue())
    print(cq.enQueue(4))
    print(cq.Rear())
    
