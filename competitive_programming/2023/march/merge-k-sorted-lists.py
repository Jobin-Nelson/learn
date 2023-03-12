'''
Created Date: 2023-03-12
Qn: You are given an array of k linked-lists lists, each linked-list is sorted
    in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.
Link: https://leetcode.com/problems/merge-k-sorted-lists/
Notes:
    - use merge sort
    - divide to left and right
    - merge
'''
from typing import Optional, Self

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Optional[Self]:
        root = cls()
        node = root
        for n in arr:
            node.next = cls(n)
            node = node.next
        return root.next

    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)

def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists: return None
    if len(lists) == 1: return lists[0]

    mid = len(lists) >> 1
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])
    return merge(left, right)

def merge(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    cur = dummy

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

if __name__ == '__main__':
    l1 = [ListNode.from_list([1,4,5]),ListNode.from_list([1,3,4]),ListNode.from_list([2,6])]
    l2 = []
    l3 = [ListNode.from_list([])]

    print(mergeKLists(l1))
    print(mergeKLists(l2))
    print(mergeKLists(l3))
