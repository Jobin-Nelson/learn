"""
Created Date: 2025-02-23
Qn: Given two integer arrays, preorder and postorder where preorder is the
    preorder traversal of a binary tree of distinct values and postorder is the
    postorder traversal of the same tree, reconstruct and return the binary
    tree.

    If there exist multiple answers, you can return any of them.
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
Notes:
    - use dfs
"""

from collections import deque
from typing import Self
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
                return
            node = cls(arr[i])
            node.left = inner(i * 2 + 1)
            node.right = inner(i * 2 + 2)
            return node

        return inner(0)

    def __repr__(self) -> str:
        res = []
        q = deque([self])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return str(res)

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, TreeNode):
            return False
        q1, q2 = deque([self]), deque([other])
        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()
            if n1.val != n2.val:
                return False
            if n1.left:
                q1.append(n1.left)
            if n1.right:
                q1.append(n1.right)
            if n2.left:
                q2.append(n2.left)
            if n2.right:
                q2.append(n2.right)
        return not q1 and not q2


class Solution:
    def constructFromPrePost(
        self, preorder: list[int], postorder: list[int]
    ) -> TreeNode | None:
        N = len(preorder)
        post_val_to_ind = {n: i for i, n in enumerate(postorder)}

        def build(i1: int, i2: int, j1: int, j2: int) -> TreeNode | None:
            if i1 > i2 or j1 > j2:
                return

            root = TreeNode(preorder[i1])
            if i1 != i2:
                left_val = preorder[i1 + 1]
                mid = post_val_to_ind[left_val]
                left_size = mid - j1 + 1
                root.left = build(i1 + 1, i1 + left_size, j1, mid)
                root.right = build(i1 + left_size + 1, i2, mid + 1, j2 - 1)
            return root

        return build(0, N - 1, 0, N - 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_constructFromPrePost1(self):
        pre, post = [1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]
        expected = TreeNode.from_list([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(expected, self.sol.constructFromPrePost(pre, post))

    def test_constructFromPrePost2(self):
        pre, post = [1], [1]
        expected = TreeNode.from_list([1])
        self.assertEqual(expected, self.sol.constructFromPrePost(pre, post))


if __name__ == '__main__':
    unittest.main()
