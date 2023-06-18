'''
Created Date: 2023-06-14
Qn: Given the root of a Binary Search Tree (BST), return the minimum absolute
difference between the values of any two different nodes in the tree.
Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
Notes:
    - use inorder traversal to calculate min difference
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
            node.left = inner(i * 2 + 1)
            node.right = inner(i * 2 + 2)
            return node
        return inner(0)
    
    def __str__(self) -> str:
        res = []
        q = deque([self])

        while q:
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            res.append(node.val)
        return str(res)
            
def getMinimumDifference(root: TreeNode | None) -> int:
    res = 1e9
    prevNode = None

    def inorder(node: TreeNode | None):
        nonlocal res, prevNode
        if node is None: return
        inorder(node.left)
        if prevNode is not None:
            res = min(res, node.val - prevNode)
        prevNode = node.val
        inorder(node.right)

    inorder(root)
    return res
if __name__ == '__main__':
    r1 = TreeNode.from_list([4,2,6,1,3])
    r2 = TreeNode.from_list([1,0,48,None,None,12,49])

    print(getMinimumDifference(r1))
    print(getMinimumDifference(r2))
