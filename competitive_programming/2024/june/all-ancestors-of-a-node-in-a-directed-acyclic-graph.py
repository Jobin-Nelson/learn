"""
Created Date: 2024-06-29
Qn: You are given a positive integer n representing the number of nodes of a
    Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1
    (inclusive).

    You are also given a 2D integer array edges, where edges[i] = [fromi, toi]
    denotes that there is a unidirectional edge from fromi to toi in the graph.

    Return a list answer, where answer[i] is the list of ancestors of the ith
    node, sorted in ascending order.

    A node u is an ancestor of another node v if u can reach v via a set of
    edges.
Link: https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
Notes:
    - use topological sorting
"""
def getAncestors(n: int, edges: list[list[int]]) -> list[list[int]]:
    graph = [[] for _ in range(n)]
    indegrees = [0] * n

    for s, d in edges:
        graph[s].append(d)
        indegrees[d] += 1

    zero_indegress = [i for i, v in enumerate(indegrees) if v == 0]
    topological_order = []

    while zero_indegress:
        node = zero_indegress.pop(0)
        topological_order.append(node)
        for nei in graph[node]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                zero_indegress.append(nei)

    ancestors_set_list = [set() for _ in range(n)]
    ancestors_list = [[] for _ in range(n)]

    for node in topological_order:
        for nei in graph[node]:
            ancestors_set_list[nei].add(node)
            ancestors_set_list[nei].update(ancestors_set_list[node])

    for i in range(n):
        ancestors_list[i].extend(ancestors_set_list[i])
        ancestors_list[i].sort()
    return ancestors_list

if __name__ == '__main__':
    n1, e1 = 8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    n2, e2 = 5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    print(getAncestors(n1, e1))
    print(getAncestors(n2, e2))
