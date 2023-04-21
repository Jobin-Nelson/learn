'''
Created Date: 2023-04-20
Qn: Given the root of a binary tree, return the maximum width of the given
    tree.

    The maximum width of a tree is the maximum width among all levels.

    The width of one level is defined as the length between the end-nodes
    (the leftmost and rightmost non-null nodes), where the null nodes between
    the end-nodes that would be present in a complete binary tree extending
    down to that level are also counted into the length calculation.

    It is guaranteed that the answer will in the range of a 32-bit signed
    integer.
Link: https://leetcode.com/problems/maximum-width-of-binary-tree/
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
        def inner(index: int | None) -> Self | None:
            if index is None or index >= N: return None
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

def widthOfBinaryTree(root: TreeNode | None) -> int:
    if not root: return 0

    q: deque[tuple[TreeNode, int]] = deque([(root, 0)])
    res = 0

    while q:
        level_start = q[0][1]
        level_end = q[-1][1]

        for _ in range(len(q)):
            node, index = q.popleft()
            if node.left: q.append((node.left, 2 * index + 1))
            if node.right: q.append((node.right, 2 * index + 2))
        res = max(res, level_end - level_start + 1)
    return res

if __name__ == '__main__':
    r1 = TreeNode.from_list([1,3,2,5,3,None,9])
    r2 = TreeNode.from_list([1,3,2,5,None,None,9,6,None,None,None,None,None,7])
    r3 = TreeNode.from_list([1,3,2,5])

    print(widthOfBinaryTree(r1))
    print(widthOfBinaryTree(r2))
    print(widthOfBinaryTree(r3))
