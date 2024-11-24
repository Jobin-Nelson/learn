"""
Created Date: 2024-11-23
Qn:
Link: https://leetcode.com/problems/rotating-the-box/
Notes:
    - rotate 90 and simulate gravity
"""

import unittest


class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        # rotate 90 degree
        r90 = [list(l) for l in map(reversed, zip(*box))]

        # simulate gravity
        M, N = len(r90), len(r90[0])

        for c in range(N):
            vacant = None
            for r in range(M-1, -1, -1):
                if vacant is not None and r90[r][c] == '#':
                    r90[r][c] = '.'
                    r90[vacant][c] = '#'
                    while vacant >= r:
                        if r90[vacant][c] == '.':
                            break
                        vacant -= 1
                    else:
                        vacant = None
                elif vacant is None and r90[r][c] == '.':
                    vacant = r
                if r90[r][c] == '*':
                    vacant = None
        return r90


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_rotateTheBox1(self):
        b = [["#", ".", "#"]]
        expected = [["."], ["#"], ["#"]]
        self.assertEqual(self.sol.rotateTheBox(b), expected)

    def test_rotateTheBox2(self):
        b = [["#", ".", "*", "."], ["#", "#", "*", "."]]
        expected = [["#", "."], ["#", "#"], ["*", "*"], [".", "."]]
        self.assertEqual(self.sol.rotateTheBox(b), expected)

    def test_rotateTheBox3(self):
        b = [
            ["#", "#", "*", ".", "*", "."],
            ["#", "#", "#", "*", ".", "."],
            ["#", "#", "#", ".", "#", "."],
        ]
        expected = [
            [".", "#", "#"],
            [".", "#", "#"],
            ["#", "#", "*"],
            ["#", "*", "."],
            ["#", ".", "*"],
            ["#", ".", "."],
        ]
        self.assertEqual(self.sol.rotateTheBox(b), expected)


if __name__ == '__main__':
    unittest.main()
