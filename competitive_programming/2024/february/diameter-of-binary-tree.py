"""
Created Date: 2024-02-27
Qn: Given the root of a binary tree, return the length of the diameter of the
    tree.

    The diameter of a binary tree is the length of the longest path between any
    two nodes in a tree. This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of
    edges between them.
Link: https://leetcode.com/problems/diameter-of-binary-tree/
Notes:
    - use dfs
"""
from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int]) -> Self|None:
        N = len(arr)
        def inner(n: int) -> Self|None:
            if n >= N: return None
            node = cls(arr[n])
            node.left = inner(n*2+1)
            node.right = inner(n*2+2)
            return node
        return inner(0)

    def __str__(self) -> str:
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

def diameterOfBinaryTree(root: TreeNode|None) -> int:
    if root is None: return 0
    res = 0
    def longest(node: TreeNode|None) -> int:
        if node is None: return -1
        nonlocal res
        left = longest(node.left)
        right = longest(node.right)
        res = max(res, 2 + left + right)
        return 1 + max(left, right)
    longest(root)
    return res

if __name__ == '__main__':
    r1 = TreeNode.from_list(list(range(1, 6)))
    r2 = TreeNode.from_list([1,2])

    print(diameterOfBinaryTree(r1))
    print(diameterOfBinaryTree(r2))
