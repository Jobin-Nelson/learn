'''
Qn: Given the root of a binary search tree, determine if it is a valid binary search tree
Link: https://leetcode.com/problems/validate-binary-search-tree/
Notes: 
- just check if node.val is greater than left and smaller than right
- left and right starts of as negative infinity and positive infinity
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    def valid(left, node, right):
        if not node: return True
        if not(left < node.val and node.val < right):
            return False
        return valid(left, node.left, node.val) and valid(node.val, node.right, right)
    return valid(float('-inf'),root, float('inf'))

if __name__ == '__main__':
    a1 = TreeNode(1)
    b1 = TreeNode(3)
    r1 = TreeNode(2, a1, b1)

    a2 = TreeNode(1)
    b2 = TreeNode(3)
    c2 = TreeNode(6)
    d2 = TreeNode(4, b2, c2)
    r2 = TreeNode(5, a2, d2)

    print(is_valid_bst(r1))
    print(is_valid_bst(r2))
     