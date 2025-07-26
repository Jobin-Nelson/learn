"""
Created Date: 2025-07-22
Qn: You are given an array of positive integers nums and want to erase a
    subarray containing unique elements. The score you get by erasing the
    subarray is equal to the sum of its elements.

    Return the maximum score you can get by erasing exactly one subarray.

    An array b is called to be a subarray of a if it forms a contiguous
    subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some
    (l,r).
Link: https://leetcode.com/problems/maximum-erasure-value/
Notes:
    - use sliding window
"""

import unittest


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        visited = set()
        left = 0
        max_sum = 0
        cur_sum = 0
        for n in nums:
            if n in visited:
                while nums[left] != n:
                    cur_sum -= nums[left]
                    visited.remove(nums[left])
                    left += 1
                left += 1
            else:
                visited.add(n)
                cur_sum += n

            max_sum = max(max_sum, cur_sum)
        return max_sum


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumUniqueSubarray1(self):
        n = [4, 2, 4, 5, 6]
        expected = 17
        self.assertEqual(expected, self.sol.maximumUniqueSubarray(n))

    def test_maximumUniqueSubarray2(self):
        n = [5, 2, 1, 2, 5, 2, 1, 2, 5]
        expected = 8
        self.assertEqual(expected, self.sol.maximumUniqueSubarray(n))


if __name__ == '__main__':
    unittest.main()
