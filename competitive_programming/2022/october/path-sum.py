'''
Created Date: 2022-10-04
Qn: Given the root of a binary tree and an integer targetSum, return true if
    the tree has a root-to-leaf path such that adding up all the values along
    the path equals targetSum.

    A leaf is a node with no children.
Link: https://leetcode.com/problems/path-sum/
Notes:
    - recursion
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode | None, targetSum: int) -> bool:
    if not root: return False
    targetSum = targetSum - root.val
    if not root.left and not root.right: return targetSum == 0
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)

if __name__ == '__main__':
    a1 = TreeNode(7)
    b1 = TreeNode(2)
    c1 = TreeNode(1)
    d1 = TreeNode(11, a1, b1)
    e1 = TreeNode(13)
    f1 = TreeNode(4, None, c1)
    g1 = TreeNode(4, d1)
    h1 = TreeNode(8, e1, f1)
    r1 = TreeNode(5, g1, h1)
    t1 = 22

    a2 = TreeNode(2)
    b2 = TreeNode(3)
    r2 = TreeNode(1, a2, b2)
    t2 = 5

    r3 = None
    t3 = 0

    print(hasPathSum(r1, t1))
    print(hasPathSum(r2, t2))
    print(hasPathSum(r3, t3))
