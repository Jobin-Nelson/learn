"""
Created Date: 2025-01-19
Qn: Given an m x n integer matrix heightMap representing the height of each
    unit cell in a 2D elevation map, return the volume of water it can trap
    after raining.
Link: https://leetcode.com/problems/trapping-rain-water-ii/
Notes:
    - use priority queue and insert all the edge cells
"""

import unittest
import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        R, C = len(heightMap), len(heightMap[0])

        min_heap = []
        for r in range(R):
            for c in range(C):
                if r in [0, R - 1] or c in [0, C - 1]:
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        max_h = -1
        while min_heap:
            h, r, c = heapq.heappop(min_heap)
            max_h = max(max_h, h)
            res += max_h - h

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= R or nc >= C or heightMap[nr][nc] == -1:
                    continue
                heapq.heappush(min_heap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_trapRainWater1(self):
        h = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
        expected = 4
        self.assertEqual(expected, self.sol.trapRainWater(h))

    def test_trapRainWater2(self):
        h = [
            [3, 3, 3, 3, 3],
            [3, 2, 2, 2, 3],
            [3, 2, 1, 2, 3],
            [3, 2, 2, 2, 3],
            [3, 3, 3, 3, 3],
        ]
        expected = 10
        self.assertEqual(expected, self.sol.trapRainWater(h))


if __name__ == '__main__':
    unittest.main()
