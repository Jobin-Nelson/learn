"""
Created Date: 2024-02-29
Qn: A binary tree is named Even-Odd if it meets the following conditions:

    - The root of the binary tree is at level index 0, its children are at
      level index 1, their children are at level index 2, etc. 
    - For every even-indexed level, all nodes at the level have odd integer
      values in strictly increasing order (from left to right). 
    - For every odd-indexed level, all nodes at the level have even integer
      values in strictly decreasing order (from left to right).

    Given the root of a binary tree, return true if the binary tree is Even-Odd,
    otherwise return false.
Link: https://leetcode.com/problems/even-odd-tree/
Notes:
    - use bfs
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
        N = len(arr)
        def inner(i: int) -> Self|None:
            if i >= N or arr[i] is None: return None
            node = cls(arr[i])
            node.left = inner(i*2+1)
            node.right = inner(i*2+2)
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

    def __repr__(self) -> str:
        return self.__str__()

def isEvenOddTree(root: TreeNode|None) -> bool:
    if root is None: return False
    q = deque([root])
    is_even = True
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        prev = level[0]
        if is_even and prev & 1 == 0: return False
        if not is_even and prev & 1: return False
        for cur in level[1:]:
            if is_even and (cur & 1 == 0 or cur <= prev): return False
            if not is_even and (cur & 1 or cur >= prev): return False
            prev = cur
        is_even = not is_even
    return True

if __name__ == '__main__':
    r1 = TreeNode.from_list([1,10,4,3,None,7,9,12,8,None,None,6,None,None,2])
    r2 = TreeNode.from_list([5,4,2,3,3,7])
    r3 = TreeNode.from_list([5,9,1,3,5,7])
    r4 = TreeNode.from_list([1,10,4,3,None,7,9,12,8,6,None,None,2])

    print(isEvenOddTree(r1))
    print(isEvenOddTree(r2))
    print(isEvenOddTree(r3))
    print(isEvenOddTree(r4))
