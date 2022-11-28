'''
Created Date: 2022-09-07
Qn: Given the root of a binary tree, construct a string consisting of
    parenthesis and integers from a binary tree with the preorder traversal way,
    and return it.

    Omit all the empty parenthesis pairs that do not affect the one-to-one mapping
    relationship between the string and the original binary tree.
Link: https://leetcode.com/problems/construct-string-from-binary-tree/
Notes:
    - dfs and slice to return
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree2str(root: TreeNode | None) -> str:
    res = []

    def preorder(node):
        if not node: return

        res.append('(')
        res.append(str(node.val))
        if not node.left and node.right: res.append('()')
        preorder(node.left)
        preorder(node.right)
        res.append(')')

    preorder(root)
    return ''.join(res)[1:-1]

if __name__ == '__main__':
    a1 = TreeNode(4)
    b1 = TreeNode(2, a1)
    c1 = TreeNode(3)
    r1 = TreeNode(1, b1, c1)

    a2 = TreeNode(4)
    b2 = TreeNode(2, None, a2)
    c2 = TreeNode(3)
    r2 = TreeNode(2, b2, c2)

    print(tree2str(r1))
    print(tree2str(r2))
