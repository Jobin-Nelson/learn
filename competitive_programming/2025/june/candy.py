"""
Created Date: 2025-06-02
Qn: There are n children standing in a line. Each child is assigned a rating
    value given in the integer array ratings.

    You are giving candies to these children subjected to the following
    requirements:

    - Each child must have at least one candy.
    - Children with a higher rating get more candies than their neighbors.

    Return the minimum number of candies you need to have to distribute the
    candies to the children.
Link: https://leetcode.com/problems/candy/
Notes:
"""

import unittest
from itertools import pairwise, starmap


class Solution:
    def candy(self, ratings: list[int]) -> int:
        # Imperative
        n = len(ratings)
        candy = [1] * n
        for i in range(1,n):
            if ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1)
        return sum(candy)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_candy1(self):
        r = [1, 0, 2]
        expected = 5
        self.assertEqual(expected, self.sol.candy(r))

    def test_candy2(self):
        r = [1, 2, 2]
        expected = 4
        self.assertEqual(expected, self.sol.candy(r))


if __name__ == '__main__':
    unittest.main()
