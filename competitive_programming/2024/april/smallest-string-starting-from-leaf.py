"""
Created Date: 2024-04-17
Qn: You are given the root of a binary tree where each node has a value in the
    range [0, 25] representing the letters 'a' to 'z'.

    Return the lexicographically smallest string that starts at a leaf of this
    tree and ends at the root.

    As a reminder, any shorter prefix of a string is lexicographically smaller.

        - For example, "ab" is lexicographically smaller than "aba".

    A leaf of a node is a node that has no children.
Link: https://leetcode.com/problems/smallest-string-starting-from-leaf/
Notes:
    - greedy approach won't work since the string is constructed from bottom to
      top
    - use dfs and compare strings
"""
from typing import Self
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int|None]) -> Self|None:
        N = len(arr)
        def inner(i: int) -> Self|None:
            if i >= N or arr[i] is None: return None
            node = cls(arr[i])
            node.left = inner(i*2+1)
            node.right = inner(i*2+2)
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

def smallestFromLeaf(root: TreeNode|None) -> str:
    if root is None: return ''
    def dfs(node: TreeNode, cur: str) -> str:
        cur = chr(node.val + ord('a')) + cur
        if node.left and node.right:
            return min(dfs(node.left, cur), dfs(node.right, cur))
        if node.left: return dfs(node.left, cur)
        if node.right: return dfs(node.right, cur)
        return cur
    return dfs(root, '')


if __name__ == '__main__':
    r1 = TreeNode.from_list([0,1,2,3,4,3,4])
    r2 = TreeNode.from_list([25,1,3,1,3,0,2])
    r3 = TreeNode.from_list([2,2,1,None,1,0,None,0])
    r4 = TreeNode.from_list([0,None,1])
    r5 = TreeNode.from_list([2,2,1,None,1,0,None,0])
    r6 = TreeNode.from_list([4,0,1,1])

    print(smallestFromLeaf(r1))
    print(smallestFromLeaf(r2))
    print(smallestFromLeaf(r3))
    print(smallestFromLeaf(r4))
    print(smallestFromLeaf(r5))
    print(smallestFromLeaf(r6))
