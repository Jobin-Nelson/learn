"""
Created Date: 2025-02-22
Qn: We run a preorder depth-first search (DFS) on the root of a binary tree.

    At each node in this traversal, we output D dashes (where D is the depth of
    this node), then we output the value of this node.  If the depth of a node
    is D, the depth of its immediate child is D + 1.  The depth of the root
    node is 0.

    If a node has only one child, that child is guaranteed to be the left
    child.

    Given the output traversal of this traversal, recover the tree and return
    its root.
Link: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
Notes:
    - use stack
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
                return
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
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
        dashes = 0
        stack = []
        i = 0
        while i < len(traversal):
            if traversal[i] == '-':
                dashes += 1
                i += 1
            else:
                j = i
                while j < len(traversal) and traversal[j] != '-':
                    j += 1
                val = int(traversal[i:j])
                node = TreeNode(val)
                while len(stack) > dashes:
                    stack.pop()
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                stack.append(node)
                i = j
                dashes = 0
        return stack[0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_recoverFromPreorder1(self):
        t = "1-2--3--4-5--6--7"
        expected = TreeNode.from_list([1, 2, 5, 3, 4, 6, 7])
        self.assertEqual(expected, self.sol.recoverFromPreorder(t))

    def test_recoverFromPreorder2(self):
        t = "1-2--3---4-5--6---7"
        expected = TreeNode.from_list(
            [1, 2, 5, 3, None, 6, None, 4, None, None, None, 7]
        )
        self.assertEqual(expected, self.sol.recoverFromPreorder(t))

    def test_recoverFromPreorder3(self):
        t = "1-401--349---90--88"
        expected = TreeNode.from_list([1, 401, None, 349, 88, None, None, 90])
        self.assertEqual(expected, self.sol.recoverFromPreorder(t))


if __name__ == '__main__':
    unittest.main()
