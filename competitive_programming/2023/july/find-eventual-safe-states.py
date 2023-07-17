'''
Created Date: 2023-07-12
Qn: There is a directed graph of n nodes with each node labeled from 0 to n -
    1. The graph is represented by a 0-indexed 2D integer array graph where
       graph[i] is an integer array of nodes adjacent to node i, meaning there
       is an edge from node i to each node in graph[i].

    A node is a terminal node if there are no outgoing edges. A node is a safe
    node if every possible path starting from that node leads to a terminal
    node (or another safe node).

    Return an array containing all the safe nodes of the graph. The answer
    should be sorted in ascending order.
Link: https://leetcode.com/problems/find-eventual-safe-states/
Notes:
    - use dfs
'''
def eventualSafeNodes(graph: list[list[int]]) -> list[int]:
    def dfs(node: int, adj: list[list[int]], visit: list[bool], inStack: list[bool]) -> bool:
        if inStack[node]: return True
        if visit[node]: return False
        visit[node] = True
        inStack[node] = True
        for nei in adj[node]:
            if dfs(nei, adj, visit, inStack): return True
        inStack[node] = False
        return False
    N = len(graph)
    adj = [[] for _ in range(N)]
    for i in range(N):
        for node in graph[i]:
            adj[i].append(node)
    visit = [False] * N
    inStack = [False] * N

    for i in range(N):
        dfs(i, adj, visit, inStack)
    
    safeNodes = [i for i in range(N) if not inStack[i]]
    return safeNodes

if __name__ == '__main__':
    g1 = [[1,2],[2,3],[5],[0],[5],[],[]]
    g2 = [[1,2,3,4],[1,2],[3,4],[0,4],[]]

    print(eventualSafeNodes(g1))
    print(eventualSafeNodes(g2))
