"""
Created Date: 2025-07-18
Qn: You are given a 0-indexed integer array nums consisting of 3 * n elements.

    You are allowed to remove any subsequence of elements of size exactly n
    from nums. The remaining 2 * n elements will be divided into two equal
    parts:

    - The first n elements belonging to the first part and their sum is
      sumfirst.
    - The next n elements belonging to the second part and their sum is
      sumsecond.

    The difference in sums of the two parts is denoted as sumfirst - sumsecond.

    - For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
    - Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.

    Return the minimum difference possible between the sums of the two parts
    after the removal of n elements.
Link: https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/
Notes:
    - minimize the first part and maximize the second part
"""

import heapq
import unittest
from sys import maxsize


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n, n3 = len(nums), len(nums) // 3
        t1 = sum(nums[:n3])
        max_pq = [-x for x in nums[:n3]]
        heapq.heapify(max_pq)
        p1 = [0] * n
        p1[n3 - 1] = t1

        for i in range(n3, n3 * 2):
            t1 += nums[i]
            heapq.heappush(max_pq, -nums[i])
            t1 -= -heapq.heappop(max_pq)
            p1[i] = t1

        t2 = sum(nums[-n3:])
        min_pq = nums[-n3:]
        heapq.heapify(min_pq)
        p2 = [0] * n
        p2[n3 * 2] = t2

        for i in range(n3 * 2 - 1, n3 - 1, -1):
            t2 += nums[i]
            heapq.heappush(min_pq, nums[i])
            t2 -= heapq.heappop(min_pq)
            p2[i] = t2
        res = maxsize

        for i in range(n3 - 1, n3 * 2):
            res = min(res, p1[i] - p2[i + 1])
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumDifference1(self):
        n = [3, 1, 2]
        expected = -1
        self.assertEqual(expected, self.sol.minimumDifference(n))

    def test_minimumDifference2(self):
        n = [7, 9, 5, 8, 1, 3]
        expected = 1
        self.assertEqual(expected, self.sol.minimumDifference(n))


if __name__ == '__main__':
    unittest.main()
