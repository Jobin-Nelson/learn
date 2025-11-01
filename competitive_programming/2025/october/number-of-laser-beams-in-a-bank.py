"""
Created Date: 2025-10-27
Qn: Anti-theft security devices are activated inside a bank. You are given a
    0-indexed binary string array bank representing the floor plan of the bank,
    which is an m x n 2D matrix. bank[i] represents the ith row, consisting of
    '0's and '1's. '0' means the cell is empty, while'1' means the cell has a
    security device.

    There is one laser beam between any two security devices if both conditions
    are met:

    - The two devices are located on two different rows: r1 and r2, where r1 <
      r2.
    - For each row i where r1 < i < r2, there are no security devices in the
      ith row.

    Laser beams are independent, i.e., one beam does not interfere nor join
    with another.

    Return the total number of laser beams in the bank.
Link: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
Notes:
"""

import unittest


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        res = 0
        prev = bank[0].count('1')

        for row in bank[1:]:
            cur = row.count('1')
            if cur > 0:
                res += prev * cur
                prev = cur
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        b = ["011001", "000000", "010100", "001000"]
        expected = 8
        self.assertEqual(expected, self.sol.numberOfBeams(b))

    def test2(self):
        b = ["000", "111", "000"]
        expected = 0
        self.assertEqual(expected, self.sol.numberOfBeams(b))


if __name__ == '__main__':
    unittest.main()
