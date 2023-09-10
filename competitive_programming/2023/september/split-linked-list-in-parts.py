'''
Created Date: 2023-09-06
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
    - use divmod to get the remainder and base_len of each list parts
'''
from typing import Self

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        node = head = cls()
        for n in arr:
            node.next = cls(n)
            node = node.next
        return head.next

    def __str__(self) -> str:
        if self is None: return str([])
        res, cur = [], self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def splitListToParts(head: ListNode | None, k: int) -> list[ListNode | None]:
    size, cur = 0, head
    while cur:
        cur = cur.next
        size += 1

    base_len, remainder = divmod(size, k)
    res, cur = [], head
    for _ in range(k):
        res.append(cur)
        for _ in range(base_len - 1 + (remainder > 0)):
            if not cur: break
            cur = cur.next
        if remainder > 0: remainder -= 1
        if cur: cur.next, cur = None, cur.next
    return res

if __name__ == '__main__':
    h1, k1 = ListNode.from_list([1,2,3]), 5
    h2, k2 = ListNode.from_list([1,2,3,4,5,6,7,8,9,10]), 3

    print(splitListToParts(h1, k1))
    print(splitListToParts(h2, k2))

