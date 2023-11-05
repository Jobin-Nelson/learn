'''
Created Date: 2023-11-02
Qn: Given the root of a binary tree, return the number of nodes where the
    value of the node is equal to the average of the values in its subtree.

    Note:

        - The average of n elements is the sum of the n elements divided by n
          and rounded down to the nearest integer. 
        - A subtree of root is a tree consisting of root and all of its
          descendants.

Link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
Notes:
    - use dfs and return sum and number of nodes
'''
from typing import Self
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: list[int|None]) -> Self | None:
        if not arr: return None
        N = len(arr)
        def inner(i: int) -> Self | None:
            if i >= N or arr[i] is None: return None
            node = cls(arr[i])
            node.left = inner(2*i+1)
            node.right = inner(2*i+2)
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
            
def averageOfSubtree(root: TreeNode | None) -> int:
    if root is None: return 0
    res = 0
    def dfs(node: TreeNode) -> tuple[int, int]:
        nonlocal res
        s, n = node.val, 1
        if node.left:
            sl, nl = dfs(node.left)
            s += sl
            n += nl
        if node.right:
            sr, nr = dfs(node.right)
            s += sr
            n += nr
        if s // n == node.val: res += 1
        return (s, n)
    dfs(root)
    return res

if __name__ == '__main__':
    r1 = TreeNode.from_list([4,8,5,0,1,None,6])
    r2 = TreeNode.from_list([1])

    print(averageOfSubtree(r1))
    print(averageOfSubtree(r2))
