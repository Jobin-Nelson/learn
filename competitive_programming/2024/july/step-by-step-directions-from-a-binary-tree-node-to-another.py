"""
Created Date: 2024-07-16
Qn: You are given the root of a binary tree with n nodes. Each node is uniquely
    assigned a value from 1 to n. You are also given an integer startValue
    representing the value of the start node s, and a different integer
    destValue representing the value of the destination node t.

    Find the shortest path starting from node s and ending at node t. Generate
    step-by-step directions of such path as a string consisting of only the
    uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific
    direction:

        - 'L' means to go from a node to its left child node.
        - 'R' means to go from a node to its right child node.
        - 'U' means to go from a node to its parent node.

    Return the step-by-step directions of the shortest path from node s to node t.
Link: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
Notes:
    - find the lowest common ancestor (LCA)
    - change directions to U for start path
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
        def inner(i: int) -> Self|None:
            if i >= len(arr) or arr[i] is None: return
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

def getDirections(root: TreeNode|None, startValue: int, destValue: int) -> str:
    if root is None: return ''
    def dfs(node: TreeNode|None, path: list[str], target: int) -> list[str]:
        if node is None: return []
        if node.val == target:
            return path
        path.append('L')
        res = dfs(node.left, path, target)
        if res: return res

        path.pop()

        path.append('R')
        res = dfs(node.right, path, target)
        if res: return res

        path.pop()
        return []

    start_path = dfs(root, [], startValue)
    dest_path = dfs(root, [], destValue)

    i = 0
    while i < min(len(start_path), len(dest_path)) and start_path[i] == dest_path[i]:
        i += 1

    res = ''.join(['U'] * len(start_path[i:]) + dest_path[i:])
    return res

if __name__ == '__main__':
    r1, s1, d1 = TreeNode.from_list([5,1,2,3,None,6,4],), 3, 6
    r2, s2, d2 = TreeNode.from_list([2,1],), 2, 1

    print(getDirections(r1, s1, d1))
    print(getDirections(r2, s2, d2))
