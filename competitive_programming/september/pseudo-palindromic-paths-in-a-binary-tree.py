'''
Created Date: 2022-09-14
Qn: Given a binary tree where node values are digits from 1 to 9. A path in the
    binary tree is said to be pseudo-palindromic if at least one permutation of the
    node values in the path is a palindrome.

    Return the number of pseudo-palindromic paths going from the root node to leaf
    nodes.
Link: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
Notes:
    - depth first search and keep track of the set of node.val
    - at each leaf check if the len of set is less than or equal to 1
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pseudoPalindromicPaths(root: TreeNode | None) -> int:

    def traverse(node, pairs):
        if not node: return 0

        if node.val in pairs: pairs.remove(node.val)
        else: pairs.add(node.val)

        if not node.left and not node.right:
            return 1 if len(pairs) <= 1 else 0

        return traverse(node.left, set(pairs)) + traverse(node.right, set(pairs))
    return traverse(root, set())

if __name__ == '__main__':
    a1 = TreeNode(3)
    b1 = TreeNode(1)
    c1 = TreeNode(1)
    d1 = TreeNode(3, a1, b1)
    e1 = TreeNode(1, None, c1)
    r1 = TreeNode(2, d1, e1)

    a2 = TreeNode(1)
    b2 = TreeNode(1)
    c2 = TreeNode(3, None, a2)
    d2 = TreeNode(1, b2, c2)
    e2 = TreeNode(1)
    r2 = TreeNode(2, d2, e2)

    r3 = TreeNode(9)

    print(pseudoPalindromicPaths(r1))
    print(pseudoPalindromicPaths(r2))
    print(pseudoPalindromicPaths(r3))
