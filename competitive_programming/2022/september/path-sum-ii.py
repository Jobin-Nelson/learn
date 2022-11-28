'''
Created Date: 2022-09-24
Qn: Given the root of a binary tree and an integer targetSum, return all
    root-to-leaf paths where the sum of the node values in the path equals
    targetSum. Each path should be returned as a list of the node values, not node
    references.

    A root-to-leaf path is a path starting from the root and ending at any leaf
    node. A leaf is a node with no children.
Link: https://leetcode.com/problems/path-sum-ii/
Notes:
    - dfs and pass in a list with all the node values
    - at each leaf check if the sum of all the node values matches targetSum
    - append the list of node values to the result if it is a match
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: TreeNode | None, targetSum: int) -> list[list[int]]:
    result = []
    def dfs(node: TreeNode, target: int, path: list) -> list[list[int]] | None:
        nonlocal result, targetSum
        target += node.val
        tmp = path +  [node.val]

        if node.left: dfs(node.left, target, tmp)
        if node.right: dfs(node.right, target, tmp)

        if not node.left and not node.right and target == targetSum: result.append(tmp)
    
    if not root: return []
    dfs(root, 0, [])
    return result

if __name__ == '__main__':
    a1 = TreeNode(7)
    b1 = TreeNode(2)
    c1 = TreeNode(5)
    d1 = TreeNode(1)
    e1 = TreeNode(11, a1, b1)
    f1 = TreeNode(13)
    g1 = TreeNode(4, c1, d1)
    h1 = TreeNode(4, e1)
    i1 = TreeNode(8, f1, g1)
    r1 = TreeNode(5, h1, i1)

    a2 = TreeNode(2)
    b2 = TreeNode(3)
    r2 = TreeNode(1, a2, b2)

    print(pathSum(r1, 22))
    print(pathSum(r2, 5))

