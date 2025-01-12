"""
Created Date: 2025-01-05
Qn: You are given a string s of lowercase English letters and a 2D integer
    array shifts where shifts[i] = [starti, endi, directioni]. For every i,
    shift the characters in s from the index starti to the index endi
    (inclusive) forward if directioni = 1, or shift the characters backward if
    directioni = 0.

    Shifting a character forward means replacing it with the next letter in the
    alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a
    character backward means replacing it with the previous letter in the
    alphabet (wrapping around so that 'a' becomes 'z').

    Return the final string after all such shifts to s are applied.
Link: https://leetcode.com/problems/shifting-letters-ii/
Notes:
    - use a diff array and accumulate
"""

import unittest
from itertools import accumulate


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        # Functional approach
        N = len(s)
        ord_a = ord('a')
        diff_arr = [0] * (N + 1)

        for start, end, direction in shifts:
            direction = -1 if direction == 0 else 1
            diff_arr[start] += direction
            diff_arr[end + 1] -= direction

        def shift_by(c: str, i: int) -> str:
            return chr(((ord(c) - ord_a + i) % 26) + ord_a)

        return ''.join(map(shift_by, s, accumulate(diff_arr)))

        # Imperative approach
        # N = len(s)
        # ord_a = ord('a')
        # diff_arr = [0] * (N+1)
        # ords_s = [ord(c) - ord_a for c in s]
        # for start, end, direction in shifts:
        #     direction = -1 if direction == 0 else 1
        #     diff_arr[start] += direction
        #     diff_arr[end + 1] -= direction
        #
        # cur_shift = 0
        # for i in range(N):
        #     cur_shift = (cur_shift + diff_arr[i]) % 26
        #     ords_s[i] = (ords_s[i] + cur_shift) % 26
        #
        # return ''.join(chr(ord_a + o) for o in ords_s)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_shiftingLetters1(self):
        s = "abc"
        shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
        expected = "ace"
        self.assertEqual(expected, self.sol.shiftingLetters(s, shifts))

    def test_shiftingLetters2(self):
        s = "abc"
        shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
        expected = "ace"
        self.assertEqual(expected, self.sol.shiftingLetters(s, shifts))


if __name__ == '__main__':
    unittest.main()
