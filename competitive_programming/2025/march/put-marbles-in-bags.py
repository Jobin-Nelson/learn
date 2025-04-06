"""
Created Date: 2025-03-31
Qn: You have k bags. You are given a 0-indexed integer array weights where
    weights[i] is the weight of the ith marble. You are also given the integer
    k.

    Divide the marbles into the k bags according to the following rules:

    - No bag is empty.
    - If the ith marble and jth marble are in a bag, then all marbles with an
      index between the ith and jth indices should also be in that same bag.
    - If a bag consists of all the marbles with an index from i to j
      inclusively, then the cost of the bag is weights[i] + weights[j].

    The score after distributing the marbles is the sum of the costs of all the
    k bags.

    Return the difference between the maximum and minimum scores among marble
    distributions.
Link: https://leetcode.com/problems/put-marbles-in-bags/
Notes:
    - take the sum of pair, sort and sum up the ends of the sorted array till k-1
"""

import unittest
from itertools import pairwise


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        pair_weights = [w1 + w2 for w1, w2 in pairwise(weights)]
        pair_weights.sort()
        N = len(pair_weights)
        return sum(pair_weights[N - 1 - i] - pair_weights[i] for i in range(k - 1))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_putMarbles1(self):
        w = [1, 3, 5, 1]
        k = 2
        expected = 4
        self.assertEqual(expected, self.sol.putMarbles(w, k))

    def test_putMarbles2(self):
        w = [1, 3]
        k = 2
        expected = 0
        self.assertEqual(expected, self.sol.putMarbles(w, k))


if __name__ == '__main__':
    unittest.main()
