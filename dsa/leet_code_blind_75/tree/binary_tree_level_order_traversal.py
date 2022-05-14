'''
Qn: Given the root of a binary tree, return the level order traversal of its nodes' values
i.e. from left to right, level by level
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
Notes:
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: TreeNode) -> list[list[int]]:
    queue = [root]
    res = []

    while queue:
        q_len = len(queue)
        level = []
        for i in range(q_len):
            current = queue.pop(0)
            if current:
                level.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
        if level:
            res.append(level)
    return res



if __name__ == '__main__':
    a1 = TreeNode(9)
    b1 = TreeNode(15)
    c1 = TreeNode(7)
    d1 = TreeNode(20, b1, c1)
    r1 = TreeNode(3, a1, d1)

    r2 = TreeNode(1)

    r3 = TreeNode()

    print(level_order(r1))
    print(level_order(r2))
    print(level_order(r3))

