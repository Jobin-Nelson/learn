"""
Created Date: 2024-01-09
Qn: Consider all the leaves of a binary tree, from left to right order, the
    values of those leaves form a leaf value sequence.

    For example, in the given tree above, the leaf value sequence is (6, 7, 4,
    9, 8).

    Two binary trees are considered leaf-similar if their leaf value sequence
    is the same.

    Return true if and only if the two given trees with head nodes root1 and
    root2 are leaf-similar.
Link: https://leetcode.com/problems/leaf-similar-trees/
Notes:
    - use recursion to get leaves of a tree
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
        if N == 0: return None
        def inner(i: int) -> Self | None:
            if i >= N or arr[i] is None: return None
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
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def leafSimilar(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def getLeaf(node: TreeNode | None, res: list[int]):
        if node is None: return
        if node.left is None and node.right is None:
            res.append(node.val)
            return
        if node.left: getLeaf(node.left, res)
        if node.right: getLeaf(node.right, res)
    r1, r2 = [], []
    getLeaf(root1, r1)
    getLeaf(root2, r2)
    return r1 == r2

if __name__ == '__main__':
    r11, r12 = TreeNode.from_list([3,5,1,6,2,9,8,None,None,7,4]), TreeNode.from_list([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
    r21, r22 = TreeNode.from_list([1, 2, 3]), TreeNode.from_list([1, 3, 2])

    print(leafSimilar(r11, r12))
    print(leafSimilar(r21, r22))
