"""
Created Date: 2025-07-23
Qn: You are given a string s and two integers x and y. You can perform two
    types of operations any number of times.

    - Remove substring "ab" and gain x points.
        - For example, when removing "ab" from "cabxbae" it becomes "cxbae".
    - Remove substring "ba" and gain y points.
        - For example, when removing "ba" from "cabxbae" it becomes "cabxe".

    Return the maximum points you can gain after applying the above operations
    on s.
Link: https://leetcode.com/problems/maximum-score-from-removing-substrings/
Notes:
    - always make x greater and y and reverse string if needed keeping "ab"
      with maximum value
    - count a, b value
"""

import unittest


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s[::-1]
            x, y = y, x
        a_count, b_count, total_points = 0, 0, 0

        for c in s:
            if c == "a":
                a_count += 1
            elif c == "b":
                if a_count > 0:
                    a_count -= 1
                    total_points += x
                else:
                    b_count += 1
            else:
                total_points += min(a_count, b_count) * y
                a_count, b_count = 0, 0
        total_points += min(a_count, b_count) * y
        return total_points


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumGain1(self):
        s = "cdbcbbaaabab"
        x, y = 4, 5
        expected = 19
        self.assertEqual(expected, self.sol.maximumGain(s, x, y))

    def test_maximumGain2(self):
        s = "aabbaaxybbaabb"
        x, y = 5, 4
        expected = 20
        self.assertEqual(expected, self.sol.maximumGain(s, x, y))


if __name__ == '__main__':
    unittest.main()
