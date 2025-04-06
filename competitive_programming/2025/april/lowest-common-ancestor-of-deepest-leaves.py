"""
Created Date: 2025-04-04
Qn: Given the root of a binary tree, return the lowest common ancestor of its
    deepest leaves.

    Recall that:

    - The node of a binary tree is a leaf if and only if it has no children
    - The depth of the root of the tree is 0. if the depth of a node is d, the
      depth of each of its children is d + 1.
    - The lowest common ancestor of a set S of nodes, is the node A with the
      largest depth such that every node in S is in the subtree with root A.
Link: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
Notes:
    - use dfs
"""

from typing import Self
from collections import deque
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        N = len(arr)

        def inner(i: int) -> Self | None:
            if i >= N or arr[i] is None:
                return None
            node = cls(arr[i])
            node.left = inner(i * 2 + 1)
            node.right = inner(i * 2 + 2)
            return node

        return inner(0)

    def __repr__(self) -> str:
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


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(node: TreeNode | None) -> tuple[int, TreeNode | None]:
            if not node:
                return (0, None)
            left = dfs(node.left)
            right = dfs(node.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, node

        return dfs(root)[1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_lcaDeepestLeaves1(self):
        r = TreeNode.from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        expected = [2, 7, 4]
        self.assertEqual(expected, self.sol.lcaDeepestLeaves(r))

    def test_lcaDeepestLeaves2(self):
        r = TreeNode.from_list([1])
        expected = [2]
        self.assertEqual(expected, self.sol.lcaDeepestLeaves(r))

    def test_lcaDeepestLeaves3(self):
        r = TreeNode.from_list([0, 1, 3, None, 2])
        expected = [2]
        self.assertEqual(expected, self.sol.lcaDeepestLeaves(r))


if __name__ == '__main__':
    unittest.main()
