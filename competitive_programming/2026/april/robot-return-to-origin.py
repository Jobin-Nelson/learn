"""
Created Date: 2026-04-05
Qn: There is a robot starting at the position (0, 0), the origin, on a 2D
    plane. Given a sequence of its moves, judge if this robot ends up at (0, 0)
    after it completes its moves.

    You are given a string moves that represents the move sequence of the robot
    where moves[i] represents its ith move. Valid moves are 'R' (right), 'L'
    (left), 'U' (up), and 'D' (down).

    Return true if the robot returns to the origin after it finishes all of its
    moves, or false otherwise.

    Note: The way that the robot is "facing" is irrelevant. 'R' will always
    make the robot move to the right once, 'L' will always make it move left,
    etc. Also, assume that the magnitude of the robot's movement is the same
    for each move.
Link: https://leetcode.com/problems/robot-return-to-origin/
Notes:
"""

from functools import reduce
import unittest


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for d in moves:
            if d == 'R':
                x += 1
            elif d == 'L':
                x -= 1
            elif d == 'U':
                y += 1
            elif d == 'D':
                y -= 1
        return x == 0 and y == 0

        # Functional approach
        # default = (0, 0)
        # def translate(c: str) -> tuple[int, int]:
        #     if c == 'R':
        #         return (1, 0)
        #     elif c == 'L':
        #         return (-1, 0)
        #     elif c == 'U':
        #         return (0, 1)
        #     elif c == 'D':
        #         return (0, -1)
        #     return default
        #
        # def agg(acc: tuple[int, int], node: tuple[int, int]) -> tuple[int, int]:
        #     return (acc[0] + node[0], acc[1] + node[1])
        #
        # return reduce(agg, map(translate, moves), initial=default) == default


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        m = 'UD'
        expected = True
        self.assertEqual(expected, self.sol.judgeCircle(m))

    def test2(self):
        m = 'LL'
        expected = False
        self.assertEqual(expected, self.sol.judgeCircle(m))

    def test3(self):
        m = 'ULL'
        expected = False
        self.assertEqual(expected, self.sol.judgeCircle(m))


if __name__ == '__main__':
    unittest.main()
