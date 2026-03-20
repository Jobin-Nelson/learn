"""
Created Date: 2026-03-16
Qn: You are given an m x n integer matrix grid​​​.

    A rhombus sum is the sum of the elements that form the border of a regular
    rhombus shape in grid​​​. The rhombus must have the shape of
    a square rotated 45 degrees with each of the corners centered in a grid
    cell. Below is an image of four valid rhombus shapes with the corresponding
    colored cells that should be included in each rhombus sum:

    Note that the rhombus can have an area of 0, which is depicted by the
    purple rhombus in the bottom right corner.

    Return the biggest three distinct rhombus sums in the grid in descending
    order. If there are less than three distinct values, return all of them.
Link: https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/
Notes:
"""

import unittest


class Answer:
    def __init__(self):
        self.ans = [0, 0, 0]

    def put(self, x: int) -> None:
        _ans = self.ans
        if x > _ans[0]:
            _ans[0], _ans[1], _ans[2] = x, _ans[0], _ans[1]
        elif x != _ans[0] and x > _ans[1]:
            _ans[1], _ans[2] = x, _ans[1]
        elif x != _ans[0] and x != _ans[1] and x > _ans[2]:
            _ans[2] = x

    def get(self) -> list[int]:
        return [n for n in self.ans if n != 0]


class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        sum1 = [[0] * (n + 2) for _ in range(m + 2)]
        sum2 = [[0] * (n + 2) for _ in range(m + 2)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum1[i][j] = sum1[i - 1][j - 1] + grid[i - 1][j - 1]
                sum2[i][j] = sum2[i - 1][j + 1] + grid[i - 1][j - 1]

        ans = Answer()

        for r in range(m):
            for c in range(n):
                ans.put(grid[r][c])

                for L in range(1, min(r, c)):
                    if r + 2 * L >= m or c - L < 0 or c + L >= n:
                        break

                    edge1 = sum2[r + L + 1][c - L + 1] - sum2[r + 1][c + 1]
                    edge2 = sum1[r + 2 * L + 1][c + 1] - sum1[r + L + 1][c - L + 1]
                    edge3 = sum1[r + L + 1][c + L + 1] - sum1[r + 1][c + 1]
                    edge4 = sum2[r + 2 * L + 1][c + 1] - sum2[r + L + 1][c + L + 1]

                    total = (
                        edge1 + edge2 + edge3 + edge4 + grid[r][c] - grid[r + 2 * L][c]
                    )
                    ans.put(total)
        return ans.get()


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        g = [
            [3, 4, 5, 1, 3],
            [3, 3, 4, 2, 3],
            [20, 30, 200, 40, 10],
            [1, 5, 5, 4, 1],
            [4, 3, 2, 2, 5],
        ]
        expected = [228, 216, 211]
        self.assertEqual(expected, self.sol.getBiggestThree(g))

    def test2(self):
        g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [20, 9, 8]
        self.assertEqual(expected, self.sol.getBiggestThree(g))

    def test3(self):
        g = [[7, 7, 7]]
        expected = [7]
        self.assertEqual(expected, self.sol.getBiggestThree(g))


if __name__ == '__main__':
    unittest.main()
