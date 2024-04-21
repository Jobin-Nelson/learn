"""
Created Date: 2024-04-16
Qn: Given the root of a binary tree and two integers val and depth, add a row
    of nodes with value val at the given depth depth.

    Note that the root node is at depth 1.

    The adding rule is:

        - Given the integer depth, for each not null tree node cur at the depth
          depth - 1, create two tree nodes with value val as cur's left subtree
          root and right subtree root. 
        - cur's original left subtree should be the left subtree of the new
          left subtree root. 
        - cur's original right subtree should be the right subtree of the new
          right subtree root. 
        - If depth == 1 that means there is no depth depth - 1 at all, then
          create a tree node with value val as the new root of the whole
          original tree, and the original tree is the new root's left subtree.

Link: https://leetcode.com/problems/add-one-row-to-tree/
Notes:
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
            node.left = inner(2 * i + 1)
            node.right = inner(2 * i + 2)
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

def addOneRow(root: TreeNode|None, val: int, depth: int) -> TreeNode|None:
    if depth == 1: return TreeNode(val, root, None)
    q = deque([root])
    level = 1
    while q:
        if level == depth-1: break
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
        level += 1
    for node in q:
        cur_left = node.left
        node.left = TreeNode(val, cur_left, None)
        cur_right = node.right
        node.right = TreeNode(val, None, cur_right)
    return root


if __name__ == '__main__':
    r1, v1, d1 = TreeNode.from_list([4,2,6,3,1,5]), 1, 2
    r2, v2, d2 = TreeNode.from_list([4,2,None,3,1]), 1, 3
    r3, v3, d3 = TreeNode.from_list([4,2,6,3,1,5]), 1, 2

    print(addOneRow(r1, v1, d1))
    print(addOneRow(r2, v2, d2))
    print(addOneRow(r3, v3, d3))

