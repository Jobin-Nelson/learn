"""
Created Date: 2025-02-07
Qn: You are given an integer limit and a 2D array queries of size n x 2.

    There are limit + 1 balls with distinct labels in the range [0, limit].
    Initially, all balls are uncolored. For every query in queries that is of
    the form [x, y], you mark ball x with the color y. After each query, you
    need to find the number of distinct colors among the balls.

    Return an array result of length n, where result[i] denotes the number of
    distinct colors after ith query.

    Note that when answering a query, lack of a color will not be considered as
    a color.
Link: https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/
Notes:
"""

import unittest


class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        res = [0] * len(queries)
        color_map = {}
        ball_map = {}

        for i, (b, c) in enumerate(queries):
            if b in ball_map:
                prev_color = ball_map[b]
                color_map[prev_color] -= 1

                if color_map[prev_color] == 0:
                    del color_map[prev_color]
            ball_map[b] = c
            color_map[c] = color_map.get(c, 0) + 1
            res[i] = len(color_map)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_queryResults1(self):
        l, q = 4, [[1, 4], [2, 5], [1, 3], [3, 4]]
        expected = [1, 2, 2, 3]
        self.assertEqual(expected, self.sol.queryResults(l, q))

    def test_queryResults2(self):
        l, q = 4, [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
        expected = [1, 2, 2, 3, 4]
        self.assertEqual(expected, self.sol.queryResults(l, q))


if __name__ == '__main__':
    unittest.main()
