"""
Created Date: 2024-12-28
Qn: Given an integer array nums and an integer k, find three
    non-overlapping subarrays of length k with maximum sum and return
    them.

    Return the result as a list of indices representing the starting
    position of each interval (0-indexed). If there are multiple answers,
    return the lexicographically smallest one.
Link: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
Notes:
    - use preprocessing to calculate k_sums
    - use dp to get_max sum of 3 indices
"""

import unittest


class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        # pre processing
        k_sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            k_sums.append(k_sums[-1] + nums[i] - nums[i - k])

        dp = {}

        def get_max(i: int, cnt: int) -> int:
            if cnt == 3 or i > len(nums) - k:
                return 0
            if (i, cnt) in dp:
                return dp[(i, cnt)]
            include = k_sums[i] + get_max(i + k, cnt + 1)
            skip = get_max(i + 1, cnt)
            dp[(i, cnt)] = max(include, skip)
            return dp[(i, cnt)]

        def get_indices():
            i = 0
            indices = []
            while i <= len(nums) - k and len(indices) < 3:
                include = k_sums[i] + get_max(i+k, len(indices)+1)
                skip = get_max(i+1, len(indices))

                if include >= skip:
                    indices.append(i)
                    i += k
                else:
                    i += 1
            return indices
        return get_indices()


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxSumOfThreeSubarrays1(self):
        n, k = [1, 2, 1, 2, 6, 7, 5, 1], 2
        expected = [0, 3, 5]
        self.assertEqual(expected, self.sol.maxSumOfThreeSubarrays(n, k))

    def test_maxSumOfThreeSubarrays2(self):
        n, k = [1, 2] * 4 + [1], 2
        expected = [0, 2, 4]
        self.assertEqual(expected, self.sol.maxSumOfThreeSubarrays(n, k))


if __name__ == '__main__':
    unittest.main()
