"""
Created Date: 2025-06-25
Qn: Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an
    integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j]
    where 0 <= i < nums1.length and 0 <= j < nums2.length.
Link: https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/
Notes:
    - use binary search twice
        - first for finding the target
        - second for finding the smaller product counts
"""

import bisect
import math
import unittest


class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        N2 = len(nums2)

        def get_smaller_product_count(target: int) -> int:
            smaller = 0
            for n in nums1:
                if n < 0:
                    smaller += N2 - bisect.bisect_left(nums2, math.ceil(target / n))
                elif n == 0:
                    if target >=0:
                        smaller += N2
                else:
                    smaller += bisect.bisect_right(nums2, target // n)
            return smaller

        def good(target: int) -> bool:
            return get_smaller_product_count(target) >= k

        left, right = -(10**10), 10**10
        while left < right:
            mid = left + ((right - left) >> 1)
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left

        # TLE
        # return sorted(x * y for x in nums1 for y in nums2)[k-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_kthSmallestProduct1(self):
        n1, n2 = [2, 5], [3, 4]
        k = 2
        expected = 8
        self.assertEqual(expected, self.sol.kthSmallestProduct(n1, n2, k))

    def test_kthSmallestProduct2(self):
        n1, n2 = [-4, -2, 0, 3], [2, 4]
        k = 6
        expected = 0
        self.assertEqual(expected, self.sol.kthSmallestProduct(n1, n2, k))

    def test_kthSmallestProduct3(self):
        n1, n2 = [-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5]
        k = 3
        expected = -6
        self.assertEqual(expected, self.sol.kthSmallestProduct(n1, n2, k))


if __name__ == '__main__':
    unittest.main()
