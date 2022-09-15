'''
Qn: Return true if and only if it is bipartite.
Link: https://leetcode.com/problems/is-graph-bipartite/
Notes:
    - try to assign alternative values like(0,1) for every node
    - if it can be done the graph is bipartite else not
'''
from collections import deque

def isBipartitie(graph: list[list[int]]) -> bool:
    graph_len = len(graph)
    col = [-1] * graph_len

    for i in range(graph_len):
        if col[i] != -1:
            continue
        q = deque()
        q.append((i, 0))
        while q:
            node, color = q.popleft()
            if col[node] == -1:
                col[node] = color
                for nx in graph[node]:
                    q.append((nx, color^1))
            elif col[node] != color:
                return False
    return True


if __name__ == '__main__':
    g1 = [[1,2,3],[0,2],[0,1,3],[0,2]]
    g2 = [[1,3],[0,2],[1,3],[0,2]]
    print(isBipartitie(g1))
    print(isBipartitie(g2))
