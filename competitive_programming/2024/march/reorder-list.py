"""
Created Date: 2024-03-23
Qn: You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln

    Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

    You may not modify the values in the list's nodes. Only nodes themselves
    may be changed.
Link: https://leetcode.com/problems/reorder-list/
Notes:
    - use slow and fast pointers
"""
from typing import Self

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self|None:
        cur = dummy = cls(0)
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

def reorderList(head: ListNode|None) -> None:
    if head is None: return None
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    p2 = slow.next
    slow.next = None
    prev = None

    while p2:
        nex = p2.next
        p2.next = prev
        prev = p2
        p2 = nex

    p1 = head
    p2 = prev

    while p1 and p2:
        p1_next = p1.next
        p2_next = p2.next
        p1.next = p2
        p2.next = p1_next
        p1 = p1_next
        p2 = p2_next

if __name__ == '__main__':
    h1 = ListNode.from_list(list(range(1, 5)))
    h2 = ListNode.from_list(list(range(1, 6)))

    reorderList(h1)
    reorderList(h2)

    print(h1)
    print(h2)
