"""
Created Date: 2024-03-03
Qn: Given the head of a linked list, remove the nth node from the end of the
    list and return its head.
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Notes:
"""
from typing import Self

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self|None:
        cur = dummy = cls()
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
        
def removeNthFromEnd(head: ListNode|None, n: int) -> ListNode|None:
    if head is None: return None
    dummy = ListNode(0, head)
    p1, p2 = dummy, dummy
    for _ in range(n):
        p1 = p1.next
    while p1.next:
        p1 = p1.next
        p2 = p2.next
    p2.next = p2.next.next
    print(f'{p2.next=} = {p2.next.next=}')
    return head

if __name__ == '__main__':
    h1, n1 = ListNode.from_list(list(range(1,6))), 2
    h2, n2 = ListNode.from_list([1]), 1
    h3, n3 = ListNode.from_list([1,2]), 1

    print(removeNthFromEnd(h1, n1))
    print(removeNthFromEnd(h2, n2))
    print(removeNthFromEnd(h3, n3))
