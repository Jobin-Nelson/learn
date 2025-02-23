"""
Created Date: 2025-02-20
Qn: Given an array of strings nums containing n unique binary strings each of
    length n, return a binary string of length n that does not appear in nums.
    If there are multiple answers, you may return any of them.
Link: https://leetcode.com/problems/find-unique-binary-string/
Notes:
    - to be a unique string it has to differ in atleast one character
    - construct a string that is different from each input string in atleast
      one character
"""

import unittest


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        res = []
        for i, n in enumerate(nums):
            res.append("1" if n[i] == "0" else "0")
        return "".join(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findDifferentBinaryString1(self):
        n = ["01", "10"]
        expected = "11"
        self.assertEqual(expected, self.sol.findDifferentBinaryString(n))

    def test_findDifferentBinaryString2(self):
        n = ["00", "01"]
        expected = "10"
        self.assertEqual(expected, self.sol.findDifferentBinaryString(n))

    def test_findDifferentBinaryString3(self):
        n = ["111", "011", "001"]
        expected = "000"
        self.assertEqual(expected, self.sol.findDifferentBinaryString(n))


if __name__ == '__main__':
    unittest.main()
