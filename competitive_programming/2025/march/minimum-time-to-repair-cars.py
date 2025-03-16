"""
Created Date: 2025-03-16
Qn: You are given an integer array ranks representing the ranks of some
    mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r
    can repair n cars in r * n2 minutes.

    You are also given an integer cars representing the total number of cars
    waiting in the garage to be repaired.

    Return the minimum time taken to repair all the cars. Note: All the
    mechanics can repair the cars simultaneously.
Link: https://leetcode.com/problems/minimum-time-to-repair-cars/
Notes:
    - use binary search
"""

import unittest


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        def isRepairable(time: int) -> bool:
            return sum(int((time // r) ** 0.5) for r in ranks) >= cars

        l, r = 1, min(ranks) * cars * cars
        while l <= r:
            m = l + ((r - l) >> 1)
            if isRepairable(m):
                r = m - 1
            else:
                l = m + 1
        return l


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_repairCars1(self):
        r = [4, 2, 3, 1]
        c = 10
        expected = 16
        self.assertEqual(expected, self.sol.repairCars(r, c))

    def test_repairCars2(self):
        r = [5, 1, 8]
        c = 6
        expected = 16
        self.assertEqual(expected, self.sol.repairCars(r, c))


if __name__ == '__main__':
    unittest.main()
