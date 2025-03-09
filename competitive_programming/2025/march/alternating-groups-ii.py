"""
Created Date: 2025-03-09
Qn: There is a circle of red and blue tiles. You are given an array of integers
    colors and an integer k. The color of tile i is represented by colors[i]:

    - colors[i] == 0 means that tile i is red.
    - colors[i] == 1 means that tile i is blue.

    An alternating group is every k contiguous tiles in the circle with
    alternating colors (each tile in the group except the first and last one
    has a different color from its left and right tiles).

    Return the number of alternating groups.

    Note that since colors represents a circle, the first and the last tiles
    are considered to be next to each other.
Link: https://leetcode.com/problems/alternating-groups-ii/
Notes:
    - use sliding window
"""

import unittest
from itertools import chain, pairwise
from functools import reduce


class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        # Functional approach
        def count(
            acc: tuple[int, int], c: tuple[int, tuple[int, int]]
        ) -> tuple[int, int]:
            l, res = acc
            i, (c1, c2) = c
            return (
                (i, res)
                if c1 == c2
                else (l + 1, res + 1)
                if i - l + 1 == k
                else (l, res)
            )

        _, res = reduce(
            count, enumerate(pairwise(chain(colors, colors[: k - 1])), start=1), (0, 0)
        )
        return res

        # Imperative approach
        # l = 0
        # N = len(colors)
        # res = 0
        # for r in range(1, N + k - 1):
        #     if colors[r % N] == colors[(r - 1) % N]:
        #         l = r
        #     elif r - l + 1 == k:
        #         res += 1
        #         l += 1
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_numberOfAlternatingGroups1(self):
        c = [0, 1, 0, 1, 0]
        k = 3
        expected = 3
        self.assertEqual(expected, self.sol.numberOfAlternatingGroups(c, k))

    def test_numberOfAlternatingGroups2(self):
        c = [0, 1, 0, 0, 1, 0, 1]
        k = 6
        expected = 2
        self.assertEqual(expected, self.sol.numberOfAlternatingGroups(c, k))

    def test_numberOfAlternatingGroups3(self):
        c = [1, 1, 0, 1]
        k = 4
        expected = 0
        self.assertEqual(expected, self.sol.numberOfAlternatingGroups(c, k))


if __name__ == '__main__':
    unittest.main()
