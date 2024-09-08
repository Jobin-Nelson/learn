"""
Created Date: 2024-09-08
Qn: Given the head of a singly linked list and an integer k, split the linked
    list into k consecutive linked list parts.

    The length of each part should be as equal as possible: no two parts should
    have a size differing by more than one. This may lead to some parts being
    null.

    The parts should be in the order of occurrence in the input list, and parts
    occurring earlier should always have a size greater than or equal to parts
    occurring later.

    Return an array of the k parts.
Link: https://leetcode.com/problems/split-linked-list-in-parts/
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


def splitListToParts(head: ListNode | None, k: int) -> list[ListNode | None]:
    res = [None] * k
    N = 0
    cur = head
    while cur:
        N += 1
        cur = cur.next
    divisor, remainder = divmod(N, k)
    cur = head

    for i in range(k):
        tail = new_part = ListNode(0)
        current_size = divisor
        if remainder > 0:
            remainder -= 1
            current_size += 1
        for j in range(current_size):
            tail.next = ListNode(cur.val)
            tail = tail.next
            cur = cur.next
        res[i] = new_part.next
    return res


if __name__ == '__main__':
    h1, k1 = ListNode.from_list(list(range(1, 4))), 5
    h2, k2 = ListNode.from_list(list(range(1, 11))), 3

    print(splitListToParts(h1, k1))
    print(splitListToParts(h2, k2))
