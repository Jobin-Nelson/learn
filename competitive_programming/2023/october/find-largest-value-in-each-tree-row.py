'''
Created Date: 2023-10-24
Qn: Given the root of a binary tree, return an array of the largest value in
    each row of the tree (0-indexed).
Link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
Notes:
'''
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
        if N == 0: return 
        def inner(i: int) ->  Self | None:
            if i >= N or arr[i] is None: return None
            node = cls(arr[i])
            node.left = inner(2*i+1)
            node.right = inner(2*i+2)
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

def largestValues(root: TreeNode | None) -> list[int]:
    if root is None: return []
    q = deque([root])
    res = []
    while q:
        cur_max = float('-inf')
        for _ in range(len(q)):
            node = q.popleft()
            cur_max = max(cur_max, node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(cur_max)
    return res

if __name__ == '__main__':
    r1 = TreeNode.from_list([1,3,2,5,3,None,9])
    r2 = TreeNode.from_list([1,2,3])

    print(largestValues(r1))
    print(largestValues(r2))
