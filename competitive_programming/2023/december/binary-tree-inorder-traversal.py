"""
Created Date: 2023-12-09
Qn: Given the root of a binary tree, return the inorder traversal of its nodes' values.
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Notes:
    - use dfs approach
"""
from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        N = len(arr)
        def inner(i: int) -> Self | None:
            if i >= N or arr[i] is None: return None
            node = cls(arr[i])
            node.left = inner(2*i+1)
            node.right = inner(2*i+2)
            return node
        return inner(0)

    def __str__(self) -> str:
        if self is None: return '[]'
        res = []
        q = deque([self])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()


def inorderTraversal(root: TreeNode | None) -> list[int]:
    if root is None: return []
    res = []
    def dfs(node: TreeNode) -> None:
        nonlocal res
        if node.left: dfs(node.left)
        res.append(node.val)
        if node.right: dfs(node.right)
    dfs(root)
    return res

if __name__ == '__main__':
    r1 = TreeNode.from_list([1, None, 2, None, None, 3])
    r2 = TreeNode.from_list([])
    r3 = TreeNode.from_list([1])

    print(inorderTraversal(r1))
    print(inorderTraversal(r2))
    print(inorderTraversal(r3))
