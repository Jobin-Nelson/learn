"""
Created Date: 2024-02-26
Qn: Given the roots of two binary trees p and q, write a function to check if
    they are the same or not.

    Two binary trees are considered the same if they are structurally
    identical, and the nodes have the same value.
Link: https://leetcode.com/problems/same-tree/
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
    def from_list(cls, arr: list[int|None]) -> Self|None:
        N = len(arr)
        def inner(i: int) -> Self|None:
            if i >= N or arr[i] is None: return None
            node = cls(arr[i])
            node.left = inner(i*2 + 1)
            node.right = inner(i*2 + 2)
            return node
        return inner(0)
    
    def __str__(self) -> str:
        q = deque([self])
        res = []
        while q:
            node = q.pop()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def isSameTree(p: TreeNode|None, q: TreeNode|None) -> bool:
    if p is None and q is None: return True
    if p is None or q is None: return False
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

if __name__ == '__main__':
    p1, q1 = TreeNode.from_list([1,2,3]), TreeNode.from_list([1,2,3])
    p2, q2 = TreeNode.from_list([1,2]), TreeNode.from_list([1,None,2])
    p3, q3 = TreeNode.from_list([1,2,1]), TreeNode.from_list([1,1,2])

    print(isSameTree(p1, q1))
    print(isSameTree(p2, q2))
    print(isSameTree(p3, q3))

