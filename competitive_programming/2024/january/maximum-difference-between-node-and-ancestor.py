"""
Created Date: 2024-01-11
Qn: Given the root of a binary tree, find the maximum value v for which there
    exist different nodes a and b where v = |a.val - b.val| and a is an
    ancestor of b.

    A node a is an ancestor of b if either: any child of a is equal to b or any
    child of a is an ancestor of b.
Link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
Notes:
    - use recursion
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
        if N == 0: return None
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

def maxAncestorDiff(root: TreeNode|None) -> int:
    def dfs(node: TreeNode|None, mn: int, mx: int) -> int:
        if node is None: return 0
        mn = min(mn, node.val)
        mx = max(mx, node.val)
        left = dfs(node.left, mn, mx)
        right = dfs(node.right, mn, mx)
        return max(mx - mn, max(left, right))
    return dfs(root, float('inf'), 0)

if __name__ == '__main__':
    r1 = TreeNode.from_list([8,3,10,1,6,None,14,None,None,4,7,None,None,13])
    r2 = TreeNode.from_list([1,None,2,None,None,None,0,None,None,None,None,None,None,3])

    print(maxAncestorDiff(r1))
    print(maxAncestorDiff(r2))
