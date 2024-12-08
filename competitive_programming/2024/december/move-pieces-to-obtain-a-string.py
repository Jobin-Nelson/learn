"""
Created Date: 2024-12-05
Qn: You are given two strings start and target, both of length n. Each string
    consists only of the characters 'L', 'R', and '_' where:

    - The characters 'L' and 'R' represent pieces, where a piece 'L' can move
      to the left only if there is a blank space directly to its left, and a
      piece 'R' can move to the right only if there is a blank space directly
      to its right.
    - The character '_' represents a blank space that can be occupied by any of
      the 'L' or 'R' pieces.

    Return true if it is possible to obtain the string target by moving the
    pieces of the string start any number of times. Otherwise, return false.
Link: https://leetcode.com/problems/move-pieces-to-obtain-a-string/
Notes:
"""

import unittest
from functools import reduce
from itertools import accumulate
from typing import TypeAlias

Freq: TypeAlias = tuple[int, int, int, int, bool]


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Functional approach (WIP)
        # def inner(acc: Freq, x: tuple[str, str]) -> Freq:
        #     a, b = x
        #     sl, sr, tl, tr, fail = acc
        #     return (
        #         sl + 1 if a == 'L' else sl,
        #         sr + 1 if a == 'R' else sr,
        #         tl + 1 if b == 'L' else tl,
        #         tr + 1 if b == 'R' else tr,
        #         (
        #             (
        #                 False
        #                 if a == 'L' and tr > sr
        #                 else False
        #                 if a == 'R' and tl > sl
        #                 else fail
        #             )
        #             or (
        #                 False
        #                 if b == 'L' and sr > tr
        #                 else False
        #                 if b == 'R' and sl > tl
        #                 else fail
        #             )
        #         ),
        #     )
        #
        # def inner_helper(x: Freq) -> bool:
        #     sl, sr, tl, tr, fail = x
        #     return fail and not (tr > sr or sl > tl)
        #
        # if any(
        #     map(
        #         inner_helper,
        #         accumulate(zip(start, target), inner, initial=(0, 0, 0, 0, True)),
        #     )
        # ):
        #     return False
        # sl, sr, tl, tr, _ = reduce(inner, zip(start, target), (0, 0, 0, 0, True))
        # return sl == tl and sr == tr

        # Imperative approach
        start_left = start_right = 0
        target_left = target_right = 0
        for sc, tc in zip(start, target):
            if sc == 'L':
                start_left += 1
                if target_right > start_right:
                    return False
            elif sc == 'R':
                start_right += 1
                if target_left > start_left:
                    return False

            if tc == 'L':
                target_left += 1
                if start_right > target_right:
                    return False
            elif tc == 'R':
                target_right += 1
                if start_left > target_left:
                    return False

            if target_right > start_right or start_left > target_left:
                return False

        return start_left == target_left and start_right == target_right


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_canChange1(self):
        s = "_L__R__R_"
        t = "L______RR"
        self.assertEqual(True, self.sol.canChange(s, t))

    def test_canChange2(self):
        s = "R_L_"
        t = "__LR"
        self.assertEqual(False, self.sol.canChange(s, t))

    def test_canChange3(self):
        s = "_R"
        t = "R_"
        self.assertEqual(False, self.sol.canChange(s, t))

    def test_canChange4(self):
        s = "_LL__R__R_"
        t = "L___L___RR"
        self.assertEqual(False, self.sol.canChange(s, t))


if __name__ == '__main__':
    unittest.main()
