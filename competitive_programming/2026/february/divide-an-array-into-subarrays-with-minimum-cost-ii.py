"""
Created Date: 2026-02-02
Qn: You are given a 0-indexed array of integers nums of length n, and two
    positive integers k and dist.

    The cost of an array is the value of its first element. For example, the
    cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

    You need to divide nums into k disjoint contiguous , such that the
    difference between the starting index of the second subarray and the
    starting index of the kth subarray should be less than or equal to dist. In
    other words, if you divide nums into the subarrays nums[0..(i1 - 1)],
    nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)], then ik-1 - i1 <= dist.

    Return the minimum possible sum of the cost of these subarrays.
Link: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
Notes:
"""

import unittest
from sys import maxsize


class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        if k == 1:
            return nums[0]
        k -= 1
        window = SortedList(nums[1 : dist + 2])
        cur_sum = sum(window[:k])
        min_sum = cur_sum
        for i in range(1, len(nums) - dist - 1):
            outgoing = nums[i]
            incoming = nums[i + dist + 1]
            index_out = window.index(outgoing)
            if index_out < k:
                cur_sum -= outgoing
                cur_sum += window[k]
            window.remove(outgoing)
            window.add(incoming)
            index_in = window.index(incoming)
            if index_in < k:
                cur_sum += incoming
                cur_sum -= window[k]
            min_sum = min(min_sum, cur_sum)
        return min_sum + nums[0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        nums, k, dist = [1, 3, 2, 6, 4, 2], 3, 3
        expected = 5
        self.assertEqual(expected, self.sol.minimumCost(nums, k, dist))

    def test2(self):
        nums, k, dist = [10, 8, 18, 9], 3, 1
        expected = 36
        self.assertEqual(expected, self.sol.minimumCost(nums, k, dist))


if __name__ == '__main__':
    unittest.main()
