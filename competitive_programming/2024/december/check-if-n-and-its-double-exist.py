"""
Created Date: 2024-12-01
Qn: Given an array arr of integers, check if there exist two indices i and j
    such that :

    - i != j
    - 0 <= i, j < arr.length
    - arr[i] == 2 * arr[j]
Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/
Notes:
    - use hashset
"""

import unittest


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()
        for num in arr:
            if 2 * num in seen or (num & 1 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_checkIfExist1(self):
        a = [10, 2, 5, 3]
        self.assertEqual(self.sol.checkIfExist(a), True, '10 is double of 5')

    def test_checkIfExist2(self):
        a = [3, 1, 7, 11]
        self.assertEqual(
            self.sol.checkIfExist(a),
            False,
            'There is no i and j that satisfy the condition',
        )


if __name__ == '__main__':
    unittest.main()
