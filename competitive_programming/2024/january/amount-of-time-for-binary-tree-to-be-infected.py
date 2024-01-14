"""
Created Date: 2024-01-10
Qn: You are given the root of a binary tree with unique values, and an integer
    start. At minute 0, an infection starts from the node with value start.

    Each minute, a node becomes infected if:

        - The node is currently uninfected.
        - The node is adjacent to an infected
        node.

    Return the number of minutes needed for the entire tree to be infected.
Link: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
Notes:
    - use recursion to get distance to farthest node away from the start node
"""
from typing import Self
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int|None]) -> Self | None:
        N = len(arr)
        def inner(i: int) -> Self | None:
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

def amountOfTime(root: TreeNode|None, start: int) -> int:
    max_distance = 0
    def traverse(node: TreeNode|None, start: int) -> int:
        nonlocal max_distance
        depth = 0
        if node is None: return depth
        ld = traverse(node.left, start)
        rd = traverse(node.right, start)
        
        if node.val == start:
            max_distance = max(ld, rd)
            depth = -1
        elif ld >= 0 and rd >= 0:
            depth = max(ld, rd) + 1
        else:
            max_distance = max(max_distance, abs(ld) + abs(rd))
            depth = min(ld, rd) - 1
        return depth
    traverse(root, start)
    return max_distance
        
if __name__ == '__main__':
    r1, s1 = TreeNode.from_list([1,5,3,None,4,10,6,None,None,9,2]), 3
    r2, s2 = TreeNode.from_list([1]), 1
    r3, s3 = TreeNode.from_list([1,2,None,3,None,None,None,4,None,None,None,None,None,5]), 3

    print(amountOfTime(r1, s1))
    print(amountOfTime(r2, s2))
    print(amountOfTime(r3, s3))
