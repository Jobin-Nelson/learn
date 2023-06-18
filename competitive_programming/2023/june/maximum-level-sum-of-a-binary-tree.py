'''
Created Date: 2023-06-15
Qn: Given the root of a binary tree, the level of its root is 1, the level of
    its children is 2, and so on.

    Return the smallest level x such that the sum of all the values of nodes at
    level x is maximal.
Link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
Notes:
    - use bfs, calculate levelsum update result
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
        def inner(i: int) -> Self | None:
            if i >= N or arr[i] is None: return None
            node = cls(arr[i])
            node.left = inner(2 * i + 1)
            node.right = inner(2 * i + 2)
            return node
        return inner(0)

    def __str__(self) -> str:
        res = []
        q = deque([self])
        while q:
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            res.append(node.val)
        return str(res)
            
def maxLevelSum(root: TreeNode) -> int:
    res = level = 0
    maxSum = -1e9
    q = deque([root])
    while q:
        level += 1
        levelSum = 0
        for _ in range(len(q)):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            levelSum += node.val
        if levelSum > maxSum:
            maxSum = levelSum
            res = level
    return res

if __name__ == '__main__':
    r1 = TreeNode.from_list([1,7,0,7,-8,None,None])
    r2 = TreeNode.from_list([989,None,10250,98693,-89388,None,None,None,-32127])

    print(maxLevelSum(r1))
    print(maxLevelSum(r2))
