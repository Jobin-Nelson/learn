'''
Created Date: 2023-04-25
Qn: You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

    Implement the SmallestInfiniteSet class:

        - SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to
          contain all positive integers. 
        - int popSmallest() Removes and returns the smallest integer contained
          in the infinite set. 
        - void addBack(int num) Adds a positive integer num back into the
          infinite set, if it is not already in the infinite set.

Link: https://leetcode.com/problems/smallest-number-in-infinite-set/
Notes:
    - use variable to keep track of the smallest element
    - use set to keep track of the popped elements
'''
class SmallestInfiniteSet():
    def __init__(self):
        self.small = 1
        self.popped = set()
    def popSmallest(self) -> int:
        res = self.small
        self.popped.add(res)
        self.small += 1
        while self.small in self.popped:
            self.small += 1
        return res
    def addBack(self, num: int) -> None:
        self.popped.discard(num)
        if num < self.small:
            self.small = num


if __name__ == '__main__':
    obj = SmallestInfiniteSet()
    obj.addBack(2)
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    obj.addBack(1)
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
