'''
Created Date: 2023-03-15
Qn: Given the root of a binary tree, determine if it is a complete binary tree.

    In a complete binary tree, every level, except possibly the last, is
    completely filled, and all nodes in the last level are as far left as
    possible. It can have between 1 and 2h nodes inclusive at the last level h.
Link: https://leetcode.com/problems/check-completeness-of-a-binary-tree/
Notes:
    - use bfs level traversing capture none as well to till the last level
    - pop till you run out of None
    - return False if the q is not empty and True otherwise
'''
from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr:list[int | None]) -> Self | None:
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

def isCompleteTree(root: TreeNode | None) -> bool:
    if not root: return True

    q = deque([root])
    while q[0] is not None:
        node = q.popleft()
        q.append(node.left)
        q.append(node.right)

    while q and q[0] is None:
        q.popleft()

    return not bool(q)

if __name__ == '__main__':
    r1 = TreeNode.from_list([1,2,3,4,5,6])
    r2 = TreeNode.from_list([1,2,3,4,5,None,7])

    print(isCompleteTree(r1))
    print(isCompleteTree(r2))
