"""
Created Date: 2025-08-01
Qn: Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly
    above it as shown:
Link: https://leetcode.com/problems/pascals-triangle/
Notes:
"""

import operator as op
import unittest


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Functional approach
        res = [[1]]
        for _ in range(numRows - 1):
            res.append(list(map(op.add, res[-1] + [0], [0] + res[-1])))
        return res

        # Imperative approach
        # res = [[1]]
        # for _ in range(numRows-1):
        #     cur_level = [1]
        #     prev_level = res[-1]
        #     for i in range(1, len(prev_level)):
        #         cur_level.append(prev_level[i - 1] + prev_level[i])
        #     cur_level.append(1)
        #     res.append(cur_level)
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_generate1(self):
        n = 5
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertEqual(expected, self.sol.generate(n))

    def test_generate2(self):
        n = 1
        expected = [[1]]
        self.assertEqual(expected, self.sol.generate(n))


if __name__ == '__main__':
    unittest.main()
