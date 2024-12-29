"""
Created Date: 2024-12-27
Qn: You are given an integer array values where values[i] represents the value
    of the ith sightseeing spot. Two sightseeing spots i and j have a distance
    j - i between them.

    The score of a pair (i < j) of sightseeing spots is values[i] + values[j] +
    i - j: the sum of the values of the sightseeing spots, minus the distance
    between them.

    Return the maximum score of a pair of sightseeing spots.
Link: https://leetcode.com/problems/best-sightseeing-pair/
Notes:
    - track cur_max as you iterate
"""

import unittest


class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        res = 0
        cur_max = values[0] - 1
        for n in values[1:]:
            res = max(res, n + cur_max)
            cur_max = max(cur_max - 1, n - 1)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxScoreSightseeingPair1(self):
        v = [8, 1, 5, 2, 6]
        expected = 11
        self.assertEqual(expected, self.sol.maxScoreSightseeingPair(v))

    def test_maxScoreSightseeingPair2(self):
        v = [1, 2]
        expected = 2
        self.assertEqual(expected, self.sol.maxScoreSightseeingPair(v))


if __name__ == '__main__':
    unittest.main()
