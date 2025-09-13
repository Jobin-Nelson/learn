"""
Created Date: 2025-09-07
Qn: Given an integer n, return any array containing n unique integers such that
    they add up to 0.
Link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
Notes:
"""

import unittest


class Solution:
    def sumZero(self, n: int) -> list[int]:
        l = range((-n+1)>>1,(n+2)>>1)
        return list(l) if n & 1 else [i for i in l if i != 0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sumZero1(self):
        n = 5
        # expected = [-7, -1, 1, 3, 4]
        expected = [-2,-1,0,1,2]
        self.assertEqual(expected, self.sol.sumZero(n))

    def test_sumZero2(self):
        n = 3
        expected = [-1, 0, 1]
        self.assertEqual(expected, self.sol.sumZero(n))

    def test_sumZero3(self):
        n = 1
        expected = [0]
        self.assertEqual(expected, self.sol.sumZero(n))
    def test_sumZero4(self):
        n = 4
        expected = [-2,-1,1,2]
        self.assertEqual(expected, self.sol.sumZero(n))


if __name__ == '__main__':
    unittest.main()
