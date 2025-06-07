"""
Created Date: 2025-06-03
Qn: You have n boxes labeled from 0 to n - 1. You are given four arrays:
    status, candies, keys, and containedBoxes where:

    - status[i] is 1 if the ith box is open and 0 if the ith box is closed,
    - candies[i] is the number of candies in the ith box,
    - keys[i] is a list of the labels of the boxes you can open after opening
      the ith box.
    - containedBoxes[i] is a list of the boxes you found inside the ith box.

    You are given an integer array initialBoxes that contains the labels of the
    boxes you initially have. You can take all the candies in any open box and
    you can use the keys in it to open new boxes and you also can use the boxes
    you find in it.

    Return the maximum number of candies you can get following the rules above.
Link: https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
Notes:
    - use bfs
    - use 2 states, can open and has box
"""

import unittest
from collections import deque


class Solution:
    def maxCandies(
        self,
        status: list[int],
        candies: list[int],
        keys: list[list[int]],
        containedBoxes: list[list[int]],
        initialBoxes: list[int],
    ) -> int:
        n = len(status)
        q = deque(initialBoxes)
        res = 0
        used_box, has_box = [False] * n, [False] * n
        for b in initialBoxes:
            has_box[b] = True
            if status[b]:
                q.append(b)
                used_box[b] = True
                res += candies[b]
        while q:
            box = q.popleft()
            for k in keys[box]:
                status[k] = 1
                if not used_box[k] and has_box[k]:
                    q.append(k)
                    used_box[k] = True
                    res += candies[k]

            for b in containedBoxes[box]:
                has_box[b] = True
                if not used_box[b] and status[b]:
                    q.append(b)
                    used_box[b] = True
                    res += candies[b]
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxCandies1(self):
        status = [1, 0, 1, 0]
        candies = [7, 5, 4, 100]
        keys = [[], [], [1], []]
        containedBoxes = [[1, 2], [3], [], []]
        initialBoxes = [0]
        expected = 16
        self.assertEqual(
            expected,
            self.sol.maxCandies(status, candies, keys, containedBoxes, initialBoxes),
        )

    def test_maxCandies2(self):
        status = [1, 0, 0, 0, 0, 0]
        candies = [1, 1, 1, 1, 1, 1]
        keys = [[1, 2, 3, 4, 5], [], [], [], [], []]
        containedBoxes = [[1, 2, 3, 4, 5], [], [], [], [], []]
        initialBoxes = [0]
        expected = 6
        self.assertEqual(
            expected,
            self.sol.maxCandies(status, candies, keys, containedBoxes, initialBoxes),
        )

    def test_maxCandies3(self):
        status = [1, 1, 1]
        candies = [100, 1, 100]
        keys = [[], [0, 2], []]
        containedBoxes = [[], [], []]
        initialBoxes = [1]
        expected = 1
        self.assertEqual(
            expected,
            self.sol.maxCandies(status, candies, keys, containedBoxes, initialBoxes),
        )


if __name__ == '__main__':
    unittest.main()
