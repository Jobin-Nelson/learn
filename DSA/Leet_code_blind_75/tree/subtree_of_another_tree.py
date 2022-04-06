'''
Qn: Given the roots of two binary trees root and subroot
return true if there is a subtree of root with the same structure and node values of subroot and false otherwise
Link: https://leetcode.com/problems/subtree-of-another-tree/
Notes:
- have to check same tree at each node
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_subtree(root: TreeNode, subroot: TreeNode) -> bool:
    if not subroot: return True
    if not root: return False
    if same_tree(root, subroot):
        return True
    return is_subtree(root.left, subroot) or is_subtree(root.right, subroot)

def same_tree(t, s) -> bool:
    if not t and not s: return True
    if s and t and s.val == t.val:
        return same_tree(t.left, s.left) and same_tree(t.right, s.right)
    return False


if __name__ == '__main__':
    a1 = TreeNode(1)
    b1 = TreeNode(2)
    c1 = TreeNode(5)
    d1 = TreeNode(4, a1, b1)
    r1 = TreeNode(3, d1, c1)

    a2 = TreeNode(1)
    b2 = TreeNode(2)
    r2 = TreeNode(4, a2, b2)

    a3 = TreeNode(1)
    b3 = TreeNode(0)
    c3 = TreeNode(5)
    d3 = TreeNode(2, b3)
    e3 = TreeNode(4, a3, d3)
    r3 = TreeNode(e3, c3)

    a4 = TreeNode(1)
    b4 = TreeNode(2)
    r4 = TreeNode(4, a4, b4)

    print(is_subtree(r1, r2))
    print(is_subtree(r3, r4))
