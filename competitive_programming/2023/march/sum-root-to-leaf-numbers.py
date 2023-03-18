'''
Created Date: 2023-03-14
Qn: You are given the root of a binary tree containing digits from 0 to 9 only.

    Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
    Return the total sum of all root-to-leaf numbers. Test cases are generated
    so that the answer will fit in a 32-bit integer.

    A leaf node is a node with no children.
Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
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
    def from_list(cls, arr: list[int]) -> Self | None:
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

def sumNumbers(root: TreeNode | None) -> int:
    def dfs(node: TreeNode | None, cur_sum: int) -> int:
        if not node: return 0
        cur_sum = cur_sum * 10 + node.val
        if not node.left and not node.right: return cur_sum
        return dfs(node.left, cur_sum) + dfs(node.right, cur_sum)
    return dfs(root, 0)

if __name__ == '__main__':
    r1 = TreeNode.from_list([1,2,3])
    r2 = TreeNode.from_list([4,9,0,5,1])

    print(sumNumbers(r1))
    print(sumNumbers(r2))

