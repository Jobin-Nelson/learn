"""
Created Date: 2024-12-09
Qn: An array is considered special if every pair of its adjacent elements
    contains two numbers with different parity.

    You are given an array of integer nums and a 2D integer matrix queries,
    where for queries[i] = [fromi, toi] your task is to check that subarray
    nums[fromi..toi] is special or not.

    Return an array of booleans answer such that answer[i] is true if
    nums[fromi..toi] is special.
Link: https://leetcode.com/problems/special-array-ii/
Notes:
    - precompute prefix violating counts till index
    - query prefix[end] - prefix[start] == 0
"""

import unittest
from itertools import accumulate, pairwise


class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        # Functional approach
        prefix = list(
            accumulate(
                pairwise(nums),
                lambda x, y: x + 1 if y[0] & 1 == y[1] & 1 else x,
                initial=0,
            )
        )

        def query(start: int, end: int) -> bool:
            return prefix[end] - prefix[start] == 0

        return [query(s, e) for s, e in queries]

        # Imperative approach
        # res = [False] * len(queries)
        # prefix = [0] * len(nums)
        # prefix[0] = 0
        # for i in range(1, len(nums)):
        #     if nums[i] % 2 == nums[i - 1] % 2:
        #         prefix[i] = prefix[i - 1] + 1
        #     else:
        #         prefix[i] = prefix[i - 1]
        # for i, (s, e) in enumerate(queries):
        #     res[i] = prefix[e] - prefix[s] == 0
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_isArraySpecial1(self):
        n = [3, 4, 1, 2, 6]
        q = [[0, 4]]
        expected = [False]
        self.assertEqual(expected, self.sol.isArraySpecial(n, q))

    def test_isArraySpecial2(self):
        n = [4, 3, 1, 6]
        q = [[0, 2], [2, 3]]
        expected = [False, True]
        self.assertEqual(expected, self.sol.isArraySpecial(n, q))

    def test_isArraySpecial3(self):
        n = [10, 8, 8, 9]
        q = [[2, 3], [0, 1], [2, 3], [1, 3], [2, 2]]
        expected = [True, False, True, False, True]
        self.assertEqual(expected, self.sol.isArraySpecial(n, q))


if __name__ == '__main__':
    unittest.main()
