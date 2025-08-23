"""
Created Date: 2025-08-18
Qn: You are given an integer array cards of length 4. You have four cards, each
    containing a number in the range [1, 9]. You should arrange the numbers on
    these cards in a mathematical expression using the operators ['+', '-',
    '*', '/'] and the parentheses '(' and ')' to get the value 24.

    You are restricted with the following rules:

    - The division operator '/' represents real division, not integer division.
        - For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
    - Every operation done is between two numbers. In particular, we cannot use
      '-' as a unary operator.
        - For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1"
          is not allowed.
    - You cannot concatenate numbers together
        - For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not
          valid.

    Return true if you can get such expression that evaluates to 24, and false
    otherwise.
Link: https://leetcode.com/problems/24-game/
Notes:
    - use backtracking recursion
    - try all possibilities
"""

import math
import unittest


class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        fcards: list[float] = [x for x in cards]
        return self.solve(fcards)

    def solve(self, cards: list[float]) -> bool:
        if len(cards) == 1:
            return math.isclose(cards[0], 24, rel_tol=1e-5)

        n = len(cards)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = cards[i], cards[j]
                new_cards = [x for ind, x in enumerate(cards) if ind not in (i, j)]
                for c in self.candidates(a, b):
                    new_cards.append(c)
                    if self.solve(new_cards):
                        return True
                    new_cards.pop()
        return False

    def candidates(self, a: float, b: float) -> list[float]:
        res = [
            a + b,
            a * b,
            a - b,
            b - a,
        ]
        if b > 1e-5:
            res.append(a / b)
        if a > 1e-5:
            res.append(b / a)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_judgePoint24_1(self):
        c = [4, 1, 8, 7]
        expected = True
        self.assertEqual(expected, self.sol.judgePoint24(c))

    def test_judgePoint24_2(self):
        c = [1, 2, 1, 2]
        expected = False
        self.assertEqual(expected, self.sol.judgePoint24(c))


if __name__ == '__main__':
    unittest.main()
