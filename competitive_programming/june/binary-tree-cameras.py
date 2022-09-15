'''
Created Date: 17-06-2022
Qn: You are given the root of a binary tree. We install cameras on the tree nodes 
    where each camera at a node can monitor its parent, itself, and its immediate 
    children.
    Return the minimum number of cameras needed to monitor all nodes of the tree.
Link: https://leetcode.com/problems/binary-tree-cameras/
Notes:
    - track two variables at each node till get the whole tree covered/monitored
'''
from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def minCameraCover(root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node):
        nonlocal res
        if not node: return False, True
        c1, m1 = dfs(node.left)
        c2, m2 = dfs(node.right)

        camera = monitor = False
        if c1 or c2: monitor = True
        if not m1 or not m2:
            camera = True
            monitor = True
            res += 1
        return camera, monitor
    c, m = dfs(root)
    return res + 1 if not m else res

if __name__ == '__main__':
    b1 = TreeNode(0)
    c1 = TreeNode(0)
    a1 = TreeNode(0, b1, c1)
    r1 = TreeNode(0, a1)

    d2 = TreeNode(0)
    b2 = TreeNode(0, d2)
    c2 = TreeNode(0, b2)
    a2 = TreeNode(0, b2)
    r2 = TreeNode(0, a2)

    print(minCameraCover(r1))
    print(minCameraCover(r2))
