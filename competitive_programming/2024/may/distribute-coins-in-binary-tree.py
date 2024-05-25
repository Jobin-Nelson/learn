"""
Created Date: 2024-05-18
Qn: You are given the root of a binary tree with n nodes where each node in the
    tree has node.val coins. There are n coins in total throughout the whole
    tree.

    In one move, we may choose two adjacent nodes and move one coin from one
    node to another. A move may be from parent to child, or from child to
    parent.

    Return the minimum number of moves required to make every node have exactly
    one coin.
Link: https://leetcode.com/problems/distribute-coins-in-binary-tree/
Notes:
    - use dfs
    - use extra coins
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
        def inner(i: int) -> Self|None:
            if i >= len(arr) or arr[i] is None:
                return None
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

def distributeCoins(root: TreeNode|None) -> int:
    # dfs
    res = 0
    def dfs(cur: TreeNode|None) -> int:
        if not cur: return 0
        nonlocal res
        l_extra = dfs(cur.left)
        r_extra = dfs(cur.right)
        extra_coins = cur.val + l_extra + r_extra -1
        res += abs(extra_coins)
        return extra_coins
    dfs(root)
    return res

if __name__ == '__main__':
    r1 = TreeNode.from_list([3,0,0])
    r2 = TreeNode.from_list([0,3,0])

    print(distributeCoins(r1))
    print(distributeCoins(r2))
