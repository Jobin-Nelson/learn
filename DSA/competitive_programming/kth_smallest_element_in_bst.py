'''
Qn: Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Notes:
- use stack to get access to parent nodes while decrementing k and return the value when k hits zero
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
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
    b1 = TreeNode(1, right=a1)
    c1 = TreeNode(4)
    r1 = TreeNode(3, b1, c1)

    a2 = TreeNode(1)
    b2 = TreeNode(2, a2)
    c2 = TreeNode(4)
    d2 = TreeNode(3, b2, c2)
    e2 = TreeNode(6)
    r2 = TreeNode(5, d2, e2)

    print(kthSmallest(r1, 1))
    print(kthSmallest(r2, 3))