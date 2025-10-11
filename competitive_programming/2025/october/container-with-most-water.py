"""
Created Date: 2025-10-04
Qn: You are given an integer array height of length n. There are n vertical
    lines drawn such that the two endpoints of the ith line are (i, 0) and (i,
    height[i]).

    Find two lines that together with the x-axis form a container, such that
    the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

Link: https://leetcode.com/problems/container-with-most-water/
Notes:
"""

import unittest


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(res, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        self.assertEqual(expected, self.sol.maxArea(h))

    def test2(self):
        h = [1, 1]
        expected = 1
        self.assertEqual(expected, self.sol.maxArea(h))


if __name__ == '__main__':
    unittest.main()
