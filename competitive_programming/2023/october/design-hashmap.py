'''
Created Date: 2023-10-04
Qn: Design a HashMap without using any built-in hash table libraries.

    Implement the MyHashMap class:

        - MyHashMap() initializes the object with an empty map. 
        - void put(int key, int value) inserts a (key, value) pair into the
          HashMap. 
        - If the key already exists in the map, update the corresponding value. 
        - int get(int key) returns the value to which the specified key is
          mapped, or -1 if this map contains no mapping for the key. 
        - void remove(key) removes the key and its corresponding value if the
          map contains the mapping for the key.

Link: https://leetcode.com/problems/design-hashmap/
Notes:
    - use array and linkedlist
'''
class LinkedList:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.map = [LinkedList(-1, -1) for _ in range(self.size)]
    def hash(self, key: int) -> int:
        return key % self.size
    def put(self, key: int, value: int) -> None:
        ll = self.map[self.hash(key)]
        while ll.next:
            if ll.next.key == key:
                ll.next.val = value
                return
            ll = ll.next
        ll.next = LinkedList(key, value)

    def get(self, key: int) -> int:
        ll = self.map[self.hash(key)]
        while ll:
            if ll.key == key: return ll.val
            ll = ll.next
        return -1

    def remove(self, key: int) -> None:
        ll = self.map[self.hash(key)]
        while ll.next:
            if ll.next.key == key:
                ll.next = ll.next.next
                return
            ll = ll.next

if __name__ == '__main__':
    h = MyHashMap()
    h.put(1, 1)
    h.put(2, 2)
    print(h.get(1))
    print(h.get(3))
    h.put(2, 1)
    print(h.get(2))
    h.remove(2)
    print(h.get(2))
