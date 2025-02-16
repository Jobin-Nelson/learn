"""
Created Date: 2025-02-15
Qn: Given a positive integer n, return the punishment number of n.

    The punishment number of n is defined as the sum of the squares of all
    integers i such that:

    - 1 <= i <= n
    - The decimal representation of i * i can be partitioned into contiguous
      substrings such that the sum of the integer values of these substrings
      equals i.
Link: https://leetcode.com/problems/find-the-punishment-number-of-an-integer/
Notes:
"""

import unittest


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(i: int, cur: int, target: int, string: str) -> bool:
            if i == len(string) and cur == target:
                return True
            for j in range(i, len(string)):
                if partition(j+1, cur + int(string[i:j+1]), target, string):
                    return True
            return False
        res = 0
        for i in range(1, n+1):
            if partition(0,0,i,str(i*i)):
                res += i * i
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_punishmentNumber1(self):
        n = 10
        expected = 182
        self.assertEqual(expected, self.sol.punishmentNumber(n))

    def test_punishmentNumber2(self):
        n = 37
        expected = 1478
        self.assertEqual(expected, self.sol.punishmentNumber(n))


if __name__ == '__main__':
    unittest.main()
