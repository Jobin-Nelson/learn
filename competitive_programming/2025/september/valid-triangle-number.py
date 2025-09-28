"""
Created Date: 2025-09-26
Qn: Given an integer array nums, return the number of triplets
    chosen from the array that can make triangles if we take
    them as side lengths of a triangle.
Link: https://leetcode.com/problems/valid-triangle-number/
Notes:
"""

import unittest


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n-2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i+1, n):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += k - j - i
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = [2, 2, 3, 4]
        expected = 3
        self.assertEqual(expected, self.sol.triangleNumber(n))

    def test2(self):
        n = [4, 2, 3, 4]
        expected = 4
        self.assertEqual(expected, self.sol.triangleNumber(n))


if __name__ == '__main__':
    unittest.main()
