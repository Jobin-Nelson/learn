"""
Created Date: 2024-02-28
Qn: Given the root of a binary tree, return the leftmost value in the last row
    of the tree.
Link: https://leetcode.com/problems/find-bottom-left-tree-value/
Notes:
    - use bfs
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
        q = deque([self])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def findBottomLeftValue(root: TreeNode|None) -> int:
    if root is None: return -1
    q = deque([root])
    prev_left = -1
    cur_left = -1
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if i == 0: cur_left = node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        prev_left = cur_left
    return prev_left

if __name__ == '__main__':
    r1 = TreeNode.from_list([2,1,3])
    r2 = TreeNode.from_list([1,2,3,4,None,5,6,None,None,None,None,7])

    print(findBottomLeftValue(r1))
    print(findBottomLeftValue(r2))
