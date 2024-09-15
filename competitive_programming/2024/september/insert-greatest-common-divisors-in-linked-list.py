"""
Created Date: 2024-09-10
Qn: Given the head of a linked list head, in which each node contains an
  integer value.

  Between every pair of adjacent nodes, insert a new node with a value equal to
  the greatest common divisor of them.

  Return the linked list after insertion.

  The greatest common divisor of two numbers is the largest positive integer
  that evenly divides both numbers.
Link: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
Notes:
"""

from typing import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        cur = dummy = cls()
        for i in arr:
            cur.next = cls(i)
            cur = cur.next
        return dummy.next

    def __repr__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)


def insertGreatestCommonDivisor(head: ListNode | None) -> ListNode | None:
    def gcd(a: int, b: int) -> int:
        while a:
            a, b = b % a, a
        return b

    if head is None:
        return None
    cur = head
    while cur.next:
        a = cur.val
        b = cur.next.val
        nex = cur.next
        cur.next = ListNode(gcd(a, b), nex)
        cur = nex
    return head


if __name__ == '__main__':
    h1 = ListNode.from_list([18, 6, 10, 3])
    h2 = ListNode.from_list([7])

    print(insertGreatestCommonDivisor(h1))
    print(insertGreatestCommonDivisor(h2))
