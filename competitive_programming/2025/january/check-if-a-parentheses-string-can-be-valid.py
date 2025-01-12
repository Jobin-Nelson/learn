"""
Created Date: 2025-01-12
Qn: A parentheses string is a non-empty string consisting only of '(' and ')'.
    It is valid if any of the following conditions is true:

    - It is ().
    - It can be written as AB (A concatenated with B), where A and B are valid
      parentheses strings.
    - It can be written as (A), where A is a valid parentheses string.

    You are given a parentheses string s and a string locked, both of length n.
    locked is a binary string consisting only of '0's and '1's. For each index
    i of locked,

    - If locked[i] is '1', you cannot change s[i].
    - But if locked[i] is '0', you can change s[i] to either '(' or ')'.

    Return true if you can make s a valid parentheses string. Otherwise, return
    false.
Link: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
Notes:
"""

import unittest
from functools import reduce
from typing import Callable


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # Functional approach
        if len(s) & 1:
            return False

        def get_count_fn(l2r: bool) -> Callable:
            paren = '(' if l2r else ')'

            def count_locked_unlocked(
                x: tuple[int, int, bool], y: tuple[str, str]
            ) -> tuple[int, int, bool]:
                locked, unlocked, state = x
                p, l = y
                return (
                    (locked, unlocked, state)
                    if not state
                    else (locked, unlocked + 1, state)
                    if l == '0'
                    else (locked + 1, unlocked, state)
                    if p == paren
                    else (locked - 1, unlocked, state)
                    if locked > 0
                    else (locked, unlocked - 1, state)
                    if unlocked > 0
                    else (locked, unlocked, False)
                )

            return count_locked_unlocked

        locked_count, _, state = reduce(
            get_count_fn(True), zip(s, locked), (0, 0, True)
        )
        return (
            state
            if locked_count == 0
            else reduce(
                get_count_fn(False), zip(reversed(s), reversed(locked)), (0, 0, True)
            )[2]
        )

        # Imperative approach
        # if len(s) & 1:
        #     return False
        #
        # locked_count = 0
        # unlocked_count = 0
        #
        # for p, l in zip(s, locked):
        #     if l == '0':
        #         unlocked_count += 1
        #     elif p == '(':
        #         locked_count += 1
        #     else:
        #         if locked_count > 0:
        #             locked_count -= 1
        #         elif unlocked_count > 0:
        #             unlocked_count -= 1
        #         else:
        #             return False
        # if locked_count == 0:
        #     return True
        #
        # locked_count = 0
        # unlocked_count = 0
        #
        # for p, l in zip(reversed(s), reversed(locked)):
        #     if l == '0':
        #         unlocked_count += 1
        #     elif p == ')':
        #         locked_count += 1
        #     else:
        #         if locked_count > 0:
        #             locked_count -= 1
        #         elif unlocked_count > 0:
        #             unlocked_count -= 1
        #         else:
        #             return False
        #
        # return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_canBeValid1(self):
        s = "))()))"
        l = "010100"
        expected = True
        self.assertEqual(expected, self.sol.canBeValid(s, l))

    def test_canBeValid2(self):
        s = "()()"
        l = "0000"
        expected = True
        self.assertEqual(expected, self.sol.canBeValid(s, l))

    def test_canBeValid3(self):
        s = ")"
        l = "0"
        expected = False
        self.assertEqual(expected, self.sol.canBeValid(s, l))


if __name__ == '__main__':
    unittest.main()
