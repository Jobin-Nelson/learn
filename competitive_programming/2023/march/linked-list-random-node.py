'''
Created Date: 2023-03-10
Qn: Given a singly linked list, return a random node's value from the linked
    list. Each node must have the same probability of being chosen.

    Implement the Solution class:

        - Solution(ListNode head) Initializes the object with the head of the
          singly-linked list head. 
        - int getRandom() Chooses a node randomly from the list and returns its
          value. All the nodes of the list should be equally likely to be
          chosen.
Link: https://leetcode.com/problems/linked-list-random-node/
Notes:
    - use list
    - randomly index into the list
'''
from __future__ import annotations
from typing import Self
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        N = len(arr)
        def dfs(i: int) -> Self | None:
            if i >= N: return None
            node = cls(arr[i])
            node.next = dfs(i + 1)
            return node
        return dfs(0)

    def __str__(self) -> str:
        res = []
        cur = self

        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

class Solution():
    def __init__(self, head: ListNode | None):
        self.head = head
        self.values = []
        while head:
            self.values.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.values[random.randint(0, len(self.values)-1)]

if __name__ == '__main__':
    o = Solution(ListNode.from_list([1, 2, 3]))
    print(o.getRandom())
    print(o.getRandom())
    print(o.getRandom())
    print(o.getRandom())
    print(o.getRandom())
