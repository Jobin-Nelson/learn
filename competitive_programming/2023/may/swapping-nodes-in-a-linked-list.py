'''
Created Date: 2023-05-15
Qn: You are given the head of a linked list, and an integer k.

    Return the head of the linked list after swapping the values of the kth
    node from the beginning and the kth node from the end (the list is
    1-indexed).
Link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
Notes:
    - use two pointers
'''
from typing import Self

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self:
        N = len(arr)
        head = cls()
        node = head.next = cls(arr[0])
        for i in range(1, N):
            node.next = cls(arr[i])
            node = node.next
        return head.next
    
    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)


def swapNodes(head: ListNode | None, k: int) -> ListNode | None:
    start, end = head, head
    k -= 1
    while k and end:
        end = end.next
        k -= 1
    first_k = end

    while end.next:
        start = start.next
        end = end.next
    end_k = start
    
    first_k.val, end_k.val = end_k.val, first_k.val
    
    return head

if __name__ == '__main__':
    h1, k1 = ListNode.from_list([1,2,3,4,5]), 2
    h2, k2 = ListNode.from_list([7,9,6,6,7,8,3,0,9,5]), 5

    print(swapNodes(h1, k1))
    print(swapNodes(h2, k2))
