"""
Created Date: 2024-12-19
Qn: You are given an integer array arr of length n that represents a
    permutation of the integers in the range [0, n - 1].

    We split arr into some number of chunks (i.e., partitions), and
    individually sort each chunk. After concatenating them, the result should
    equal the sorted array.

    Return the largest number of chunks we can make to sort the array.
Link: https://leetcode.com/problems/max-chunks-to-make-sorted/
Notes:
    - use cur_sum or cur_max and count the number of times it matches with index
"""

import unittest
from functools import reduce

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        # Functional approach
        def cur_max_res(x: tuple[int, int], y: tuple[int, int]):
            cur_max = max(x[1], y[1])
            return (x[0] + 1, cur_max) if y[0] == cur_max else (x[0],cur_max)
        return reduce(cur_max_res, enumerate(arr), (0,0))[0]

        # Imperative appraoch
        # cur_max = 0
        # res = 0
        # for i, n in enumerate(arr):
        #     cur_max = max(cur_max, n)
        #     if i == cur_max:
        #         res += 1
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxChunksToSorted1(self):
        a = [4, 3, 2, 1, 0]
        expected = 1
        self.assertEqual(expected, self.sol.maxChunksToSorted(a))

    def test_maxChunksToSorted2(self):
        a = [1, 0, 2, 3, 4]
        expected = 4
        self.assertEqual(expected, self.sol.maxChunksToSorted(a))


if __name__ == '__main__':
    unittest.main()
