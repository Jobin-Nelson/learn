"""
Created Date: 2024-11-21
Qn: You are given two integers m and n representing a 0-indexed m x n grid. You
    are also given two 2D integer arrays guards and walls where guards[i] =
    [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith
    guard and jth wall respectively.

    A guard can see every cell in the four cardinal directions (north, east,
    south, or west) starting from their position unless obstructed by a wall or
    another guard. A cell is guarded if there is at least one guard that can
    see it.

    Return the number of unoccupied cells that are not guarded.
Link: https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
Notes:
    - construct and simulate graph
"""

import unittest


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]
    ) -> int:
        graph = [['U'] * n for _ in range(m)]
        for i, j in walls:
            graph[i][j] = 'W'
        for i, j in guards:
            graph[i][j] = 'G'
        for i, j in guards:
            for row in range(i + 1, m):
                if graph[row][j] in 'WG':
                    break
                graph[row][j] = 'S'
            for row in range(i - 1, -1, -1):
                if graph[row][j] in 'WG':
                    break
                graph[row][j] = 'S'
            for col in range(j + 1, n):
                if graph[i][col] in 'WG':
                    break
                graph[i][col] = 'S'
            for col in range(j - 1, -1, -1):
                if graph[i][col] in 'WG':
                    break
                graph[i][col] = 'S'
        return len([c for r in graph for c in r if c == 'U'])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countUnguarded1(self):
        m, n = 4, 6
        g = [[0, 0], [1, 1], [2, 3]]
        w = [[0, 1], [2, 2], [1, 4]]
        self.assertEqual(
            self.sol.countUnguarded(
                m,
                n,
                g,
                w,
            ),
            7,
        )

    def test_countUnguarded2(self):
        m, n = 3, 3
        g = [[1, 1]]
        w = [[0, 1], [1, 0], [2, 1], [1, 2]]
        self.assertEqual(
            self.sol.countUnguarded(
                m,
                n,
                g,
                w,
            ),
            4,
        )

    def test_countUnguarded3(self):
        m, n = 5, 5
        g = [[1, 4], [4, 1], [0, 3]]
        w = [[3, 2]]
        self.assertEqual(
            self.sol.countUnguarded(
                m,
                n,
                g,
                w,
            ),
            3,
        )


if __name__ == '__main__':
    unittest.main()
