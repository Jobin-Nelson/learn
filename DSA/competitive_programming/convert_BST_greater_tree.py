'''
Qn: Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key 
of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
Link: https://leetcode.com/problems/convert-bst-to-greater-tree/
Notes:
- use a instance variable to track the sum by recursing to the right node then carrying the sum to the left node
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def dfs(node):
            if not node: return
            dfs(node.right)
            self.sum += node.val
            node.val = self.sum
            dfs(node.left)
        dfs(root)
        return root

def list_tree_rec(root: TreeNode) -> list:
    if root == None: return []
    queue = [root]
    res = []

    while queue:
        current = queue.pop(0)
        res.append(current.val)
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return res


if __name__ == '__main__':
    a = TreeNode(0)
    b = TreeNode(3)
    c = TreeNode(5)
    d = TreeNode(8)
    e = TreeNode(2, right=b)
    f = TreeNode(7, right=d)
    g = TreeNode(1, a, e)
    h = TreeNode(6, c, f)
    r = TreeNode(4, g, h)
    print(list_tree_rec(r))
    sol = Solution()
    print(list_tree_rec(sol.convertBST(r)))