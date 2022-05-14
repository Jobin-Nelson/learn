'''
Qn: Given the root of a binary tree, return the maximum path sum of any non-empty path.
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Notes:
- keep track of nonlocal res variable with maximum sequence path sum
- return maximum path sum
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root: TreeNode) -> int:
    res = root.val
    
    def dfs(root):
        nonlocal res
        if not root: return 0
        left_max = max(dfs(root.left), 0)
        right_max = max(dfs(root.right), 0)
        res = max(res, root.val + left_max + right_max)
        return root.val + max(left_max, right_max)

    dfs(root)
    return res

if __name__ == '__main__':
    a1 = TreeNode(2)
    b1 = TreeNode(3)
    r1 = TreeNode(1, a1, b1)

    a2 = TreeNode(9)
    b2 = TreeNode(15)
    c2 = TreeNode(7)
    d2 = TreeNode(20, b2, c2)
    r2 = TreeNode(-10, a2, d2)

    print(max_path_sum(r1))
    print(max_path_sum(r2))