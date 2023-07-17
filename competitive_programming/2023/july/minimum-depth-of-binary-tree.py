'''
Created Date: 2023-07-10
Qn: Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the
    root node down to the nearest leaf node.

    Note: A leaf is a node with no children.
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
Notes:
    - use bfs
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
        cur = deque([self])
        while cur:
            node = cur.popleft()
            res.append(node.val)
            if node.left: cur.append(node.left)
            if node.right: cur.append(node.right)
        return str(res)

def minDepth(root: TreeNode | None) -> int:
    if root is None: return 0
    q = deque([root])
    res = 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left is None and node.right is None:
                return res
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res += 1
    return -1

if __name__ == '__main__':
    r1 = TreeNode.from_list([3,9,20,None,None,15,7])
    r2 = TreeNode.from_list([2,None,3,None,4,None,5,None,6])

    print(minDepth(r1))
    print(minDepth(r2))
