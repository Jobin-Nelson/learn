"""
Created Date: 2024-01-08
Qn: Given the root node of a binary search tree and two integers low and high,
    return the sum of values of all nodes with a value in the inclusive range
    [low, high].
Link: https://leetcode.com/problems/range-sum-of-bst/
Notes:
    - use recursion or iterative approach
"""
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
        if N == 0: return None
        def inner(i: int) -> Self | None:
            if i >= N or arr[i] is None: return None
            node = cls(arr[i])
            node.left = inner(i * 2 + 1)
            node.right = inner(i * 2 + 2)
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


def rangeSumBST(root: TreeNode | None, low: int, high: int) -> int:
    if root is None: return 0
    res = 0
    q = deque([root])
    while q:
        node = q.popleft()
        if low <= node.val <= high:
            res += node.val
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return res

if __name__ == '__main__':
    r1, l1, h1 = TreeNode.from_list([10,5,15,3,7,None,18]), 7, 15
    r2, l2, h2 = TreeNode.from_list([10,5,15,3,7,13,18,1,None,6]), 6, 10

    print(rangeSumBST(r1, l1, h1))
    print(rangeSumBST(r2, l2, h2))
