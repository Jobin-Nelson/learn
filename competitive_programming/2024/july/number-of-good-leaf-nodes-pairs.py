"""
Created Date: 2024-07-18
Qn: You are given the root of a binary tree and an integer distance. A pair of
    two different leaf nodes of a binary tree is said to be good if the length
    of the shortest path between them is less than or equal to distance.

    Return the number of good leaf node pairs in the tree.
Link: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
Notes:
    - use post order
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

    def __repr__(self) -> str:
        return self.__str__()

def countPairs(root: TreeNode|None, distance: int) -> int:
    res = 0
    def dfs(node: TreeNode|None) -> list[int]:
        if not node:
            return [0] * 12

        if not node.left and not node.right:
            current = [0] * 12
            current[0] = 1
            return current
        nonlocal res
        left_dist = dfs(node.left)
        right_dist = dfs(node.right)
        current = [0] * 12
        for i in range(10):
            current[i+1] += left_dist[i] + right_dist[i]
        current[11] = left_dist[11] + right_dist[11]
        for d1 in range(distance+1):
            for d2 in range(distance+1):
                if 2 + d1 + d2 <= distance:
                    current[11] += left_dist[d1] * right_dist[d2]
        
        return current
    return dfs(root)[11]

if __name__ == '__main__':
    r1, d1 = TreeNode.from_list([1,2,3,None,4]), 3
    r2, d2 = TreeNode.from_list(list(range(1,8))), 3
    r3, d3 = TreeNode.from_list([7,1,4,6,None,5,3,None,None,None,None,None,2]), 3
    
    print(countPairs(r1, d1))
    print(countPairs(r2, d2))
    print(countPairs(r3, d3))
