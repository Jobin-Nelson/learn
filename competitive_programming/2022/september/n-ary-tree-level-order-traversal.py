'''
Created Date: 2022-09-05
Qn: Given an n-ary tree, return the level order traversal of its nodes' values.

    Nary-Tree input serialization is represented in their level order traversal,
    each group of children is separated by the null value (See examples).
Link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
Notes:
    - double ended queue for obtaining the node level wise
'''
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def levelOrder(root: Node) -> list[list[int]]:
    if not root: return []
    q = deque()
    q.append(root)
    result = []

    while q:
        qlen = len(q)
        level = []

        for _ in range(qlen):
            node = q.popleft()
            if not node: continue
            level.append(node.val)
            if node.children: q.extend(node.children)
        result.append(level)
    return result

if __name__ == '__main__':
    a1 = Node(5)
    b1 = Node(6)
    c1 = Node(3, [a1, b1])
    d1 = Node(2)
    e1 = Node(4)
    r1 = Node(1, [c1, d1, e1])

    a2 = Node(14)
    b2 = Node(11, [a2])
    c2 = Node(12)
    d2 = Node(13)
    e2 = Node(6)
    f2 = Node(7, [b2])
    g2 = Node(8, [c2])
    h2 = Node(9, [d2])
    i2 = Node(10)
    j2 = Node(2)
    k2 = Node(3, [e2, f2])
    l2 = Node(4, [g2])
    m2 = Node(5, [h2, i2])
    r2 = Node(1, [j2, k2, l2, m2])

    print(levelOrder(r1))
    print(levelOrder(r2))
