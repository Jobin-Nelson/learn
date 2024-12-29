"""
Created Date: 2024-12-25
Qn: Given the root of a binary tree, return an array of the largest value in
    each row of the tree (0-indexed).
Link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
Notes:
    - use level order traversal
"""

from typing import Self
import unittest
from collections import deque
from sys import maxsize


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

    def __str__(self) -> str:
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


class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        q = deque([root])

        res = []
        while q:
            cur_max = -maxsize
            for _ in range(len(q)):
                node = q.popleft()
                cur_max = max(cur_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(cur_max)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_largestValues1(self):
        r = TreeNode.from_list([1, 3, 2, 5, 3, None, 9])
        expected = [1, 3, 9]
        self.assertEqual(expected, self.sol.largestValues(r))


if __name__ == '__main__':
    unittest.main()
