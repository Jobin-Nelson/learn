'''
Qn: Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Notes
- inorder traversal with the kth element
- iterating through left node till it and finding the kth element by decrementing k and going over right node 
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root: TreeNode, k: int) -> int:
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k: return root.val
        root = root.right

if __name__ == '__main__':
    a1 = TreeNode(2)
    b1 = TreeNode(1, None, a1)
    c1 = TreeNode(4)
    r1 = TreeNode(3, b1, c1)

    a2 = TreeNode(1)
    b2 = TreeNode(4)
    c2 = TreeNode(6)
    d2 = TreeNode(2, a2)
    e2 = TreeNode(3, d2, b2)
    r2 = TreeNode(5, e2, c2)

    print(kth_smallest(r1, 1))
    print(kth_smallest(r2, 3))

