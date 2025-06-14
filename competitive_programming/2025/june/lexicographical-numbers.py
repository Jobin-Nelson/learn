"""
Created Date: 2025-06-08
Qn: Given an integer n, return all the numbers in the range [1, n] sorted in
    lexicographical order.

    You must write an algorithm that runs in O(n) time and uses O(1) extra
    space.
Link: https://leetcode.com/problems/lexicographical-numbers/
Notes:
"""

import unittest


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []
        current_num = 1
        for _ in range(n):
            res.append(current_num)
            if current_num * 10 <= n:
                current_num *= 10
            else:
                while current_num % 10 == 9 or current_num >= n:
                    current_num //= 10
                current_num += 1
        return res

        # return sorted(range(1,n+1), key=lambda x: str(x))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_lexicalOrder1(self):
        n = 13
        expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected, self.sol.lexicalOrder(n))

    def test_lexicalOrder2(self):
        n = 2
        expected = [1, 2]
        self.assertEqual(expected, self.sol.lexicalOrder(n))


if __name__ == '__main__':
    unittest.main()
