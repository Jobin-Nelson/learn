'''
Created Date: 2022-09-01
Qn: Given a binary tree root, a node X in the tree is named good if in the path
    from root to X there are no nodes with a value greater than X.

    Return the number of good nodes in the binary tree.
Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Notes:
- dfs and track the good nodes
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    def count_good_nodes(node, cur_max):
        if node is None: return 0
        count = 1 if node.val >= cur_max else 0
        count += count_good_nodes(node.left, max(cur_max, node.val))
        count += count_good_nodes(node.right, max(cur_max, node.val))
        return count

    return count_good_nodes(root, root.val)

if __name__ == '__main__':
    a1 = TreeNode(3)
    b1 = TreeNode(1)
    c1 = TreeNode(5)
    d1 = TreeNode(1, a1)
    e1 = TreeNode(4, b1, c1)
    r1 = TreeNode(3, d1, e1)

    a2 = TreeNode(4)
    b2 = TreeNode(2)
    c2 = TreeNode(3, a2, b2)
    r2 = TreeNode(3, c2)
    
    print(goodNodes(r1))
    print(goodNodes(r2))

