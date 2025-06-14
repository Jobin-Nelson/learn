"""
Created Date: 2025-06-09
Qn: Given two integers n and k, return the kth lexicographically smallest
    integer in the range [1, n].
Link: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
Notes:
"""

import unittest


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        i = 1
        def count(cur: int) -> int:
            res = 0
            nei = cur + 1
            while cur <= n:
                res += min(nei, n+1) - cur
                cur *= 10
                nei *= 10
            return res

        while i < k:
            steps = count(cur)
            if i + steps <= k:
                cur += 1
                i += steps
            else:
                cur *= 10
                i += 1
        return cur


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findKthNumber1(self):
        n, k = 13, 2
        expected = 10
        self.assertEqual(expected, self.sol.findKthNumber(n, k))

    def test_findKthNumber2(self):
        n, k = 1, 1
        expected = 1
        self.assertEqual(expected, self.sol.findKthNumber(n, k))

    def test_findKthNumber3(self):
        n, k = 2, 2
        expected = 2
        self.assertEqual(expected, self.sol.findKthNumber(n, k))

    def test_findKthNumber4(self):
        n, k = 100, 100
        expected = 99
        self.assertEqual(expected, self.sol.findKthNumber(n, k))


if __name__ == '__main__':
    unittest.main()
