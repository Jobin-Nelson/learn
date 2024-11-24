"""
Created Date: 2024-11-20
Qn: You are given a string s consisting of the characters 'a', 'b', and 'c' and
    a non-negative integer k. Each minute, you may take either the leftmost
    character of s, or the rightmost character of s.

    Return the minimum number of minutes needed for you to take at least k of
    each character, or return -1 if it is not possible to take k of each
    character.
Link: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/
Notes:
    - use sliding window to determine which window we can avoid and still
      statisfy the condition
"""

import unittest


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        N = len(s)
        count = [0] * 3
        ord_a = ord('a')
        for c in s:
            count[ord(c) - ord_a] += 1
        if any(c < k for c in count):
            return -1
        window = [0] * 3
        l, max_window = 0, 0
        for r in range(N):
            window[ord(s[r]) - ord_a] += 1
            while l <= r and any(count[i] - window[i] < k for i in range(3)):
                window[ord(s[l]) - ord_a] -= 1
                l += 1
            max_window = max(max_window, r - l + 1)
        return N - max_window


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_takeCharacters1(self):
        s, k = "aabaaaacaabc", 2
        self.assertEqual(self.sol.takeCharacters(s, k), 8)

    def test_takeCharacters2(self):
        s, k = "a", 1
        self.assertEqual(self.sol.takeCharacters(s, k), -1)


if __name__ == '__main__':
    unittest.main()
