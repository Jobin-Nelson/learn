"""
Created Date: 2026-05-20
Qn: You are given two 0-indexed integer permutations A and B of length n.

    A prefix common array of A and B is an array C such that C[i] is equal to
    the count of numbers that are present at or before the index i in both A
    and B.

    Return the prefix common array of A and B.

    A sequence of n integers is called a permutation if it contains all
    integers from 1 to n exactly once.
Link: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
Notes:
    - use hashset
"""

import unittest


class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        pa, pb = set(), set()
        res = [0] * len(A)
        count = 0
        for i, (a, b) in enumerate(zip(A, B)):
            pa.add(a)
            pb.add(b)
            if a == b:
                if a in pb or b in pa:
                    count += 1
            else:
                if a in pb:
                    count += 1
                if b in pa:
                    count += 1
            res[i] = count
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A, B = [1, 3, 2, 4], [3, 1, 2, 4]
        expected = [0, 2, 3, 4]
        self.assertEqual(expected, self.sol.findThePrefixCommonArray(A, B))

    def test2(self):
        A, B = [2, 3, 1], [3, 1, 2]
        expected = [0, 1, 3]
        self.assertEqual(expected, self.sol.findThePrefixCommonArray(A, B))


if __name__ == '__main__':
    unittest.main()
