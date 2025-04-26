"""
Created Date: 2025-04-14
Qn: Given an array of integers arr, and three integers a, b and c. You need to
    find the number of good triplets.

    A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are
    true:

    - 0 <= i < j < k < arr.length
    - |arr[i] - arr[j]| <= a
    - |arr[j] - arr[k]| <= b
    - |arr[i] - arr[k]| <= c

    Where |x| denotes the absolute value of x.

    Return the number of good triplets.
Link: https://leetcode.com/problems/count-good-triplets/
Notes:
"""

import unittest


class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        res = 0
        n = len(arr)
        prefix_count = [0] * 1001

        for j in range(n-1):
            for k in range(j+1, n):
                if abs(arr[j] - arr[k]) <= b:
                    r = min(arr[j] + a, arr[k] + c, 1000)
                    l = max(0, arr[j] - a, arr[k] - c)
                    if l <= r:
                        res += prefix_count[r] - (0 if l == 0 else prefix_count[l-1])
            for index in range(arr[j], 1001):
                prefix_count[index] += 1
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countGoodTriplets1(self):
        arr = [3, 0, 1, 1, 9, 7]
        a, b, c = 7, 2, 3
        expected = 4
        self.assertEqual(expected, self.sol.countGoodTriplets(arr, a, b, c))

    def test_countGoodTriplets2(self):
        arr = [1, 1, 2, 2, 3]
        a, b, c = 0, 0, 1
        expected = 0
        self.assertEqual(expected, self.sol.countGoodTriplets(arr, a, b, c))


if __name__ == '__main__':
    unittest.main()
