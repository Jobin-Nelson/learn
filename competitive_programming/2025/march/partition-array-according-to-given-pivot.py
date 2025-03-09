"""
Created Date: 2025-03-03
Qn: You are given a 0-indexed integer array nums and an integer pivot.
    Rearrange nums such that the following conditions are satisfied:

    - Every element less than pivot appears before every element greater than
      pivot.
    - Every element equal to pivot appears in between the elements less than and
      greater than pivot.
    - The relative order of the elements less than pivot and the elements greater
      than pivot is maintained.
        - More formally, consider every pi, pj where pi is the new position of the
          ith element and pj is the new position of the jth element. If i < j and
          both elements are smaller (or larger) than pivot, then pi < pj.

    Return nums after the rearrangement.
Link: https://leetcode.com/problems/partition-array-according-to-given-pivot/
Notes:
    - use 3 lists to store smaller, same and bigger nums
"""

import unittest


class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        l, m, r = [], [], []
        for n in nums:
            if n < pivot:
                l.append(n)
            elif n > pivot:
                r.append(n)
            else:
                m.append(n)
        return l + m + r


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_pivotArray1(self):
        n = [9, 12, 5, 10, 14, 3, 10]
        p = 10
        expected = [9, 5, 3, 10, 10, 12, 14]
        self.assertEqual(expected, self.sol.pivotArray(n, p))

    def test_pivotArray2(self):
        n = [-3, 4, 3, 2]
        p = 2
        expected = [-3, 2, 4, 3]
        self.assertEqual(expected, self.sol.pivotArray(n, p))


if __name__ == '__main__':
    unittest.main()
