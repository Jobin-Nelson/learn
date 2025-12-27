"""
Created Date: 2025-12-24
Qn: You are given an array apple of size n and an array capacity of size m.

    There are n packs where the ith pack contains apple[i] apples. There are m
    boxes as well, and the ith box has a capacity of capacity[i] apples.

    Return the minimum number of boxes you need to select to redistribute these
    n packs of apples into boxes.

    Note that, apples from the same pack can be distributed into different
    boxes.
Link: https://leetcode.com/problems/apple-redistribution-into-boxes/
Notes:
"""

import unittest
from itertools import accumulate, takewhile


class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        total_apples = sum(apple)

        return sum(
            1
            for _ in takewhile(
                lambda x: x < total_apples, accumulate(sorted(capacity, reverse=True), initial=0)
            )
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        a, c = [1, 3, 2], [4, 3, 1, 5, 2]
        expected = 2
        self.assertEqual(expected, self.sol.minimumBoxes(a, c))

    def test2(self):
        a, c = [5, 5, 5], [2, 4, 2, 7]
        expected = 4
        self.assertEqual(expected, self.sol.minimumBoxes(a, c))


if __name__ == '__main__':
    unittest.main()
