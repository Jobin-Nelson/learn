'''
Created Date: 2023-02-16
Qn: Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path
    from the root node down to the farthest leaf node.
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
            if index >= N or arr[index] is None: return None

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

def maxDepth(root: TreeNode | None) -> int:

    def dfs(node: TreeNode | None) -> int:
        if not node: return 0
        return 1 + max(dfs(node.left), dfs(node.right))
    return dfs(root)

if __name__ == '__main__':
    r1 = [3,9,20,None,None,15,7]
    r2 = [1,None,2]

    print(maxDepth(TreeNode.from_list(r1)))
    print(maxDepth(TreeNode.from_list(r2)))

