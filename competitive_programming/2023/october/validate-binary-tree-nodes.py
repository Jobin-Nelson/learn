'''
Created Date: 2023-10-17
Qn: You have n binary tree nodes numbered from 0 to n - 1 where node i has two
    children leftChild[i] and rightChild[i], return true if and only if all the
    given nodes form exactly one valid binary tree.

    If node i has no left child then leftChild[i] will equal -1, similarly for
    the right child.

    Note that the nodes have no values and that we only use the node numbers in
    this problem.
Link: https://leetcode.com/problems/validate-binary-tree-nodes/
Notes:
    - use bfs or union find
'''
from collections import deque

class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.components = n
    def find(self, n: int) -> int:
        res = n
        while self.parents[res] != res:
            self.parents[res] = self.parents[self.parents[res]]
            res = self.parents[res]
        return res
    def union(self, parent: int, child: int) -> bool:
        parent_parent, child_parent = self.find(parent), self.find(child)
        if child_parent != child or parent_parent == child_parent: return False
        self.parents[child_parent] = parent_parent
        self.components -= 1
        return True

def validateBinaryTreeNodes(n: int, leftChild: list[int], rightChild: list[int]) -> bool:
    # Union Find
    uf = UnionFind(n)
    for node in range(n):
        for child in (leftChild[node], rightChild[node]):
            if child == -1: continue
            if not uf.union(node, child): return False
    return uf.components == 1


    # BFS
    # def find_root() -> int:
    #     children = set(leftChild) | set(rightChild)
    #     for i in range(n):
    #         if i not in children: return i
    #     return -1
    # root = find_root()
    # if root == -1: return False
    #
    # seen = [False] * n
    # seen[root] = True
    # q = deque([root])
    # while q:
    #     node = q.popleft()
    #     for child in (leftChild[node], rightChild[node]):
    #         if child != -1:
    #             if seen[child]: return False
    #             seen[child] = True
    #             q.append(child)
    # return all(i for i in seen)

if __name__ == '__main__':
    n1, l1, r1 = 4, [1, -1, 3, -1], [2, -1, -1, -1]
    n2, l2, r2 = 4, [1, -1, 3, -1], [2, 3, -1, -1]
    n3, l3, r3 = 2, [1, 0], [-1, -1]
    
    print(validateBinaryTreeNodes(n1, l1, r1))
    print(validateBinaryTreeNodes(n2, l2, r2))
    print(validateBinaryTreeNodes(n3, l3, r3))
