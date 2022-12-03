'''
Created Date: 2022-11-29
Qn: Implement the RandomizedSet class:

        - RandomizedSet() Initializes the RandomizedSet object.
        - bool insert(int val) Inserts an item val into the set if not present.
          Returns true if the item was not present, false otherwise.
        - bool remove(int val) Removes an item val from the set if present.
          Returns true if the item was present, false otherwise.
        - int getRandom() Returns a random element from the current set of
          elements (it's guaranteed that at least one element exists when this
          method is called). Each element must have the same probability of
          being returned.

    You must implement the functions of the class such that each function works
    in average O(1) time complexity.
Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
Notes:
    - use stack to store nums and hashmap to store index of nums
    - when removing swap the index of value to remove with the last element of
      the stack and pop from stack
'''
import random

class RandomizedSet:
    def __init__(self):
        self.map = dict()
        self.stack = []

    def insert(self, val:int) -> bool:
        if val in self.map: return False
        self.map[val] = len(self.stack)
        self.stack.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map: return False
        ind = self.map[val]
        last = self.stack[-1]
        self.stack[ind] = last
        self.map[last] = ind
        del self.map[val]
        self.stack.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.stack)

if __name__ == '__main__':
    r = RandomizedSet()
    print(r.insert(1))
    print(r.remove(2))
    print(r.insert(2))
    print(r.getRandom())
    print(r.remove(1))
    print(r.insert(2))
    print(r.getRandom())
    print(r.stack)
    print(r.map)
