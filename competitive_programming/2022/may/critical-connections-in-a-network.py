'''
Qn: There are n servers numbered from 0 to n - 1 connected by 
    undirected server-to-server connections forming a network 
    where connections[i] = [ai, bi] represents a connection between 
    servers ai and bi. Any server can reach other servers directly or 
    indirectly through the network. A critical connection is a connection that, 
    if removed, will make some servers unable to reach some other server.
    Return all critical connections in the network in any order.
Link: https://leetcode.com/problems/critical-connections-in-a-network/
Notes:
    - Tarjan's algorithm
    - track two attributes lowtime and discovery
    - update lowtime for all strongly connected nodes to have the same min values
    - update output when low[next] > dis[cur]
'''
from collections import defaultdict

def criticalConnections(n: int, connections: list[list[int]]) -> list[list[int]]:
    dis, low = [0]*n, [0]*n
    time = 0
    visited = set()
    output = []
    graph = defaultdict(list)

    for s, t in connections:
        graph[s].append(t)
        graph[t].append(s)

    def dfs(cur, prev):
        nonlocal time
        visited.add(cur)
        time += 1
        dis[cur] = low[cur] = time

        for next in graph[cur]:
            # not in visited
            if next not in visited:
                dfs(next, cur)
                low[cur] = min(low[cur], low[next])
            elif next!=prev:
                low[cur] = min(low[cur], dis[next])
            if low[next] > dis[cur]:
                output.append([cur, next])
    dfs(0, -1)
    return output

if __name__ == '__main__':
    n1, c1 = 4, [[0,1],[1,2],[2,0],[1,3]]
    n2, c2 = 2, [[0, 1]]
    print(criticalConnections(n1, c1))
    print(criticalConnections(n2, c2))

