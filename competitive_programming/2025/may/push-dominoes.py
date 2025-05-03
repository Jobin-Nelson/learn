"""
Created Date: 2025-05-02
Qn: There are n dominoes in a line, and we place each domino vertically
    upright. In the beginning, we simultaneously push some of the dominoes
    either to the left or to the right.

    After each second, each domino that is falling to the left pushes the
    adjacent domino on the left. Similarly, the dominoes falling to the right
    push their adjacent dominoes standing on the right.

    When a vertical domino has dominoes falling on it from both sides, it stays
    still due to the balance of the forces.

    For the purposes of this question, we will consider that a falling domino
    expends no additional force to a falling or already fallen domino.

    You are given a string dominoes representing the initial state where:

    - dominoes[i] = 'L', if the ith domino has been pushed to the left,
    - dominoes[i] = 'R', if the ith domino has been pushed to the right, and
    - dominoes[i] = '.', if the ith domino has not been pushed.

    Return a string representing the final state.

Link: https://leetcode.com/problems/push-dominoes/
Notes:
"""

import unittest


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        f = 0
        for i in range(n):
            if dominoes[i] == 'R': f = n
            elif dominoes[i] == 'L': f = 0
            else: f = max(f-1, 0)
            forces[i] += f

        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L': f = n
            elif dominoes[i] == 'R': f = 0
            else: f = max(f-1, 0)
            forces[i] -= f
        return ''.join('.' if f == 0 else 'R' if f > 0 else 'L' for f in forces)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_pushDominoes1(self):
        d = "RR.L"
        expected = "RR.L"
        self.assertEqual(expected, self.sol.pushDominoes(d))

    def test_pushDominoes2(self):
        d = ".L.R...LR..L.."
        expected = "LL.RR.LLRRLL.."
        self.assertEqual(expected, self.sol.pushDominoes(d))


if __name__ == '__main__':
    unittest.main()
