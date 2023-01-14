'''
Created Date: 2023-01-12
Qn: You are given a tree (i.e. a connected, undirected graph that has no
    cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1
    edges. The root of the tree is the node 0, and each node of the tree has a
    label which is a lower-case character given in the string labels 
    (i.e. The node with the number i has the label labels[i]).

    The edges array is given on the form edges[i] = [ai, bi], which means there
    is an edge between nodes ai and bi in the tree.

    Return an array of size n where ans[i] is the number of nodes in the
    subtree of the ith node which have the same label as node i.

    A subtree of a tree T is the tree consisting of a node in T and all of its
    descendant nodes.
Link: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
Notes:
    - use graph
    - use hashmap to update the result
'''
from collections import Counter

def countSubTrees(n: int, edges: list[list[int]], labels: str) -> list[int]:
    graph = {i: [] for i in range(n)}
    res = [0] * n
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node: int, parent: int) -> Counter:
        nonlocal res
        count = Counter()
        for nei in graph[node]:
            if nei != parent:
                count += dfs(nei, node)
        count[labels[node]] += 1
        res[node] = count[labels[node]]
        return count
    dfs(0, -1)
    return res

if __name__ == '__main__':
    n1, e1, l1 = 7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd"
    n2, e2, l2 = 4, [[0,1],[1,2],[0,3]], "bbbb"
    n3, e3, l3 = 5, [[0,1],[0,2],[1,3],[0,4]], "aabab"

    print(countSubTrees(n1, e1, l1))
    print(countSubTrees(n2, e2, l2))
    print(countSubTrees(n3, e3, l3))
