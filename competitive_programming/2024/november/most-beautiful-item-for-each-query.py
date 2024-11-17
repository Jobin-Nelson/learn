"""
Created Date: 2024-11-12
Qn: ou are given a 2D integer array items where items[i] = [pricei, beautyi]
    denotes the price and beauty of an item respectively.

    You are also given a 0-indexed integer array queries. For each queries[j],
    you want to determine the maximum beauty of an item whose price is less
    than or equal to queries[j]. If no such item exists, then the answer to
    this query is 0.

    Return an array answer of the same length as queries where answer[j] is the
    answer to the jth query.
Link: https://leetcode.com/problems/most-beautiful-item-for-each-query/
Notes:
"""

import unittest


class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort()
        sorted_q = sorted(enumerate(queries), key=lambda x: x[1])
        res = [0] * len(queries)
        i = 0
        N = len(items)
        max_b = 0
        for (j, q) in sorted_q:
            while i < N and items[i][0] <= q:
                max_b = max(max_b, items[i][1])
                i += 1
            res[j] = max_b
        return res
            
        # Binary search approach
        # items.sort()
        # N = len(items)
        # prefix_beauty = [0] * N
        # prefix_beauty[0] = items[0][1]
        # for i in range(1, N):
        #     prefix_beauty[i] = max(items[i][1], prefix_beauty[i - 1])
        # res = [0] * len(queries)
        # for i, q in enumerate(queries):
        #     l, r = 0, N - 1
        #     max_b = 0
        #     while l <= r:
        #         m = l + ((r - l) >> 1)
        #         if items[m][0] <= q:
        #             max_b = items[m][1]
        #             l = m + 1
        #         else:
        #             r = m - 1
        #     res[i] = max_b
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumBeauty1(self):
        items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
        queries = list(range(1, 7))
        expected = [2, 4, 5, 5, 6, 6]
        self.assertEqual(self.sol.maximumBeauty(items, queries), expected)

    def test_maximumBeauty2(self):
        items = [[1, 2], [1, 2], [1, 3], [1, 4]]
        queries = [1]
        expected = [4]
        self.assertEqual(self.sol.maximumBeauty(items, queries), expected)

    def test_maximumBeauty3(self):
        items = [[10, 1000]]
        queries = [5]
        expected = [0]
        self.assertEqual(self.sol.maximumBeauty(items, queries), expected)


if __name__ == '__main__':
    unittest.main()
