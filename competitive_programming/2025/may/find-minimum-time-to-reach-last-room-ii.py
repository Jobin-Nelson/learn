"""
Created Date: 2025-05-08
Qn: There is a dungeon with n x m rooms arranged as a grid.

    You are given a 2D array moveTime of size n x m, where moveTime[i][j]
    represents the minimum time in seconds when you can start moving to that
    room. You start from the room (0, 0) at time t = 0 and can move to an
    adjacent room. Moving between adjacent rooms takes one second for one move
    and two seconds for the next, alternating between the two.

    Return the minimum time to reach the room (n - 1, m - 1).

    Two rooms are adjacent if they share a common wall, either horizontally or
    vertically.
Link: https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/
Notes:
    - use bfs and heap
"""

import unittest
import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        R, C = len(moveTime), len(moveTime[0])
        visited = [[False] * C for _ in range(R)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        h = [(0,0,0,1)]

        while h:
            cost, r, c, add_cost = heapq.heappop(h)
            if r == R - 1 and c == C - 1:
                return cost
            next_cost = 2 if add_cost == 1 else 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    visited[nr][nc] = True
                    new_cost = max(cost, moveTime[nr][nc]) + add_cost
                    heapq.heappush(h, (new_cost, nr, nc, next_cost))
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minTimeToReach1(self):
        m = [[0,4],[4,4]]
        expected = 7
        self.assertEqual(expected, self.sol.minTimeToReach(m))

    def test_minTimeToReach2(self):
        m = [[0,0,0,0],[0,0,0,0]]
        expected = 6
        self.assertEqual(expected, self.sol.minTimeToReach(m))

    def test_minTimeToReach3(self):
        m = [[0,1],[1,2]]
        expected = 4
        self.assertEqual(expected, self.sol.minTimeToReach(m))


if __name__ == '__main__':
    unittest.main()
