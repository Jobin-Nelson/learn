'''
Qn: Given two binary trees original and cloned and given a reference to a node target in the original tree.
    The cloned tree is a copy of the original tree.
    Return a reference to the same node in the cloned tree.
Link: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
Notes:
    - dfs till you find the target and return the node in the cloned tree
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    def dfs(node1, node2):
        if not node1: return None
        if node1 == target:
            return node2
        return dfs(node1.left, node2.left) or dfs(node1.right, node2.right)
    return dfs(original , cloned)

if __name__ == '__main__':
    ao1 = TreeNode(6)
    bo1 = TreeNode(19)
    co1 = TreeNode(3, ao1, bo1)
    do1 = TreeNode(4)
    ro1 = TreeNode(7, do1, co1)
    t1 = co1
    ac1 = TreeNode(6)
    bc1 = TreeNode(19)
    cc1 = TreeNode(3, ac1, bc1)
    dc1 = TreeNode(4)
    rc1 = TreeNode(7, dc1, cc1)

    ao2 = TreeNode(1)
    bo2 = TreeNode(2, right=ao2)
    co2 = TreeNode(3, right=bo2)
    do2 = TreeNode(4, right=co2)
    eo2 = TreeNode(5, right=do2)
    fo2 = TreeNode(6, right=eo2)
    ro2 = TreeNode(8, right=fo2)
    t2 = do2
    ac2 = TreeNode(1)
    bc2 = TreeNode(2, right=ac2)
    cc2 = TreeNode(3, right=bc2)
    dc2 = TreeNode(4, right=cc2)
    ec2 = TreeNode(5, right=dc2)
    fc2 = TreeNode(6, right=ec2)
    rc2 = TreeNode(8, right=fc2)

    print(getTargetCopy(ro1, rc1, t1).val)
    print(getTargetCopy(ro2, rc2, t2).val)
