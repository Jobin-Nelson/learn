"""
Created Date: 2025-02-18
Qn: You are given a 0-indexed string pattern of length n consisting of the
    characters 'I' meaning increasing and 'D' meaning decreasing.

    A 0-indexed string num of length n + 1 is created using the following
    conditions:

    - num consists of the digits '1' to '9', where each digit is used at most
      once.
    - If pattern[i] == 'I', then num[i] < num[i + 1].
    - If pattern[i] == 'D', then num[i] > num[i + 1].

    Return the lexicographically smallest possible string num that meets the
    conditions.
Link: https://leetcode.com/problems/construct-smallest-number-from-di-string/
Notes:
    - use stack
"""

import unittest


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []
        for i in range(len(pattern)+1):
            stack.append(i+1)
            while stack and (i == len(pattern) or pattern[i] == "I"):
                res.append(str(stack.pop()))
        return ''.join(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_smallestNumber1(self):
        p = "IIIDIDDD"
        expected = "123549876"
        self.assertEqual(expected, self.sol.smallestNumber(p))

    def test_smallestNumber2(self):
        p = "DDD"
        expected = "4321"
        self.assertEqual(expected, self.sol.smallestNumber(p))


if __name__ == '__main__':
    unittest.main()
