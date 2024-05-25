"""
Created Date: 2024-05-06
Qn: You are given the head of a linked list.

    Remove every node which has a node with a greater value anywhere to the
    right side of it.

    Return the head of the modified linked list.
Link: https://leetcode.com/problems/remove-nodes-from-linked-list/
Notes:
    - use stack
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

def removeNodes(head: ListNode|None) -> ListNode|None:
    stack = []
    cur = head
    while cur:
        while stack and stack[-1] < cur.val:
            stack.pop()
        stack.append(cur.val)
        cur = cur.next
    dummy = cur = ListNode(0)
    for n in stack:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

    # recursion
    # if head is None or head.next is None:
    #     return head
    # next_node = removeNodes(head.next)
    # if head.val < next_node:
    #     return next_node
    # head.next = next_node
    # return head

if __name__ == '__main__':
    h1 = ListNode.from_list([5,2,13,3,8])
    h2 = ListNode.from_list([1,1,1,1])

    print(removeNodes(h1))
    print(removeNodes(h2))
