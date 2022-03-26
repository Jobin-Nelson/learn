'''
Qn:Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Link: https://leetcode.com/problems/same-tree/
Notes: 
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if p == None and q == None: return True
    if p == None or q == None or p.val != q.val: return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

if __name__ == '__main__':
    a1 = TreeNode(2)
    b1 = TreeNode(3)
    p1 = TreeNode(1, a1, b1)

    c1 = TreeNode(2)
    d1 = TreeNode(3)
    q1 = TreeNode(1, c1, d1)

    a2 = TreeNode(2)
    b2 = TreeNode(1)
    p2 = TreeNode(1, a2, b2)

    c2 = TreeNode(1)
    d2 = TreeNode(2)
    q2 = TreeNode(1, c2, d2)
    print(is_same_tree(p1, q1))
    print(is_same_tree(p2, q2))
