'''
Qn: Implement the BSTIterator class that represents an iterator over the in-order traversal of a 
binary search tree (BST)
Link: https://leetcode.com/problems/binary-search-tree-iterator/
Notes:
- store only left nodes in the stack and append new nodes when calling next() for O(h) space
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## runs in O(1) time and O(n) space
# class BSTIterator:
#     def __init__(self, root: Optional[TreeNode]):
#         self.stack = []
#         def dfs(node):
#             if not node: return
#             dfs(node.right)
#             self.stack.append(node.val)
#             dfs(node.left)
#         dfs(root)
# 
#     def next(self) -> int:
#         return self.stack.pop() if self.stack else None
# 
#     def hasNext(self) -> bool:
#         return self.stack != []

# runs in O(1) time and O(h) space
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return self.stack != []

if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15, b, c)
    r = TreeNode(7, a, d)

    obj = BSTIterator(r)
    print(obj.next())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
