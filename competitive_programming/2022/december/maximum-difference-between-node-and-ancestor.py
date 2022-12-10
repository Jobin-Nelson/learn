'''
Created Date: 2022-12-09
Qn: Given the root of a binary tree, find the maximum value v for which there
    exist different nodes a and b where v = |a.val - b.val| and a is an
    ancestor of b.

    A node a is an ancestor of b if either: any child of a is equal to b or any
    child of a is an ancestor of b.
Link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
Notes:
    - use dfs, keep track of cur_max and cur_min
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
        if N == 0: return None
        def inner(index: int) -> Self | None:
            if index >= N or arr[index] is None: return None

            node = cls(arr[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
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

def maxAncestorDiff(root: TreeNode | None) -> int:
    if not root: return 0

    def helper(node: TreeNode | None, cur_max: int, cur_min: int) -> int:
        if not node: return cur_max - cur_min
        cur_max = max(cur_max, node.val)
        cur_min = min(cur_min, node.val)
        left = helper(node.left, cur_max, cur_min)
        right = helper(node.right, cur_max, cur_min)
        return max(left, right)
    return helper(root, root.val, root.val)

if __name__ == '__main__':
    r1 = TreeNode.from_list([8,3,10,1,6,None,14,None,None,4,7,13])
    r2 = TreeNode.from_list([1,None,2,None,0,3])

    print(maxAncestorDiff(r1))
    print(maxAncestorDiff(r2))
