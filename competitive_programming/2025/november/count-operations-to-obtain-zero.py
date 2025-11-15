"""
Created Date: 2025-11-09
Qn: You are given two non-negative integers num1 and num2.

    In one operation, if num1 >= num2, you must subtract num2 from num1,
    otherwise subtract num1 from num2.

    For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus
    obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after
    one operation, num1 = 4 and num2 = 1. Return the number of operations
    required to make either num1 = 0 or num2 = 0.
Link: https://leetcode.com/problems/count-operations-to-obtain-zero/
Notes:
"""

import unittest


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            res += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n1, n2 = 2, 3
        expected = 3
        self.assertEqual(expected, self.sol.countOperations(n1, n2))

    def test2(self):
        n1, n2 = 10, 10
        expected = 1
        self.assertEqual(expected, self.sol.countOperations(n1, n2))


if __name__ == '__main__':
    unittest.main()
