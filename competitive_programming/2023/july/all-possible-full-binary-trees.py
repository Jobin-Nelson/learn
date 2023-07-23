'''
Created Date: 2023-07-23
Qn: Given an integer n, return a list of all possible full binary trees with n
    nodes. Each node of each tree in the answer must have Node.val == 0.

    Each element of the answer is the root node of one possible tree. You may
    return the final list of trees in any order.

    A full binary tree is a binary tree where each node has exactly 0 or 2
    children.
Link: https://leetcode.com/problems/all-possible-full-binary-trees/
Notes:
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
        q = deque([self])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def allPossibleFBT(n: int) -> list[TreeNode | None]:
    # dp approach
    if n & 1 == 0: return []

    dp = [[] for _ in range(n+1)]
    dp[1].append(TreeNode())

    for count in range(3, n + 1, 2):
        for i in range(1, count - 1, 2):
            j = count - 1 - i
            for left in dp[i]:
                for right in dp[j]:
                    root = TreeNode(0, left, right)
                    dp[count].append(root)
    return dp[n]

if __name__ == '__main__':
    n1 = 7
    n2 = 3

    print(allPossibleFBT(n1))
    print(allPossibleFBT(n2))
