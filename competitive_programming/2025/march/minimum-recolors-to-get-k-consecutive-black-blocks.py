"""
Created Date: 2025-03-08
Qn: You are given a 0-indexed string blocks of length n, where blocks[i] is
    either 'W' or 'B', representing the color of the ith block. The characters
    'W' and 'B' denote the colors white and black, respectively.

    You are also given an integer k, which is the desired number of consecutive
    black blocks.

    In one operation, you can recolor a white block such that it becomes a
    black block.

    Return the minimum number of operations needed such that there is at least
    one occurrence of k consecutive black blocks.
Link: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
Notes:
    - use sliding window
"""

import unittest


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, whites = 0, 0
        res = k
        for r in range(len(blocks)):
            whites += 1 if blocks[r] == 'W' else 0
            if r - l + 1 == k:
                res = min(res, whites)
                whites -= 1 if blocks[l] == 'W' else 0
                l += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumRecolors1(self):
        b = "WBBWWBBWBW"
        k = 7
        expected = 3
        self.assertEqual(expected, self.sol.minimumRecolors(b, k))

    def test_minimumRecolors2(self):
        b = "WBWBBBW"
        k = 2
        expected = 0
        self.assertEqual(expected, self.sol.minimumRecolors(b, k))

    def test_minimumRecolors3(self):
        b = "BWWWBB"
        k = 6
        expected = 3
        self.assertEqual(expected, self.sol.minimumRecolors(b, k))

    def test_minimumRecolors4(self):
        b = "BBBBBWWBBWBWBWWWBWBWBBBBWBBBBWBWBWBWBWWBWWBWBWWWWBBWWWWBWWWWBWBBWBBWBBWWW"
        k = 29
        expected = 10
        self.assertEqual(expected, self.sol.minimumRecolors(b, k))


if __name__ == '__main__':
    unittest.main()
