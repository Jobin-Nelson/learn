"""
Created Date: 2025-05-11
Qn: Given an integer array arr, return true if there are three consecutive odd
    numbers in the array. Otherwise, return false.
Link: https://leetcode.com/problems/three-consecutive-odds/
Notes:
"""

import unittest
from itertools import accumulate


class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        # Functional approach
        # return any(n == 3 for n in accumulate((n & 1 == 1 for n in arr), lambda acc, n: acc + 1 if n else 0, initial=0))
        def count(acc: int, n: int) -> int:
            return acc + 1 if n & 1 == 1 else 0
        return any(n == 3 for n in accumulate(arr, count, initial=0))
        


        # Imperative approach
        # count = 0
        #
        # for n in arr:
        #     if count == 3:
        #         return True
        #     if n & 1 == 1:
        #         count += 1
        #     else:
        #         count = 0
        #
        # return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_threeConsecutiveOdds1(self):
        a = [2,6,4,1]
        expected = False
        self.assertEqual(expected, self.sol.threeConsecutiveOdds(a))

    def test_threeConsecutiveOdds2(self):
        a = [1,2,34,3,4,5,7,23,12]
        expected = True
        self.assertEqual(expected, self.sol.threeConsecutiveOdds(a))


if __name__ == '__main__':
    unittest.main()
