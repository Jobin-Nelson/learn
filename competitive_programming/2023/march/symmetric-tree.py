'''
Created Date: 2023-03-13
Qn: Given the root of a binary tree, check whether it is a mirror of itself
    (i.e., symmetric around its center).
Link: https://leetcode.com/problems/symmetric-tree/
Notes:
    - use dfs
    - check left == right if either of them is None
    - return left.val == right.val and left branch isMirror and right branch isMirror
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
        q = deque[self]

        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

def isSymmetric(root: TreeNode | None) -> bool:
    def isMirror(left: TreeNode | None, right: TreeNode | None) -> bool:
        if left is None or right is None:
            return left == right
        return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    return isMirror(root.left, root.right)

if __name__ == '__main__':
    r1 = TreeNode.from_list([1,2,2,3,4,4,3])
    r2 = TreeNode.from_list([1,2,2,None,3,None,3])

    print(isSymmetric(r1))
    print(isSymmetric(r2))
