"""
Created Date: 2024-12-12
Qn: You are given an integer array gifts denoting the number of gifts in
    various piles. Every second, you do the following:

    - Choose the pile with the maximum number of gifts.
    - If there is more than one pile with the maximum number of gifts, choose
      any.
    - Leave behind the floor of the square root of the number of gifts in the
      pile. Take the rest of the gifts.

    Return the number of gifts remaining after k seconds.
Link: https://leetcode.com/problems/take-gifts-from-the-richest-pile/
Notes:
    - use heap
"""

import unittest
import heapq
import math


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            gift = -1 * heapq.heappop(heap)
            heapq.heappush(heap, -1 * math.floor(math.sqrt(gift)))
        return -1 * sum(heap)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_pickGifts1(self):
        g = [25, 64, 9, 4, 100]
        k = 4
        expected = 29
        self.assertEqual(expected, self.sol.pickGifts(g, k))
    def test_pickGifts2(self):
        g = [1] * 4
        k = 4
        expected = 4
        self.assertEqual(expected, self.sol.pickGifts(g, k))


if __name__ == '__main__':
    unittest.main()
