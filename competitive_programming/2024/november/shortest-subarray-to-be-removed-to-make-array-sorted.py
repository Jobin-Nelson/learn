"""
Created Date: 2024-11-15
Qn: Given an integer array arr, remove a subarray (can be empty) from arr such
    that the remaining elements in arr are non-decreasing.

    Return the length of the shortest subarray to remove.

    A subarray is a contiguous subsequence of the array.
Link: https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
Notes:
    - two pointer
    - find postfix that is increasing
    - then expand from left
"""

import unittest


class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        N = len(arr)
        l, r = 0, N - 1
        # remove prefix
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        res = r

        # remove middle
        l = 0
        while l < r:
            # expand invalid window
            while r < N and arr[l] > arr[r]:
                r += 1
            res = min(res, r - l - 1)
            if arr[l] > arr[l + 1]:
                break
            l += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findLengthOfShortestSubarray1(self):
        a = [1, 2, 3, 10, 4, 2, 3, 5]
        self.assertEqual(self.sol.findLengthOfShortestSubarray(a), 3)

    def test_findLengthOfShortestSubarray2(self):
        a = [5, 4, 3, 2, 1]
        self.assertEqual(self.sol.findLengthOfShortestSubarray(a), 4)

    def test_findLengthOfShortestSubarray3(self):
        a = [1, 2, 3]
        self.assertEqual(self.sol.findLengthOfShortestSubarray(a), 0)


if __name__ == '__main__':
    unittest.main()
