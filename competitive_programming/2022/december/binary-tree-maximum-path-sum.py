'''
Created Date: 2022-12-11
Qn: A path in a binary tree is a sequence of nodes where each pair of adjacent
    nodes in the sequence has an edge connecting them. A node can only appear
    in the sequence at most once. Note that the path does not need to pass
    through the root.

    The path sum of a path is the sum of the node's values in the path.

    Given the root of a binary tree, return the maximum path sum of any
    non-empty path.
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Notes:
    - use dfs to traverse and maintain a res
    - return max_single_path
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
            if index >= N or arr[index] is None:
                return None
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

def maxPathSum(root: TreeNode | None) -> int:
    res = float('-inf')

    def dfs(node: TreeNode | None) -> int:
        if not node: return 0
        nonlocal res
        l, r = dfs(node.left), dfs(node.right)
        max_single_path = max(node.val + max(l, r), node.val)
        res = max(res, max_single_path, node.val + l + r)
        return max_single_path
    dfs(root)
    return int(res)

if __name__ == '__main__':
    r1 = TreeNode.from_list([1, 2, 3])
    r2 = TreeNode.from_list([-10,9,20,None,None,15,7])

    print(maxPathSum(r1))
    print(maxPathSum(r2))
