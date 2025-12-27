"""
Created Date: 2025-12-21
Qn: You are given an array of n strings strs, all of the same length.

    We may choose any deletion indices, and we delete all the characters in
    those indices for each string.

    For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0,
    2,
    3}, then the final array after deletions is ["bef", "vyz"].

    Suppose we chose a set of deletion indices answer such that after
    deletions, the final array has its elements in lexicographic order (i.e.,
    strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum
    possible value of answer.length.
Link: https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
Notes:
"""

import unittest


class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        def is_sorted(arr: list[str]) -> bool:
            return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
        res = 0
        cur = [''] * len(strs)
        for col in zip(*strs, strict=True):
            cur2 = cur[:]

            for i, letter in enumerate(col):
                cur2[i] = cur2[i] + letter

            if is_sorted(cur2):
                cur = cur2
            else:
                res += 1
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1(self):
        s = ["ca", "bb", "ac"]
        expected = 1
        self.assertEqual(expected, self.sol.minDeletionSize(s))

    def test_2(self):
        s = ["xc", "yb", "za"]
        expected = 0
        self.assertEqual(expected, self.sol.minDeletionSize(s))

    def test_3(self):
        s = ["zyx", "wvu", "tsr"]
        expected = 3
        self.assertEqual(expected, self.sol.minDeletionSize(s))


if __name__ == '__main__':
    unittest.main()
