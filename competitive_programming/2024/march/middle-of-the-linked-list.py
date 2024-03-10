"""
Created Date: 2024-03-06
Qn: Given the head of a singly linked list, return the middle node of the linked list.
    If there are two middle nodes, return the second middle node.
Link: https://leetcode.com/problems/middle-of-the-linked-list/
Notes:
    - use slow and fast pointer
"""
from typing import Self

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    @classmethod
    def from_list(cls, arr: list[int], pos: int|None = None) -> Self|None:
        cur = dummy = cls()
        tail = None
        for i, n in enumerate(arr):
            cur.next = cls(n)
            cur = cur.next
            if pos is not None and i == pos: tail = cur
        if tail: cur.next = tail
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

def middleNode(head: ListNode|None) -> ListNode|None:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == '__main__':
    h1 = ListNode.from_list(list(range(1,6)))
    h2 = ListNode.from_list(list(range(1,7)))

    print(middleNode(h1))
    print(middleNode(h2))
