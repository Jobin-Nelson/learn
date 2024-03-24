"""
Created Date: 2024-03-20
Qn: You are given two linked lists: list1 and list2 of sizes n and m
    respectively.

    Remove list1's nodes from the ath node to the bth node, and put list2 in
    their place.

    The blue edges and nodes in the following figure indicate the result:
Link: https://leetcode.com/problems/merge-in-between-linked-lists/
Notes:
    - use two pointers
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

def mergeInBetween(list1: ListNode|None, a: int, b: int, list2: ListNode|None) -> ListNode|None:
    prev = p1 = list1
    p2 = list2
    while p2.next:
        p2 = p2.next
    counter = 0
    while p1:
        if counter == a:
            prev.next = list2
        if counter == b:
            p2.next = p1.next
            break
        prev = p1
        p1 = p1.next
        counter += 1
    return list1

if __name__ == '__main__':
    l11, a1, b1, l12 = ListNode.from_list([10,1,13,6,9,5]), 3, 4, ListNode.from_list([1000000,1000001,1000002])
    l21, a2, b2, l22 = ListNode.from_list([0,1,2,3,4,5,6]), 2, 5, ListNode.from_list([1000000,1000001,1000002,1000003,1000004])
    l31, a3, b3, l32 = ListNode.from_list([0,1,2]), 1, 1, ListNode.from_list([1000000,1000001,1000002,1000003])

    print(mergeInBetween(l11, a1, b1, l12))
    print(mergeInBetween(l21, a2, b2, l22))
    print(mergeInBetween(l31, a3, b3, l32))
