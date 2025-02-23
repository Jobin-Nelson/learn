"""
Created Date: 2025-02-19
Qn: A happy string is a string that:

    - consists only of letters of the set ['a', 'b', 'c'].
    - s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is
      1-indexed).

    For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy
    strings and strings "aa", "baa" and "ababbc" are not happy strings.

    Given two integers n and k, consider a list of all happy strings of length
    n sorted in lexicographical order.

    Return the kth string of this list or return an empty string if there are
    less than k happy strings of length n.
Link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
Notes:
"""

import unittest


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_happy = 3 * (2 ** (n - 1))
        res = []
        choices = "abc"
        left, right = 1, total_happy

        for _ in range(n):
            cur = left
            partition_size = (right - left + 1) // len(choices)
            for c in choices:
                if cur <= k < cur + partition_size:
                    res.append(c)
                    left = cur
                    right = cur + partition_size - 1
                    choices = "abc".replace(c, "")
                    break
                cur += partition_size
        return ''.join(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_getHappyString1(self):
        n, k = 1, 3
        expected = "c"
        self.assertEqual(expected, self.sol.getHappyString(n, k))

    def test_getHappyString2(self):
        n, k = 1, 4
        expected = ""
        self.assertEqual(expected, self.sol.getHappyString(n, k))

    def test_getHappyString3(self):
        n, k = 3, 9
        expected = "cab"
        self.assertEqual(expected, self.sol.getHappyString(n, k))


if __name__ == '__main__':
    unittest.main()
