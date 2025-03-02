"""
Created Date: 2025-03-02
Qn: You are given two 2D integer arrays nums1 and nums2.

    - nums1[i] = [idi, vali] indicate that the number with the id idi has a
      value equal to vali.
    - nums2[i] = [idi, vali] indicate that the number with the id idi has a
      value equal to vali.

    Each array contains unique ids and is sorted in ascending order by id.

    Merge the two arrays into one array that is sorted in ascending order by
    id, respecting the following conditions:

    - Only ids that appear in at least one of the two arrays should be included
      in the resulting array.
    - Each id should be included only once and its value should be the sum of
      the values of this id in the two arrays. If the id does not exist in one
      of the two arrays, then assume its value in that array to be 0.

    Return the resulting array. The returned array must be sorted in ascending
    order by id.
Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
Notes:
    - use two pointers
"""

import unittest


class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        i, j = 0, 0
        N1, N2 = len(nums1), len(nums2)
        res = []
        while i < N1 and j < N2:
            id1, n1 = nums1[i]
            id2, n2 = nums2[j]
            if id1 < id2:
                res.append(nums1[i])
                i += 1
            elif id1 > id2:
                res.append(nums2[j])
                j += 1
            else:
                res.append([id1, n1 + n2])
                i += 1
                j += 1
        if i < N1:
            res.extend(nums1[i:])
        if j < N2:
            res.extend(nums2[j:])
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_mergeArrays1(self):
        n1 = [[1, 2], [2, 3], [4, 5]]
        n2 = [[1, 4], [3, 2], [4, 1]]
        expected = [[1, 6], [2, 3], [3, 2], [4, 6]]
        self.assertEqual(expected, self.sol.mergeArrays(n1, n2))

    def test_mergeArrays2(self):
        n1 = [[2, 4], [3, 6], [5, 5]]
        n2 = [[1, 3], [4, 3]]
        expected = [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
        self.assertEqual(expected, self.sol.mergeArrays(n1, n2))


if __name__ == '__main__':
    unittest.main()
