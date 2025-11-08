"""
Created Date: 2025-11-01
Qn: You are given an array of integers nums and the head of a linked list.
    Return the head of the modified linked list after removing all nodes from
    the linked list that have a value that exists in nums.
Link: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
Notes:
"""

import unittest
from typing import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: list[int]) -> Self | None:
        cur = head = cls()
        for n in arr:
            cur.next = cls(n)
            cur = cur.next
        return head.next

    def __str__(self) -> str:
        res = []
        cur = self
        while cur:
            cur = cur.next
            res.append(cur.val)
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: ListNode) -> bool:
        cur = self
        while cur and other:
            if cur.val != other.val:
                return False
            cur = cur.next
            other = other.next
        return cur is None and other is None


class Solution:
    def modifiedList(self, nums: list[int], head: ListNode | None) -> ListNode | None:
        removeSet = set(nums)
        cur = dummy = ListNode()
        while head:
            if head.val not in removeSet:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
        return dummy.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = list(range(1, 4))
        h = ListNode.from_list(list(range(1, 6)))
        expected = ListNode.from_list([4, 5])
        self.assertEqual(expected, self.sol.modifiedList(n, h))

    def test2(self):
        n = [1]
        h = ListNode.from_list([1, 2, 1, 2, 1, 2])
        expected = ListNode.from_list([2, 2, 2])
        self.assertEqual(expected, self.sol.modifiedList(n, h))
    def test3(self):
        n = [9,2,5]
        h = ListNode.from_list([2,10,9])
        expected = ListNode.from_list([10])
        self.assertEqual(expected, self.sol.modifiedList(n, h))


if __name__ == '__main__':
    unittest.main()
