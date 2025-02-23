"""
Created Date: 2025-02-17
Qn: You have n  tiles, where each tile has one letter tiles[i] printed on it.

    Return the number of possible non-empty sequences of letters you can make
    using the letters printed on those tiles.
Link: https://leetcode.com/problems/letter-tile-possibilities/
Notes:
    - use backtracking
"""

import unittest
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backtrack() -> int:
            res = 0

            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    res += 1 + backtrack()
                    count[c] += 1
            return res

        return backtrack()


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_numTilePossibilities1(self):
        t = "AAB"
        expected = 8
        self.assertEqual(expected, self.sol.numTilePossibilities(t))

    def test_numTilePossibilities2(self):
        t = "AAABBC"
        expected = 188
        self.assertEqual(expected, self.sol.numTilePossibilities(t))

    def test_numTilePossibilities3(self):
        t = "V"
        expected = 1
        self.assertEqual(expected, self.sol.numTilePossibilities(t))


if __name__ == '__main__':
    unittest.main()
