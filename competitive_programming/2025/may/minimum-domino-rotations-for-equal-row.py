"""
Created Date: 2025-05-03
Qn: In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom
    halves of the ith domino. (A domino is a tile with two numbers from 1 to 6
    - one on each half of the tile.)

    We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

    Return the minimum number of rotations so that all the values in tops are
    the same, or all the values in bottoms are the same.

    If it cannot be done, return -1.
Link: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
Notes:
    - iterate through top and bottom for first two values
"""

import unittest


class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)
        for target in [tops[0], bottoms[0]]:
            missing_t, missing_b = 0, 0
            for i, (top, bottom) in enumerate(zip(tops, bottoms)):
                if not (top == target or bottom == target):
                    break
                if top != target:
                    missing_t += 1
                if bottom != target:
                    missing_b += 1
                if i == n - 1:
                    return min(missing_t, missing_b)
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minDominoRotations1(self):
        t, b = [2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]
        expected = 2
        self.assertEqual(expected, self.sol.minDominoRotations(t, b))

    def test_minDominoRotations2(self):
        t, b = [3, 5, 1, 2, 3], [3, 6, 3, 3, 4]
        expected = 2
        self.assertEqual(expected, self.sol.minDominoRotations(t, b))


if __name__ == '__main__':
    unittest.main()
