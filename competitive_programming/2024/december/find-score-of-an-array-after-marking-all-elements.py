"""
Created Date: 2024-12-13
Qn: You are given an array nums consisting of positive integers.

    Starting with score = 0, apply the following algorithm:

    - Choose the smallest integer of the array that is not marked. If there is
      a tie, choose the one with the smallest index.
    - Add the value of the chosen integer to score.
    - Mark the chosen element and its two adjacent elements if they exist.
    - Repeat until all the array elements are marked.

    Return the score you get after applying the above algorithm.
Link: https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/
Notes:
"""

import unittest
from itertools import accumulate
from collections import deque


class Solution:
    def findScore(self, nums: list[int]) -> int:
        # Functional approach
        xs = sorted((n, i) for i, n in enumerate(nums))
        xs = accumulate(
            xs,
            lambda x, y: x
            if y[1] in x[1]
            else (x[0] + y[0], x[1] | {y[1], y[1] - 1, y[1] + 1}),
            initial=(0, set()),
        )
        res, _ = deque(xs, maxlen=1)[0]
        return res

        # Imperative approach
        # xs = sorted((n, i) for i, n in enumerate(nums))
        # res = 0
        # adj = (-1, 1)
        # N = len(nums)
        # visited = [False] * N
        # for n, i in xs:
        #     if visited[i]: continue
        #     visited[i] = True
        #     res += n
        #     for nei in adj:
        #         if 0 <= i+nei < N:
        #             visited[i+nei] = True
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findScore1(self):
        n = [2, 1, 3, 4, 5, 2]
        expected = 7
        self.assertEqual(expected, self.sol.findScore(n))

    def test_findScore2(self):
        n = [2, 3, 5, 1, 3, 2]
        expected = 5
        self.assertEqual(expected, self.sol.findScore(n))


if __name__ == '__main__':
    unittest.main()
