'''
Created Date: 2023-07-11
Qn: Given the root of a binary tree, the value of a target node target, and an
    integer k, return an array of the values of all nodes that have a distance
    k from the target node.

    You can return the answer in any order.
Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
Notes:
    - use equivalent graph (undirected graph)
'''
from typing import Self
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def from_list(cls, arr: list[int | None]) -> Self | None:
        N = len(arr)
        def inner(i: int) -> Self | None:
            if i >= N or arr[i] is None: return None
            node = cls(arr[i])
            node.left = inner(2 * i + 1)
            node.right = inner(2 * i + 2)
            return node
        return inner(0)

    def __str__(self) -> str:
        res = []
        q = deque([self])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)
    def __repr__(self) -> str:
        return self.__str__()

def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    graph = defaultdict(list)
    def build_graph(cur: TreeNode, parent: TreeNode | None):
        if cur and parent:
            graph[cur.val].append(parent.val)
            graph[parent.val].append(cur.val)
        if cur.left: build_graph(cur.left, cur)
        if cur.right: build_graph(cur.right, cur)
    build_graph(root, None)

    res = []
    visited = set([target.val])
    q = deque([(target.val, 0)])
    while q:
        node, dist = q.popleft()
        if dist == k:
            res.append(node)
            continue
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))
    return res

if __name__ == '__main__':
    r1, k1 = TreeNode.from_list([3,5,1,6,2,0,8,None,None,7,4]), 2
    t1 = r1.right
    r2, t2, k2 = TreeNode.from_list([1]), TreeNode(1), 3

    print(distanceK(r1, t1, k1))
    print(distanceK(r2, t2, k2))
