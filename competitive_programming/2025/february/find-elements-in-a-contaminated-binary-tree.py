"""
Created Date: 2025-02-21
Qn: Given a binary tree with the following rules:

    1. root.val == 0
    2. For any treeNode:
       1. If treeNode.val has a value x and treeNode.left != null, then
          treeNode.left.val == 2 * x + 1
       2. If treeNode.val has a value x and treeNode.right != null, then
          treeNode.right.val == 2 * x + 2 Now the binary tree is contaminated,
          which means all treeNode.val have been changed to -1.

    Implement the FindElements class:

    - FindElements(TreeNode* root) Initializes the object with a contaminated
      binary tree and recovers it.
    - bool find(int target) Returns true if the target value exists in the
      recovered binary tree.
Link: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
Notes:
    - use bfs
"""

import unittest
from typing import Self
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
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

    def __repr__(self) -> str:
        return self.__str__()


class FindElements:
    def __init__(self, root: TreeNode | None) -> None:
        if not root:
            return
        self.elements = {0}
        root.val = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                self.elements.add(node.val)
                if node.left:
                    node.left.val = 2 * node.val + 1
                    q.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    q.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.elements


class TestSolution(unittest.TestCase):
    def test_FindElements1(self):
        node = TreeNode.from_list([-1, None, -1])
        fe = FindElements(node)
        targets = [1, 2]
        expects = [False, True]
        for t, e in zip(targets, expects):
            self.assertEqual(e, fe.find(t))

    def test_FindElements2(self):
        node = TreeNode.from_list([-1, -1, -1, -1, -1])
        fe = FindElements(node)
        targets = [1, 3, 5]
        expects = [True, True, False]
        for t, e in zip(targets, expects):
            self.assertEqual(e, fe.find(t))

    def test_FindElements3(self):
        node = TreeNode.from_list([-1, None, -1, -1, None, -1])
        fe = FindElements(node)
        targets = [2, 3, 4, 5]
        expects = [True, False, False, True]
        for t, e in zip(targets, expects):
            self.assertEqual(e, fe.find(t))


if __name__ == '__main__':
    unittest.main()
