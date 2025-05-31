"""
Created Date: 2025-05-31
Qn: You are given an n x n integer matrix board where the cells are labeled
    from 1 to n2 in a Boustrophedon style starting from the bottom left of the
    board (i.e. board[n - 1][0]) and alternating direction each row.

    You start on square 1 of the board. In each move, starting from square
    curr, do the following:

    - Choose a destination square next with a label in the range [curr + 1,
      min(curr + 6, n2)].
        - This choice simulates the result of a standard 6-sided die roll:
          i.e., there are always at most 6 destinations, regardless of the size
          of the board.
    - If next has a snake or ladder, you must move to the destination of that
      snake or ladder. Otherwise, you move to next.
    - The game ends when you reach the square n2.

    A board square on row r and column c has a snake or ladder if board[r][c]
    != -1. The destination of that snake or ladder is board[r][c]. Squares 1
    and n2 are not the starting points of any snake or ladder.

    Note that you only take a snake or ladder at most once per dice roll. If
    the destination to a snake or ladder is the start of another snake or
    ladder, you do not follow the subsequent snake or ladder.

    - For example, suppose the board is [[-1,4],[-1,3]], and on the first move,
      your destination square is 2. You follow the ladder to square 3, but do
      not follow the subsequent ladder to 4.

    Return the least number of dice rolls required to reach the square n2. If
    it is not possible to reach the square, return -1.
Link: https://leetcode.com/problems/snakes-and-ladders/
Notes:
    - use bfs
"""

import unittest
from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        N = n * n

        # setup cell board
        def get_pos(num: int) -> tuple[int, int]:
            r, c = divmod(num - 1, n)
            return (n - 1 - r, c) if r & 1 == 0 else (n - 1 - r, n - 1 - c)

        # bfs
        res = [-1] * (N + 1)
        q = deque([1])
        res[1] = 0
        while q:
            cur = q.popleft()
            for i in range(cur + 1, min(cur + 6, N) + 1):
                r, c = get_pos(i)
                destination = board[r][c] if board[r][c] != -1 else i
                if destination == N:
                    return res[cur] + 1
                if res[destination] == -1:
                    res[destination] = res[cur] + 1
                    q.append(destination)
        return res[N]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_snakesAndLadders1(self):
        b = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
        expected = 4
        self.assertEqual(expected, self.sol.snakesAndLadders(b))

    def test_snakesAndLadders2(self):
        b = [[-1, -1], [-1, 3]]
        expected = 1
        self.assertEqual(expected, self.sol.snakesAndLadders(b))

    def test_snakesAndLadders3(self):
        b = [
            [2, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
        ]
        expected = 4
        self.assertEqual(expected, self.sol.snakesAndLadders(b))

    def test_snakesAndLadders4(self):
        b = [[1, 1, -1], [1, 1, 1], [-1, 1, 1]]
        expected = -1
        self.assertEqual(expected, self.sol.snakesAndLadders(b))


if __name__ == '__main__':
    unittest.main()
