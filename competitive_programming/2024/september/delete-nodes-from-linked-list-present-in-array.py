"""
Created Date: 2024-09-06
Qn: You are given an array of integers nums and the head of a linked list.
  Return the head of the modified linked list after removing all nodes from the
  linked list that have a value that exists in nums.
Link: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
Notes:
"""

from typing import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        N = len(arr)
        cur = dummy = cls()
        i = 0
        while cur and i < N:
            cur.next = cls(arr[i])
            cur = cur.next
            i += 1
        return dummy.next

    def __repr__(self) -> str:
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        return str(res)


def modified(nums: list[int], head: ListNode | None) -> ListNode | None:
    if head is None:
        return None
    nums_set = set(nums)
    cur = dummy = ListNode(0, head)
    while cur.next:
        if cur.next.val in nums_set:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next


if __name__ == '__main__':
    n1, h1 = [1, 2, 3], ListNode.from_list(list(range(1, 6)))
    n2, h2 = [1], ListNode.from_list([1, 2, 1, 2, 1, 2])
    n3, h3 = [5], ListNode.from_list(list(range(1, 5)))

    print(modified(n1, h1))
    print(modified(n2, h2))
    print(modified(n3, h3))
