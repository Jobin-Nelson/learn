"""
Created Date: 2025-05-10
Qn: You are given two arrays nums1 and nums2 consisting of positive integers.

    You have to replace all the 0's in both arrays with strictly positive
    integers such that the sum of elements of both arrays becomes equal.

    Return the minimum equal sum you can obtain, or -1 if it is impossible.
Link: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
Notes:
    - count total and return max
"""

import unittest


class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        t1 = 0
        n1_zero = 0
        for n in nums1:
            if n == 0:
                n1_zero += 1
                t1 += 1
            t1 += n

        t2 = 0
        n2_zero = 0
        for n in nums2:
            if n == 0:
                n2_zero += 1
                t2 += 1
            t2 += n

        if (n1_zero == 0 and t2 > t1) or (n2_zero == 0 and t1 > t2):
            return -1
        return max(t1, t2)



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minSum1(self):
        n1 = [3,2,0,1,0]
        n2 = [6,5,0]
        expected = 12
        self.assertEqual(expected, self.sol.minSum(n1, n2))

    def test_minSum2(self):
        n1 = [2,0,2,0]
        n2 = [1,4]
        expected = -1
        self.assertEqual(expected, self.sol.minSum(n1, n2))


if __name__ == '__main__':
    unittest.main()
