"""
Created Date: 2026-05-02
Qn: An integer x is a good if after rotating each digit individually by 180
    degrees, we get a valid number that is different from x. Each digit must be
    rotated - we cannot choose to leave it alone.

    A number is valid if each digit remains a digit after rotation. For
    example:

    - 0, 1, and 8 rotate to themselves,
    - 2 and 5 rotate to each other (in this case they are rotated in a
      different direction, in other words, 2 or 5 gets mirrored),
    - 6 and 9 rotate to each other, and
    - the rest of the numbers do not rotate to any other number and become
      invalid.

    Given an integer n, return the number of good integers in the range [1, n].
Link: https://leetcode.com/problems/rotated-digits/
Notes:
"""

import unittest


class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            s = str(i)
            if any(d in s for d in ('3', '4', '7')):
                continue
            if any(d in s for d in ('2', '5', '6', '9')):
                res += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = 10
        expected = 4
        self.assertEqual(expected, self.sol.rotatedDigits(n))

    def test2(self):
        n = 1
        expected = 0
        self.assertEqual(expected, self.sol.rotatedDigits(n))

    def test3(self):
        n = 2
        expected = 1
        self.assertEqual(expected, self.sol.rotatedDigits(n))


if __name__ == '__main__':
    unittest.main()
