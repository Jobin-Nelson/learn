'''
Created Date: 2022-12-10
Qn: Given the root of a binary tree, split the binary tree into two subtrees by
    removing one edge such that the product of the sums of the subtrees is
    maximized.

    Return the maximum product of the sums of the two subtrees. Since the answer
    may be too large, return it modulo 10⁹ + 7.

    Note that you need to maximize the answer before taking the mod and not after
    taking it.
Link: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
Notes:
    - use dfs 2 pass
    - first to get the total sum of tree
    - second to find the max product
'''
from collections import deque
from typing import Self

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
        q = deque([self])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

def maxProduct(root: TreeNode | None) -> int:
    memo = {}
    res = 0

    def get_sum(node: TreeNode | None) -> int:
        total = 0
        if not node: return total
        total += node.val
        if node.left:
            total += get_sum(node.left)
        if node.right:
            total += get_sum(node.right)
        memo[node] = total
        return total

    total_sum = get_sum(root)

    def find_max_prod(node: TreeNode | None):
        nonlocal res
        if not node: return 
        if node.left:
            res2 = memo[node.left]
            res = max(res, (total_sum - res2) * res2)
            find_max_prod(node.left)
        if node.right:
            res2 = memo[node.right]
            res = max(res, (total_sum - res2) * res2)
            find_max_prod(node.right)
    find_max_prod(root)
    return res % (10**9 + 7)

if __name__ == '__main__':
    r1 = TreeNode.from_list([1,2,3,4,5,6])
    r2 = TreeNode.from_list([1,None,2,None,None,3,4,None,None,None,None,None,None,5,6])

    print(maxProduct(r1))
    print(maxProduct(r2))

