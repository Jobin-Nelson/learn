'''
Created Date: 2023-04-19
Qn: You are given the root of a binary tree.

    A ZigZag path for a binary tree is defined as follow:

        - Choose any node in the binary tree and a direction (right or left). 
        - If the current direction is right, move to the right child of the
          current node; otherwise, move to the left child. 
        - Change the direction from right to left or from left to right. 
        - Repeat the second and third steps until you can't move in the tree.

    Zigzag length is defined as the number of nodes visited - 1.
    (A single node has a length of 0).

    Return the longest ZigZag path contained in that tree.
Link: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
Notes:
    - use dfs
    - don't alternate, calculate both left and right
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
        def dfs(index: int | None) -> Self | None:
            if index is None or index >= N: return None
            node = cls(arr[index])
            node.left = dfs(2 * index + 1)
            node.right = dfs(2 * index + 2)
            return node

        return dfs(0)

    def __str__(self) -> str:
        res = []

        q = deque([self])

        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

def longestZipZag(root: TreeNode | None) -> int:
    if root is None: return 0
    def dfs(node: TreeNode | None, is_right: bool, total: int) -> int:
        if not node: return total

        l = dfs(node.left, False, total + 1 if is_right else 1)
        r = dfs(node.right, True, total + 1 if not is_right else 1)
        return max(l, r)
    
    return dfs(root, False, 0) - 1

if __name__ == '__main__':
    r1 = TreeNode.from_list([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1,None,1])
    r2 = TreeNode.from_list([1,1,1,None,1,None,None,1,1,None,1])
    r3 = TreeNode.from_list([1])

    print(longestZipZag(r1))
    print(longestZipZag(r2))
    print(longestZipZag(r3))
