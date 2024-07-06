"""
Created Date: 2024-07-04
Qn: You are given the head of a linked list, which contains a series of
    integers separated by 0's. The beginning and end of the linked list will
    have Node.val == 0.

    For every two consecutive 0's, merge all the nodes lying in between them
    into a single node whose value is the sum of all the merged nodes. The
    modified list should not contain any 0's.

    Return the head of the modified linked list.
Link: https://leetcode.com/problems/merge-nodes-in-between-zeros/
Notes:
    - use two pointers one pass
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

def mergeNodes(head: ListNode|None) -> ListNode|None:
    modify = head.next
    next_sum = modify

    while next_sum:
        cur_sum = 0
        while next_sum.val != 0:
            cur_sum += next_sum.val
            next_sum = next_sum.next
        modify.val = cur_sum
        next_sum = next_sum.next
        modify.next = next_sum
        modify = modify.next
    return head.next

if __name__ == '__main__':
    h1 = [0,3,1,0,4,5,2,0]
    h2 = [0,1,0,3,0,2,2,0]

    print(mergeNodes(ListNode.from_list(h1)))
    print(mergeNodes(ListNode.from_list(h2)))
