'''
Created Date: 2023-09-07
Qn: Given the head of a singly linked list and two integers left and right
where left <= right, reverse the nodes of the list from position left to
position right, and return the reversed list.
Link: https://leetcode.com/problems/reverse-linked-list-ii/
Notes:
    - skip till left pointer and reverse till right pointer
    - link left_prev to prev and left_inner to cur
'''
from __future__ import annotations

class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None =None):
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
        res, cur = [], self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def reverseBetween(head: ListNode | None, left: int, right: int) -> ListNode | None:
    dummy = ListNode(0, head)
    left_prev, cur = dummy, head
    for _ in range(left - 1):
        left_prev, cur = cur, cur.next

    prev = None
    for _ in range(right - left + 1):
        nex = cur.next
        cur.next = prev
        prev, cur = cur, nex

    left_prev.next.next = cur
    left_prev.next = prev
    return dummy.next


if __name__ == '__main__':
    h1, l1, r1 = ListNode.from_list([1,2,3,4,5]), 2, 4
    h2, l2, r2 = ListNode.from_list([5]), 1, 1

    print(reverseBetween(h1, l1, r1))
    print(reverseBetween(h2, l2, r2))

