"""
Created Date: 2025-08-04
Qn: You are visiting a farm that has a single row of fruit trees arranged from
    left to right. The trees are represented by an integer array fruits where
    fruits[i] is the type of fruit the ith tree produces.

    You want to collect as much fruit as possible. However, the owner has some
    strict rules that you must follow:

    - You only have two baskets, and each basket can only hold a single type of
      fruit. There is no limit on the amount of fruit each basket can hold.
    - Starting from any tree of your choice, you must pick exactly one fruit
      from every tree (including the start tree) while moving to the right. The
      picked fruits must fit in one of your baskets.
    - Once you reach a tree with fruit that cannot fit in your baskets, you
      must stop.

    Given the integer array fruits, return the maximum number of fruits you can
    pick.
Link: https://leetcode.com/problems/fruit-into-baskets/
Notes:
"""

import unittest
from collections import Counter


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count = Counter()
        left, cur_total, res = 0, 0, 0

        for fruit in fruits:
            count[fruit] += 1
            cur_total += 1

            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                cur_total -= 1
                left += 1
                if not count[left_fruit]:
                    count.pop(left_fruit)
            res = max(res, cur_total)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_totalFruit1(self):
        f = [1, 2, 1]
        expected = 3
        self.assertEqual(expected, self.sol.totalFruit(f))

    def test_totalFruit2(self):
        f = [0, 1, 2, 2]
        expected = 3
        self.assertEqual(expected, self.sol.totalFruit(f))

    def test_totalFruit3(self):
        f = [1, 2, 3, 2, 2]
        expected = 4
        self.assertEqual(expected, self.sol.totalFruit(f))


if __name__ == '__main__':
    unittest.main()
