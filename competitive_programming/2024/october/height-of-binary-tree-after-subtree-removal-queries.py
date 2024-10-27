"""
Created Date: 2024-10-26
Qn: You are given the root of a binary tree with n nodes. Each node is assigned
    a unique value from 1 to n. You are also given an array queries of size m.

    You have to perform m independent queries on the tree where in the ith
    query you do the following:

    - Remove the subtree rooted at the node with the value queries[i] from the
      tree. It is guaranteed that queries[i] will not be equal to the value of
      the root. Return an array answer of size m where answer[i] is the height
      of the tree after performing the ith query.

    Note:

    - The queries are independent, so the tree returns to its initial state
      after each query.
    - The height of a tree is the number of edges in the longest simple path
      from the root to some node in the tree.
Link: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
Notes:
    - use depth + subtree height
"""

import unittest
from collections import deque
from typing import Self


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        def inner(i: int) -> Self | None:
            if i >= len(arr) or arr[i] is None:
                return
            node = cls(arr[i])
            node.left = inner(i * 2 + 1)
            node.right = inner(i * 2 + 2)
            return node

        return inner(0)

    def __str__(self) -> str:
        q = deque([self])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()


class Solution:
    def treeQueries(self, root: TreeNode | None, queries: list[int]) -> list[int]:
        node_depths = {}
        subtree_heights = {}

        first_largest_heights = {}
        second_largest_heights = {}

        def dfs(node: TreeNode | None, level: int) -> int:
            if node is None:
                return 0
            node_depths[node.val] = level
            left_height = dfs(node.left, level + 1)
            right_height = dfs(node.right, level + 1)
            current_height = 1 + max(left_height, right_height)

            subtree_heights[node.val] = current_height
            if current_height > first_largest_heights.get(level, 0):
                second_largest_heights[level] = first_largest_heights.get(level, 0)
                first_largest_heights[level] = current_height
            elif current_height > second_largest_heights.get(level, 0):
                second_largest_heights[level] = current_height
            return current_height

        dfs(root, 0)

        return [
            node_depths[q]
            + (
                second_largest_heights.get(node_depths[q], 0)
                if subtree_heights[q] == first_largest_heights[node_depths[q]]
                else first_largest_heights[node_depths[q]]
            )
            - 1
            for q in queries
        ]


class TestMain(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def helper(self, root: list[int | None], queries: list[int], expected: list[int]):
        r = TreeNode.from_list(root)
        actual = self.sol.treeQueries(r, queries)
        self.assertEqual(actual, expected)

    def test_treeQueries1(self):
        r = [1, 3, 4, 2, None, 6, 5, None, None, None, None, None, 7]
        q = [4]
        expected = [2]
        self.helper(r, q, expected)

    def test_treeQueries2(self):
        r: list[int | None] = [5, 8, 9, 2, 1, 3, 7, 4, 6]
        q = [3, 2, 4, 8]
        expected = [3, 2, 3, 2]
        self.helper(r, q, expected)


if __name__ == '__main__':
    unittest.main()
