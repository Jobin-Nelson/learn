"""
Created Date: 2024-11-18
Qn: You have a bomb to defuse, and your time is running out! Your informer will
    provide you with a circular array code of length of n and a key k.

    To decrypt the code, you must replace every number. All the numbers are
    replaced simultaneously.

    - If k > 0, replace the ith number with the sum of the next k numbers.
    - If k < 0, replace the ith number with the sum of the previous k numbers.
    - If k == 0, replace the ith number with 0.

    As code is circular, the next element of code[n-1] is code[0], and the
    previous element of code[0] is code[n-1].

    Given the circular array code and an integer key k, return the decrypted
    code to defuse the bomb!
Link: https://leetcode.com/problems/defuse-the-bomb/
Notes:
    - use sliding window
"""

import unittest


class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)
        res = [0] * N
        if k == 0:
            return res
        l, r, window_sum = 1, k, 0
        if k < 0:
            l = N + k
            r = N - 1

        for i in range(l, r + 1):
            window_sum += code[i]

        for i in range(N):
            res[i] = window_sum
            window_sum -= code[(l + i) % N]
            window_sum += code[(r + i + 1) % N]
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_decrypt1(self):
        c, k = [5, 7, 1, 4], 3
        expected = [12, 10, 16, 13]
        self.assertEqual(self.sol.decrypt(c, k), expected)

    def test_decrypt2(self):
        c, k = list(range(1, 5)), 0
        expected = [0] * 4
        self.assertEqual(self.sol.decrypt(c, k), expected)

    def test_decrypt3(self):
        c, k = [2, 4, 9, 3], -2
        expected = [12, 5, 6, 13]
        self.assertEqual(self.sol.decrypt(c, k), expected)


if __name__ == '__main__':
    unittest.main()
