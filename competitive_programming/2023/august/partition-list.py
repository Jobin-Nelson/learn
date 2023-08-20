'''
Created Date: 2023-08-15
Qn: Given the head of a linked list and a value x, partition it such that all
    nodes less than x come before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the
    two partitions.
Link: https://leetcode.com/problems/partition-list/
Notes:
    - use 2 lists and 2 pointers
'''
from typing import Self

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        head = cls()
        cur = head
        for n in arr:
            cur.next = cls(n)
            cur = cur.next
        return head.next
    
    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)
    
    def __repr__(self) -> str:
        return self.__str__()

def partition(head: ListNode | None, x: int) -> ListNode | None:
    l1 = p1 = ListNode()
    l2 = p2 = ListNode()
    p = head

    while p:
        if p.val < x:
            p1.next = p
            p1 = p1.next
        else:
            p2.next = p
            p2 = p2.next
        p = p.next

    p2.next = None
    p1.next = l2.next
    return l1.next

if __name__ == '__main__':
    h1, x1 = ListNode.from_list([1,4,3,2,5,2]), 3
    h2, x2 = ListNode.from_list([2,1]), 2

    print(partition(h1, x1))
    print(partition(h2, x2))
