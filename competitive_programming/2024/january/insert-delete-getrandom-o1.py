"""
Created Date: 2024-01-16
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

    You must implement the functions of the class such that each function works in
    average O(1) time complexity.
Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
Notes:
    - use hashmap and list
"""
import random

class RandomizedSet:
    def __init__(self):
        self.id = []
        self.map = {}
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.id)
        self.id.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val in self.map:
            last_val = self.id[-1]
            self.id[self.map[val]] = last_val
            self.map[last_val] = self.map[val]
            self.id.pop()
            del self.map[val]
            return True
        return False
    def getRandom(self) -> int:
        return random.choice(self.id)

if __name__ == '__main__':
    r = RandomizedSet()
    r.insert(1)
    r.remove(2)
    r.insert(2)
    print(r.getRandom())
    r.remove(1)
    r.insert(2)
    print(r.getRandom())
