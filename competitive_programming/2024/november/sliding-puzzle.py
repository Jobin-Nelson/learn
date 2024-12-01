"""
Created Date: 2024-11-25
Qn: On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty
    square represented by 0. A move consists of choosing 0 and a
    4-directionally adjacent number and swapping it.

    The state of the board is solved if and only if the board is
    [[1,2,3],[4,5,0]].

    Given the puzzle board board, return the least number of moves required so
    that the state of the board is solved. If it is impossible for the state of
    the board to be solved, return -1.
Link: https://leetcode.com/problems/sliding-puzzle/
Notes:
    - use brute force
"""

import unittest
from collections import deque


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }
        b = ''.join(str(c) for row in board for c in row)
        q = deque([((b.index('0'), b, 0))]) # i, b, length
        visit = set([b])
        expected = '123450'
        while q:
            i, b, length = q.popleft()
            if b == expected:
                return length
            for j in adj[i]:
                bc_arr = list(b)
                bc_arr[j], bc_arr[i] = b[i], b[j]
                bc = ''.join(bc_arr)
                if bc not in visit:
                    q.append((j, bc, length+1))
                    visit.add(bc)
        return -1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_slidingPuzzle1(self):
        b = [[1, 2, 3], [4, 0, 5]]
        self.assertEqual(self.sol.slidingPuzzle(b), 1)

    def test_slidingPuzzle2(self):
        b = [[1, 2, 3], [5, 4, 0]]
        self.assertEqual(self.sol.slidingPuzzle(b), -1)

    def test_slidingPuzzle3(self):
        b = [[4, 1, 2], [5, 0, 3]]
        self.assertEqual(self.sol.slidingPuzzle(b), 5)


if __name__ == '__main__':
    unittest.main()
