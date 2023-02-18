'''
Created Date: 2023-02-18
Qn: Given the root of a binary tree, invert the tree, and return its root.
Link: https://leetcode.com/problems/invert-binary-tree/
Notes:
    - use dfs
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

def invertTree(root: TreeNode | None) -> TreeNode | None:
    if root is None: return
    root.right, root.left = invertTree(root.left), invertTree(root.right)
    return root

if __name__ == '__main__':
    r1 = [4,2,7,1,3,6,9]
    r2 = [2,1,3]
    r3 = []

    print(invertTree(TreeNode.from_list(r1)))
    print(invertTree(TreeNode.from_list(r2)))
    print(invertTree(TreeNode.from_list(r3)))
