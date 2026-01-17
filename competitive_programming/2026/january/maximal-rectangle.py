"""
Created Date: 2026-01-11
Qn: Given a rows x cols binary matrix filled with 0's and 1's, find the largest
    rectangle containing only 1's and return its area.

Link: https://leetcode.com/problems/maximal-rectangle/
Notes:
    - use histogram
"""

import unittest


class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = [-1]
            for i in range(n + 1):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        return max_area


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        m = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        expected = 6
        self.assertEqual(expected, self.sol.maximalRectangle(m))

    def test2(self):
        m = [["0"]]
        expected = 0
        self.assertEqual(expected, self.sol.maximalRectangle(m))

    def test3(self):
        m = [["1"]]
        expected = 1
        self.assertEqual(expected, self.sol.maximalRectangle(m))


if __name__ == '__main__':
    unittest.main()
