'''
Created Date: 2023-07-18
Qn: Design a data structure that follows the constraints of a Least Recently
    Used (LRU) cache.

    Implement the LRUCache class:

        - LRUCache(int capacity) Initialize the LRU cache with positive size
          capacity. 
        - int get(int key) Return the value of the key if the key exists,
          otherwise return -1. 
        - void put(int key, int value) Update the value of the key if the key
          exists. Otherwise, add the key-value pair to the cache. If the number
          of keys exceeds the capacity from this operation, evict the least
          recently used key.

    The functions get and put must each run in O(1) average time complexity.
Link: https://leetcode.com/problems/lru-cache/
Notes:
    - use doubly linked list
    - use two pointers left (lru) and right(mru)
    - use hashmap to store a pointer to the nodes
'''
class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def insert(self, node: Node):
        last_node, next_node = self.right.prev, self.right
        last_node.next = next_node.prev = node
        node.prev, node.next = last_node, next_node

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache: self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

if __name__ == '__main__':
    l = LRUCache(2)
    l.put(1, 1)
    l.put(2, 2)
    print(l.get(1))
    l.put(3, 3)
    print(l.get(2))
    l.put(4, 4)
    print(l.get(1))
    print(l.get(3))
    print(l.get(4))

