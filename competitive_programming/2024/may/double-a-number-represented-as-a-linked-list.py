"""
Created Date: 2024-05-07
Qn: You are given the head of a non-empty linked list representing a
    non-negative integer without leading zeroes.

    Return the head of the linked list after doubling it.
Link: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
Notes:
    - add one more listnode if the head value is more than 4
    - then double and increment as you iterate over the listnode
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

def doubleIt(head: ListNode|None) -> ListNode|None:
    if head.val > 4:
        head = ListNode(0, head)

    cur = head
    while cur:
        cur.val = (cur.val * 2) % 10
        if cur.next and cur.next.val > 4:
            cur.val += 1
        cur = cur.next
    return head

if __name__ == '__main__':
    h1 = ListNode.from_list([1,8,9])
    h2 = ListNode.from_list([9,9,9])

    print(doubleIt(h1))
    print(doubleIt(h2))
