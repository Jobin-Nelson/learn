'''
Created Date: 2022-09-02
Qn: Given the root of a binary tree, return the average value of the nodes on
    each level in the form of an array. Answers within 10-5 of the actual answer
    will be accepted.
Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
Notes:
    - level order traversal and get average at each level
'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root: TreeNode | None) -> list[float]:
    result = []
    q = deque()
    q.append(root)

    while q:
        qlen = len(q)
        level = []
        for _ in range(qlen):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        result.append(sum(level) / len(level))
    return result

if __name__ == '__main__':
    a1 = TreeNode(15)
    b1 = TreeNode(7)
    c1 = TreeNode(9)
    d1 = TreeNode(20, a1, b1)
    r1 = TreeNode(3, c1, d1)

    a2 = TreeNode(15)
    b2 = TreeNode(7)
    c2 = TreeNode(9, a2, b2)
    d2 = TreeNode(20)
    r2 = TreeNode(3, c2, d2)

    print(averageOfLevels(r1))
    print(averageOfLevels(r2))

