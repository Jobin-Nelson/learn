"""
Created Date: 2024-12-22
Qn: You are given a 0-indexed array heights of positive integers, where
    heights[i] represents the height of the ith building.

    If a person is in building i, they can move to any other building j if and
    only if i < j and heights[i] < heights[j].

    You are also given another array queries where queries[i] = [ai, bi]. On
    the ith query, Alice is in building ai while Bob is in building bi.

    Return an array ans where ans[i] is the index of the leftmost building
    where Alice and Bob can meet on the ith query. If Alice and Bob cannot move
    to a common building on query i, set ans[i] to -1.
Link: https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/
Notes:
    - use heap
"""

import unittest
from collections import defaultdict
import heapq


class Solution:
    def leftmostBuildingQueries(
        self, heights: list[int], queries: list[list[int]]
    ) -> list[int]:
        res = [-1] * len(queries)
        groups = defaultdict(list)

        for i, q in enumerate(queries):
            l, r = sorted(q)

            if l == r or heights[r] > heights[l]:
                res[i] = r
            else:
                h = max(heights[l], heights[r])
                groups[r].append((h, i))
        min_heap = []
        for i, h in enumerate(heights):
            for q_h, q_i in groups[i]:
                heapq.heappush(min_heap, (q_h, q_i))
            while min_heap and h > min_heap[0][0]:
                q_h, q_i = heapq.heappop(min_heap)
                res[q_i] = i
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_leftmostBuildingQueries1(self):
        h = [6, 4, 8, 5, 2, 7]
        q = [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
        expected = [2, 5, -1, 5, 2]
        self.assertEqual(expected, self.sol.leftmostBuildingQueries(h, q))

    def test_leftmostBuildingQueries2(self):
        h = [5, 3, 8, 2, 6, 1, 4, 6]
        q = [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]
        expected = [7, 6, -1, 4, 6]
        self.assertEqual(expected, self.sol.leftmostBuildingQueries(h, q))


if __name__ == '__main__':
    unittest.main()
