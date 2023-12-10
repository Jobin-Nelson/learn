"""
Created Date: 2023-12-08
Qn: Given the root of a binary tree, construct a string consisting of
    parenthesis and integers from a binary tree with the preorder traversal
    way, and return it.

    Omit all the empty parenthesis pairs that do not affect the one-to-one
    mapping relationship between the string and the original binary tree.
Link: https://leetcode.com/problems/construct-string-from-binary-tree/
Notes:
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


def tree2str(root: TreeNode | None) -> str:
    if root is None: return ''
    left = f'({tree2str(root.left)})' if root.left else ''
    right = f'({tree2str(root.right)})' if root.right else ''
    if right and not left: left = '()'
    return f'{root.val}{left}{right}'

if __name__ == '__main__':
    r1 = TreeNode.from_list([1,2,3,4])
    r2 = TreeNode.from_list([1,2,3,None,4])

    print(tree2str(r1))
    print(tree2str(r2))
