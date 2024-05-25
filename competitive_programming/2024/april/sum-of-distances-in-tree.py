"""
Created Date: 2024-04-28
Qn: There is an undirected connected tree with n nodes labeled from 0 to n - 1
    and n - 1 edges.

    You are given the integer n and the array edges where edges[i] = [ai, bi]
    indicates that there is an edge between nodes ai and bi in the tree.

    Return an array answer of length n where answer[i] is the sum of the
    distances between the ith node in the tree and all other nodes.
Link: https://leetcode.com/problems/sum-of-distances-in-tree/
Notes:
    - compute the sum without traversing the graph
    - parent_sum - closer_nodes + further_nodes
"""
from collections import defaultdict

def sumOfDistanceInTree(n: int, edges: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    closer_nodes_count = [0] * n
    res = [0] * n
    visited = [False] * n
    def dfs1(node: int) -> int:
        nonlocal closer_nodes_count, res, visited
        closer_nodes = 1

        for nei in graph[node]:
            if not visited[nei]:
                visited[nei] = True
                child_closer_count = dfs1(nei)
                closer_nodes += child_closer_count
                res[0] += child_closer_count

        closer_nodes_count[node] = closer_nodes
        return closer_nodes

    visited[0] = True
    dfs1(0)

    def dfs2(node: int) -> None:
        nonlocal res, visited

        for nei in graph[node]:
            if not visited[nei]:
                visited[nei] = True
                res[nei] = res[node] - closer_nodes_count[nei] + (n - closer_nodes_count[nei])
                dfs2(nei)

    visited = [False] * n
    visited[0] = True
    dfs2(0)
    return res


    # TLE DFS solution
    # graph = defaultdict(list)
    # for a, b in edges:
    #     graph[a].append(b)
    #     graph[b].append(a)
    #
    # def dfs(node: int, depth: int, visited: list[bool]) -> int:
    #     res = depth
    #     for nei in graph[node]:
    #         if not visited[nei]:
    #             visited[nei] = True
    #             res += dfs(nei, depth + 1, visited)
    #     return res
    #
    # res = []
    # for node in range(n):
    #     visited = [False] * n
    #     visited[node] = True
    #     res.append(dfs(node, 0, visited))
    # return res

if __name__ == '__main__':
    n1, e1 = 6, [[0,1],[0,2],[2,3],[2,4],[2,5]]
    n2, e2 = 1, []
    n3, e3 = 2, [[1,0]]

    print(sumOfDistanceInTree(n1, e1))
    print(sumOfDistanceInTree(n2, e2))
    print(sumOfDistanceInTree(n3, e3))
