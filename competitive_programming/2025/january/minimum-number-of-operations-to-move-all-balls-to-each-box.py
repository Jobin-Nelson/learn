"""
Created Date: 2025-01-06
Qn: You have n boxes. You are given a binary string boxes of length n, where
    boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

    In one operation, you can move one ball from a box to an adjacent box. Box
    i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there
    may be more than one ball in some boxes.

    Return an array answer of size n, where answer[i] is the minimum number of
    operations needed to move all the balls to the ith box.

    Each answer[i] is calculated considering the initial state of the boxes.
Link: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
Notes:
"""

import unittest
from itertools import accumulate, islice
from operator import add


class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        # Functional approach
        left_balls = accumulate(accumulate(map(int, boxes), initial=0))
        right_balls = reversed(
            list(accumulate(accumulate(map(int, reversed(boxes)), initial=0)))
        )
        return list(
            map(add, islice(left_balls, len(boxes)), islice(right_balls, 1, None))
        )
        # return [
        #     l + r
        #     for l, r in zip(
        #         islice(left_balls, len(boxes)), islice(right_balls, 1, None)
        #     )
        # ]

        # Imperative approach
        # N = len(boxes)
        # res = [0] * N
        # balls_to_left = 0
        # balls_to_right = 0
        # moves_to_left = 0
        # moves_to_right = 0
        #
        # for i, c in enumerate(boxes):
        #     res[i] += moves_to_left
        #     balls_to_left += int(c)
        #     moves_to_left += balls_to_left
        #
        #     j = N - i - 1
        #     res[j] += moves_to_right
        #     balls_to_right += int(boxes[j])
        #     moves_to_right += balls_to_right
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minOperations1(self):
        b = "110"
        expected = [1, 1, 3]
        self.assertEqual(expected, self.sol.minOperations(b))

    def test_minOperations2(self):
        b = "001011"
        expected = [11, 8, 5, 4, 3, 4]
        self.assertEqual(expected, self.sol.minOperations(b))


if __name__ == '__main__':
    unittest.main()
