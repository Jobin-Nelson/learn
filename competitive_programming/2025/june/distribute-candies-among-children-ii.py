"""
Created Date: 2025-06-01
Qn: You are given two positive integers n and limit.

    Return the total number of ways to distribute n candies among 3 children
    such that no child gets more than limit candies.
Link: https://leetcode.com/problems/distribute-candies-among-children-ii/
Notes:
    - use maths
"""

import unittest


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Functional
        return sum(
            min(limit, n - i) - max(0, n - i - limit) + 1
            for i in range(min(limit, n) + 1)
            if n - i <= 2 * limit
        )

        # Imperative
        # res = 0
        # for i in range(min(limit, n) + 1):
        #     if n - i > 2 * limit:
        #         continue
        #     res += min(limit, n - i) - max(n - i - limit, 0) + 1
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_distributeCandies1(self):
        n, limit = 5, 2
        expected = 3
        self.assertEqual(expected, self.sol.distributeCandies(n, limit))

    def test_distributeCandies2(self):
        n, limit = 3, 3
        expected = 10
        self.assertEqual(expected, self.sol.distributeCandies(n, limit))


if __name__ == '__main__':
    unittest.main()
