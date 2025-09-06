"""
Created Date: 2025-09-04
Qn: You are given three integers x, y, and z, representing the positions of
    three people on a number line:

    - x is the position of Person 1.
    - y is the position of Person 2.
    - z is the position of Person 3, who does not move.

    Both Person 1 and Person 2 move toward Person 3 at the same speed.

    Determine which person reaches Person 3 first:

    - Return 1 if Person 1 arrives first.
    - Return 2 if Person 2 arrives first.
    - Return 0 if both arrive at the same time.

    Return the result accordingly.
Link: https://leetcode.com/problems/find-closest-person/
Notes:
"""

import unittest


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = abs(z-x)
        b = abs(z-y)
        if b > a:
            return 1
        elif a > b:
            return 2
        else:
            return 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        x, y, z = 2, 7, 4
        expected = 1
        self.assertEqual(expected, self.sol.findClosest(x, y, z))

    def test2(self):
        x, y, z = 2, 5, 6
        expected = 2
        self.assertEqual(expected, self.sol.findClosest(x, y, z))

    def test3(self):
        x, y, z = 1,5,3
        expected = 0
        self.assertEqual(expected, self.sol.findClosest(x, y, z))

if __name__ == '__main__':
    unittest.main()
