'''
Created Date: 2023-02-27
Qn: Given a n * n matrix grid of 0's and 1's only. We want to represent the
    grid with a Quad-Tree.

    Return the root of the Quad-Tree representing the grid.

    Notice that you can assign the value of a node to True or False when isLeaf is
    False, and both are accepted in the answer.

    A Quad-Tree is a tree data structure in which each internal node has
    exactly four children. Besides, each node has two attributes:

        - val: True if the node represents a grid of 1's or False if the node
          represents a grid of 0's. 
        - isLeaf: True if the node is leaf node on the tree or False if the
          node has the four children.

    class Node {
        public boolean val;
        public boolean isLeaf;
        public Node topLeft;
        public Node topRight;
        public Node bottomLeft;
        public Node bottomRight;
    }

    We can construct a Quad-Tree from a two-dimensional area using the
    following steps:

    If the current grid has the same value (i.e all 1's or all 0's) set isLeaf
    True and set val to the value of the grid and set the four children to Null
    and stop. 

    If the current grid has different values, set isLeaf to False and set val
    to any value and divide the current grid into four sub-grids as shown in
    the photo. Recurse for each of the children with the proper sub-grid.

    Quad-Tree format:

    The output represents the serialized format of a Quad-Tree using level
    order traversal, where null signifies a path terminator where no node
    exists below.

    It is very similar to the serialization of the binary tree. The only
    difference is that the node is represented as a list [isLeaf, val].

    If the value of isLeaf or val is True we represent it as 1 in the list
    [isLeaf, val] and if the value of isLeaf or val is False we represent it as
    0.

Link: https://leetcode.com/problems/construct-quad-tree/
Notes:
    - use dfs (like binary tree but with four children)
'''
from __future__ import annotations
from collections import deque

class Node:
    def __init__(self, val: bool, isLeaf: bool,
                 topLeft: Node | None,
                 topRight: Node | None,
                 bottomLeft: Node | None,
                 bottomRight: Node | None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def __str__(self) -> str:
        res = []
        q = deque([self])

        while q:
            node = q.popleft()
            res.append([int(node.isLeaf), int(node.val)])
            if node.topLeft: q.append(node.topLeft)
            if node.topRight: q.append(node.topRight)
            if node.bottomLeft: q.append(node.bottomLeft)
            if node.bottomRight: q.append(node.bottomRight)
        return str(res)

def construct(grid: list[list[int]]) -> Node | None:
    def dfs(rs: int, cs: int, re: int, ce: int) -> Node | None:
        if rs > re or cs > ce: return None
        isLeaf = True
        val = grid[rs][cs]
        for i in range(rs, re + 1):
            for j in range(cs, ce + 1):
                if grid[i][j] != val:
                    isLeaf = False
                    break
            if not isLeaf: break
        if isLeaf: return Node(val == 1, True, None, None, None, None)
        rm = (rs + re) >> 1
        cm = (cs + ce) >> 1
        topLeft = dfs(rs, cs, rm, cm)
        topRight = dfs(rs, cm+1, rm, ce)
        bottomLeft = dfs(rm+1, cs, re, cm)
        bottomRight = dfs(rm+1, cm+1, re, ce)
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
    return dfs(0, 0, len(grid)-1, len(grid[0])-1)

if __name__ == '__main__':
    g1 = [[0,1],[1,0]]
    g2 = [[1,1,1,1,0,0,0,0],
          [1,1,1,1,0,0,0,0],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,0,0,0,0],
          [1,1,1,1,0,0,0,0],
          [1,1,1,1,0,0,0,0],
          [1,1,1,1,0,0,0,0]]

    print(construct(g1))
    print(construct(g2))
