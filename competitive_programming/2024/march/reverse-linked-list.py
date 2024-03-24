"""
Created Date: 2024-03-21
Qn: Given the head of a singly linked list, reverse the list, and return the
    reversed list.
Link: https://leetcode.com/problems/reverse-linked-list/
Notes:
    - reverse nodes as you iterate through them
"""
from typing import Self

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self|None:
        dummy = cur = cls()
        for n in arr:
            cur.next = cls(n)
            cur = cur.next
        return dummy.next

    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def reverseList(head: ListNode|None) -> ListNode|None:
    prev = None
    cur = head

    while cur:
        nex = cur.next
        cur.next = prev
        prev = cur
        cur = nex
    return prev

if __name__ == '__main__':
    h1 = ListNode.from_list(list(range(1, 6)))
    h2 = ListNode.from_list([1,2])
    h3 = ListNode.from_list([])

    print(reverseList(h1))
    print(reverseList(h2))
    print(reverseList(h3))
