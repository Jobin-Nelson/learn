"""
Created Date: 2025-06-23
Qn: A k-mirror number is a positive integer without leading zeros that reads
    the same both forward and backward in base-10 as well as in base-k.

    - For example, 9 is a 2-mirror number. The representation of 9 in base-10
      and base-2 are 9 and 1001 respectively, which read the same both forward
      and backward.
    - On the contrary, 4 is not a 2-mirror number. The representation of 4 in
      base-2 is 100, which does not read the same both forward and backward.

    Given the base k and the number n, return the sum of the n smallest
    k-mirror numbers.
Link: https://leetcode.com/problems/sum-of-k-mirror-numbers/
Notes:
    - use binary search
"""

import unittest


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_mirror(num: int, base: int) -> bool:
            digits = []
            while num:
                digits.append(num % base)
                num //= base
            return digits == digits[::-1]

        left, count, res = 1, 0, 0
        while count < n:
            right = left * 10
            for op in [0, 1]:
                for i in range(left, right):
                    if count == n:
                        break

                    combined = i
                    x = i // 10 if op == 0 else i
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if is_mirror(combined, k):
                        count += 1
                        res += combined
            left = right
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_kMirror1(self):
        k, n = 2, 5
        expected = 25
        self.assertEqual(expected, self.sol.kMirror(k, n))

    def test_kMirror2(self):
        k, n = 3, 7
        expected = 499
        self.assertEqual(expected, self.sol.kMirror(k, n))

    def test_kMirror3(self):
        k, n = 7, 17
        expected = 20379000
        self.assertEqual(expected, self.sol.kMirror(k, n))


if __name__ == '__main__':
    unittest.main()
