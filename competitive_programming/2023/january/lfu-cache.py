'''
Created Date: 2023-01-29
Qn: Design and implement a data structure for a Least Frequently Used (LFU)
    cache.

    Implement the LFUCache class:

        - LFUCache(int capacity) Initializes the object with the capacity of
          the data structure. 
        - int get(int key) Gets the value of the key if the key exists in the
          cache. Otherwise, returns -1. 
        - void put(int key, int value) Update the value of the key if present,
          or inserts the key if not already present. When the cache reaches its
          capacity, it should invalidate and remove the least frequently used
          key before inserting a new item. For this problem, when there is a
          tie (i.e., two or more keys with the same frequency), the least
          recently used key would be invalidated. 
    
    To determine the least frequently used key, a use
    counter is maintained for each key in the cache. The key with the
    smallest use counter is the least frequently used key.

    When a key is first inserted into the cache, its use counter is set to 1
    due to the put operation. The use counter for a key in the cache is
    incremented either a get or put operation is called on it.

    The functions get and put must each run in O(1) average time complexity.
Link: https://leetcode.com/problems/lfu-cache/
Notes:
    - use doubly linked list for maintaining frequency
'''
from collections import defaultdict

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None)
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, node: Node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1

    def pop(self, node=None):
        if self._size == 0:
            return

        if not node:
            node = self._sentinel.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

        return node

class LFUCache:
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._node = dict()
        self._freq = defaultdict(DLinkedList)
        self._minfreq = 0

    def _update(self, node):
        freq = node.freq
        self._freq[freq].pop(node)
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)

    def get(self, key: int) -> int:
        if key not in self._node:
            return -1

        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return
        
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1
                
            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1

if __name__ == '__main__':
    lc = LFUCache(2)
    lc.put(1, 1)
    lc.put(2, 2)
    print(lc.get(1))
    lc.put(3, 3)
    print(lc.get(2))
    print(lc.get(3))
    lc.put(4, 4)
    print(lc.get(1))
    print(lc.get(3))
    print(lc.get(4))
