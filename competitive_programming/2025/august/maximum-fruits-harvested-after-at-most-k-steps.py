"""
Created Date: 2025-08-03
Qn: Fruits are available at some positions on an infinite x-axis. You are given
    a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts
    amounti fruits at the position positioni. fruits is already sorted by
    positioni in ascending order, and each positioni is unique.

    You are also given an integer startPos and an integer k. Initially, you are
    at the position startPos. From any position, you can either walk to the
    left or right. It takes one step to move one unit on the x-axis, and you
    can walk at most k steps in total. For every position you reach, you
    harvest all the fruits at that position, and the fruits will disappear from
    that position.

    Return the maximum total number of fruits you can harvest.
Link: https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
Notes:
    - sliding window
    - get the number of steps when iterating through the fruits
"""

import unittest


class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        left, right = 0, 0
        cur_sum = 0
        n = len(fruits)
        res = 0

        def step(left: int, right: int) -> int:
            if fruits[right][0] <= startPos:
                return startPos - fruits[left][0]
            elif fruits[left][0] >= startPos:
                return fruits[right][0] - startPos
            else:
                return (
                    min(
                        abs(startPos - fruits[right][0]),
                        abs(startPos - fruits[left][0]),
                    )
                    + fruits[right][0]
                    - fruits[left][0]
                )

        while right < n:
            cur_sum += fruits[right][1]
            while left <= right and step(left, right) > k:
                cur_sum -= fruits[left][1]
                left += 1
            res = max(res, cur_sum)
            right += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxTotalFruits1(self):
        f = [[2, 8], [6, 3], [8, 6]]
        s, k = 5, 4
        expected = 9
        self.assertEqual(expected, self.sol.maxTotalFruits(f, s, k))

    def test_maxTotalFruits2(self):
        f = [[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]]
        s, k = 5, 4
        expected = 14
        self.assertEqual(expected, self.sol.maxTotalFruits(f, s, k))

    def test_maxTotalFruits3(self):
        f = [[0, 3], [6, 4], [8, 5]]
        s, k = 3, 2
        expected = 0
        self.assertEqual(expected, self.sol.maxTotalFruits(f, s, k))


if __name__ == '__main__':
    unittest.main()
