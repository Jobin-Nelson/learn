'''
Created Date: 2023-09-05
Qn: A linked list of length n is given such that each node contains an
    additional random pointer, which could point to any node in the list, or
    null.

    Construct a deep copy of the list. The deep copy should consist of exactly
    n brand new nodes, where each new node has its value set to the value of
    its corresponding original node. Both the next and random pointer of the
    new nodes should point to new nodes in the copied list such that the
    pointers in the original list and copied list represent the same list
    state. None of the pointers in the new list should point to nodes in the
    original list.

    For example, if there are two nodes X and Y in the original list, where
    X.random --> Y, then for the corresponding two nodes x and y in the copied
    list, x.random --> y.

    Return the head of the copied linked list.

    The linked list is represented in the input/output as a list of n nodes.
    Each node is represented as a pair of [val, random_index] where:

        - val: an integer representing Node.val
        - random_index: the index of the node (range from 0 to n-1) that the
          random pointer points to, or null if it does not point to any node.

    Your code will only be given the head of the original linked list.
Link: https://leetcode.com/problems/copy-list-with-random-pointer/
Notes:
    - use hashmap to map old to copy
'''
from __future__ import annotations
from typing import Self

class Node:
    def __init__(self, val: int, next: Node = None, random: Node = None):
        self.val = val
        self.next = next
        self.random = random

    @classmethod
    def from_list(cls, arr: list[list[int | None]]) -> Self | None:
        nodes = [cls(val) for val, random in arr]
        nodes.append(None)
        for i, [_, ran] in enumerate(arr):
            node = nodes[i]
            if ran: node.random = nodes[ran]
            node.next = nodes[i+1]
        return nodes[0]

    def __str__(self) -> str:
        res, cur = [], self
        while cur:
            random = cur.random.val if cur.random else None
            res.append((cur.val, random))
            cur = cur.next
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def copyRandomList(head: Node | None) -> Node | None:
    oldToCopy = { None: None}
    cur = head
    while cur:
        copy = Node(cur.val)
        oldToCopy[cur] = copy
        cur = cur.next

    cur = head
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next
    return oldToCopy[head]

if __name__ == '__main__':
    h1 = Node.from_list([[7,None],[13,0],[11,4],[10,2],[1,0]])
    h2 = Node.from_list([[1,1],[2,1]])
    h3 = Node.from_list([[3,None],[3,0],[3,None]])

    print(copyRandomList(h1))
    print(copyRandomList(h2))
    print(copyRandomList(h3))
