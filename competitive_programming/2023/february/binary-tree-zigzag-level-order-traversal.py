'''
Created Date: 2023-02-19
Qn: Given the root of a binary tree, return the zigzag level order traversal of
    its nodes' values. (i.e., from left to right, then right to left for the 
    next level and alternate between).
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Notes:
    - use bfs
    - change the way you append to level and not the queue
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
        def inner(index: int) -> Self | None:
            if index >= N or arr[index] is None: return
            node = cls(arr[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node
        return inner(0)

    def __str__(self):
        res = []
        q = deque([self])

        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

def zigzagLevelOrder(root: TreeNode | None) -> list[list[int]]:
    if root is None: return []
    res = []
    q = deque([root])
    zigzag = 0

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            if zigzag:
                level.append(node.val)
            else:
                level = [node.val] + level
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        zigzag ^= 1
        res.append(level)
    return res

if __name__ == '__main__':
    r1 = [3,9,20,None,None,15,7]
    r2 = [1]
    r3 = []
    r4 = [1,2,3,4,None,None,5]

    print(zigzagLevelOrder(TreeNode.from_list(r1)))
    print(zigzagLevelOrder(TreeNode.from_list(r2)))
    print(zigzagLevelOrder(TreeNode.from_list(r3)))
    print(zigzagLevelOrder(TreeNode.from_list(r4)))
