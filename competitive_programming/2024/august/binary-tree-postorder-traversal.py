"""
Created Date: 2024-08-25
Qn: Given the root of a binary tree, return the postorder traversal of its
nodes' values.
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Notes:
    - use dfs
"""

from collections import deque
from typing import Self


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
            node.left = inner(2 * i + 1)
            node.right = inner(2 * i + 2)
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

    def __str__(self) -> str:
        return self.__repr__()


def postOrderTraversal(root: TreeNode | None) -> list[int]:
    if not root: return []
    res = []
    def dfs(node: TreeNode):
        if node.left: dfs(node.left)
        if node.right: dfs(node.right)
        res.append(node.val)
    dfs(root)
    return res


if __name__ == '__main__':
    r1 = TreeNode.from_list([1, None, 2, None, None, 3])
    r2 = TreeNode.from_list([])
    r3 = TreeNode.from_list([1])

    print(postOrderTraversal(r1))
    print(postOrderTraversal(r2))
    print(postOrderTraversal(r3))
