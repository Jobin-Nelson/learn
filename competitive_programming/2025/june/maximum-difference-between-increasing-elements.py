"""
Created Date: 2025-06-16
Qn: Given a 0-indexed integer array nums of size n, find the maximum difference
    between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j
    < n and nums[i] < nums[j].

    Return the maximum difference. If no such i and j exists, return -1.
Link: https://leetcode.com/problems/maximum-difference-between-increasing-elements/
Notes:
"""

import unittest


class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        # Editorial
        res, premin = -1, nums[0]

        for n in nums[1:]:
            if n > premin:
                res = max(res, n - premin)
            else:
                premin = n
        return res

        # My Approach
        # N = len(nums)
        # mins = [0] * N
        # mins[0] = nums[0]
        # maxs = [0] * N
        # maxs[N - 1] = nums[N - 1]
        # for i in range(1, N):
        #     mins[i] = min(mins[i - 1], nums[i])
        #     maxs[N - i - 1] = max(maxs[N - i - 2], nums[N - i - 1])
        # res = max(y - x for x, y in zip(mins, maxs))
        # return res if res != 0 else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumDifference1(self):
        n = [7, 1, 5, 4]
        expected = 4
        self.assertEqual(expected, self.sol.maximumDifference(n))

    def test_maximumDifference2(self):
        n = [9, 4, 3, 2]
        expected = -1
        self.assertEqual(expected, self.sol.maximumDifference(n))

    def test_maximumDifference3(self):
        n = [1, 5, 2, 10]
        expected = 9
        self.assertEqual(expected, self.sol.maximumDifference(n))


if __name__ == '__main__':
    unittest.main()
