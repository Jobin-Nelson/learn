"""
Created Date: 2025-05-17
Qn: Given an array nums with n objects colored red, white, or blue, sort them
    in-place so that objects of the same color are adjacent, with the colors in
    the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and
    blue, respectively.

    You must solve this problem without using the library's sort function.
Link: https://leetcode.com/problems/sort-colors/
Notes:
    - if there are only three elements in a list use dutch sort
    - swap zero with left pointer
    - skip 1's
    - swap two with right pointer
"""

import unittest


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # Dutch sort
        N = len(nums)
        zero = 0
        two = N - 1
        current_pointer = 0

        while current_pointer <= two:
            if nums[current_pointer] == 0:
                nums[zero], nums[current_pointer] = nums[current_pointer], nums[zero]
                zero += 1
                current_pointer += 1
            elif nums[current_pointer] == 2:
                nums[two], nums[current_pointer] = nums[current_pointer], nums[two]
                two -= 1
            else:
                current_pointer += 1


        # Merge sort
        # def merge(arr: list[int]) -> None:
        #     if len(arr) == 1: return
        #     m = len(arr) >> 1
        #     left, right = arr[:m].copy(), arr[m:].copy()
        #     merge(left)
        #     merge(right)
        #
        #     l, r, k = 0, 0, 0
        #     while l < len(left) and r < len(right) and k < len(arr):
        #         if left[l] < right[r]:
        #             arr[k] = left[l]
        #             l += 1
        #         else:
        #             arr[k] = right[r]
        #             r += 1
        #         k += 1
        #
        #     while l < len(left):
        #         arr[k] = left[l]
        #         k += 1
        #         l += 1
        #
        #     while r < len(right):
        #         arr[k] = right[r]
        #         k += 1
        #         r += 1
        # merge(nums)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_sortColors1(self):
        n = [2, 0, 2, 1, 1, 0]
        expected = [0, 0, 1, 1, 2, 2]
        self.sol.sortColors(n)
        self.assertEqual(expected, n)

    def test_sortColors2(self):
        n = [2, 0, 1]
        expected = [0, 1, 2]
        self.sol.sortColors(n)
        self.assertEqual(expected, n)


if __name__ == '__main__':
    unittest.main()
