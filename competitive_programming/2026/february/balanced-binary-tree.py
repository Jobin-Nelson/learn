"""
Created Date: 2026-02-08
Qn: Given a binary tree, determine if it is height-balanced
Link: https://leetcode.com/problems/balanced-binary-tree/
Notes:
"""

import unittest
from collections import deque
from typing import Self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        n = len(arr)

        def inner(i: int) -> Self | None:
            if i >= n or arr[i] is None:
                return None
            node = cls(arr[i])
            node.left = inner(2 * i + 1)
            node.right = inner(2 * i + 2)
            return node

        return inner(0)

    def __str__(self):
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

    def __repr__(self):
        return self.__str__()


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None) -> tuple[bool, int]:
            if node is None:
                return (True, 0)
            left, right = dfs(node.left), dfs(node.right)
            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return (is_balanced, 1 + max(left[1], right[1]))

        return dfs(root)[0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        t = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        expected = True
        self.assertEqual(expected, self.sol.isBalanced(t))

    def test2(self):
        t = TreeNode.from_list([1, 2, 2, 3, 3, None, None, 4, 4])
        expected = False
        self.assertEqual(expected, self.sol.isBalanced(t))

    def test3(self):
        t = TreeNode.from_list([])
        expected = True
        self.assertEqual(expected, self.sol.isBalanced(t))


if __name__ == '__main__':
    unittest.main()
