'''
Created Date: 2023-03-23
Qn: There are n computers numbered from 0 to n - 1 connected by ethernet cables
    connections forming a network where connections[i] = [ai, bi] represents a
    connection between computers ai and bi. Any computer can reach any other
    computer directly or indirectly through the network.

    You are given an initial computer network connections. You can extract
    certain cables between two directly connected computers, and place them
    between any pair of disconnected computers to make them directly connected.

    Return the minimum number of times you need to do this in order to make all
    the computers connected. If it is not possible, return -1.
Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
Notes:
    - if len(connections) < n -1 then we can't connect all nodes
    - min number of connections to make is number of components - 1
'''
def makeConnected(n: int, connections: list[list[int]]) -> int:
    if len(connections) < n-1: return -1

    adj = [set() for _ in range(n)]
    for u, v in connections:
        adj[u].add(v)
        adj[v].add(u)

    visited = [0] * n

    def dfs(i: int) -> int:
        if visited[i]: return 0
        visited[i] = 1
        
        for nei in adj[i]:
            dfs(nei)
        return 1

    return sum(dfs(i) for i in range(n)) - 1

if __name__ == '__main__':
    n1, c1 = 4, [[0,1],[0,2],[1,2]]
    n2, c2 = 6, [[0,1],[0,2],[0,3],[1,2],[1,3]]
    n3, c3 = 6, [[0,1],[0,2],[0,3],[1,2]]

    print(makeConnected(n1, c1))
    print(makeConnected(n2, c2))
    print(makeConnected(n3, c3))
