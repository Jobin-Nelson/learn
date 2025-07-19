"""
Created Date: 2025-07-14
Qn: Given head which is a reference node to a singly-linked list. The value of
    each node in the linked list is either 0 or 1. The linked list holds the
    binary representation of a number.

    Return the decimal value of the number in the linked list.

    The most significant bit is at the head of the linked list.
Link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
Notes:
    - use bitshift << and or | to construct the decimal value
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


class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        res = 0
        cur = head
        while cur:
            res = (res << 1) | cur.val
            cur = cur.next
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_getDecimalValue1(self):
        h = ListNode.from_list([1, 0, 1])
        expected = 5
        self.assertEqual(expected, self.sol.getDecimalValue(h))

    def test_getDecimalValue2(self):
        h = ListNode.from_list([0])
        expected = 0
        self.assertEqual(expected, self.sol.getDecimalValue(h))


if __name__ == '__main__':
    unittest.main()
