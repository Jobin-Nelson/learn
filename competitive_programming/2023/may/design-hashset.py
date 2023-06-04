'''
Created Date: 2023-05-30
Qn: Design a HashSet without using any built-in hash table libraries.

    Implement MyHashSet class:

        - void add(key) Inserts the value key into the HashSet. 
        - bool contains(key) Returns whether the value key exists in the
          HashSet or not.
        - void remove(key) Removes the value key in the HashSet. If key does
          not exist in the HashSet, do nothing.

Link: https://leetcode.com/problems/design-hashset/
Notes:
    - use linkedlist for handling collisions
'''
class ListNode():
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class MyHashSet():
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]
    def add(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key: return
            cur = cur.next
        cur.next = ListNode(key)
    def remove(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False

if __name__ == '__main__':
    h = MyHashSet()
    h.add(1)
    h.add(2)
    print(h.contains(1))
    print(h.contains(3))
    h.add(2)
    print(h.contains(2))
    h.remove(2)
    print(h.contains(2))
