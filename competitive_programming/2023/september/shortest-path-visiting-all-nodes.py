'''
Created Date: 2023-09-17
Qn: You have an undirected, connected graph of n nodes labeled from 0 to n - 1.
    You are given an array graph where graph[i] is a list of all the nodes
    connected with node i by an edge.

    Return the length of the shortest path that visits every node. You may
    start and stop at any node, you may revisit nodes multiple times, and you
    may reuse edges.
Link: https://leetcode.com/problems/shortest-path-visiting-all-nodes/
Notes:
    - use bfs to find the shortest path but use state of the path traversed to
      mark visited
'''
from collections import deque

def shortestPathLength(graph: list[list[int]]) -> int:
    # shortestPath, allVisited = float('inf'), (1 << len(graph)) - 1
    # for u in range(len(graph)):
    #     q = deque([(u, 1 << u)])
    #     seen, lvl = set(q), 0
    #     while q:
    #         if any(nodeVisited == allVisited for _, nodeVisited in q):
    #             shortestPath = min(shortestPath, lvl)
    #             break
    #         q, lvl = [(v, nodeVisited | (1<<v)) for u, nodeVisited in q for v in graph[u] if (v, nodeVisited | (1 << v)) not in seen and not seen.add((v, nodeVisited | (1 << v)))], lvl + 1
    # return shortestPath

    if len(graph) <= 1: return 0
    shortest_path, all_visited = float('inf'), (1 << len(graph)) - 1
    for u in range(len(graph)):
        q = deque([(u, 1 << u)])
        seen, lvl = set(q), 0
        while q:
            lvl += 1
            for _ in range(len(q)):
                cur_node, node_visited = q.popleft()
                for v in graph[cur_node]:
                    next_visited = node_visited | (1 << v)
                    if (v, next_visited) not in seen:
                        seen.add((v, next_visited))
                        q.append((v, next_visited))
                    if next_visited == all_visited:
                        shortest_path = min(shortest_path, lvl)
                        break
    return shortest_path

    # all_visited = (1 << len(graph)) - 1
    # def bfs(node: int) -> int:
    #     q = deque([(node, 1 << node)])
    #     visited, lvl, res = set(q), 0, float('inf')
    #     while q:
    #         cur_node, cur_path = q.popleft()
    #         if any(nv == all_visited for _, nv in q):
    #             res = min(res, lvl)
    #             return res
    #         lvl += 1
    #         for nex_node in graph[cur_node]:
    #             nex_path = cur_path | (1 << nex_node)
    #             if (nex_node, nex_path) not in visited:
    #                 visited.add((nex_node, nex_path))
    #                 q.append((nex_node, nex_path))
    #     return res
    # return min(bfs(i) for i in range(len(graph)))


if __name__ == '__main__':
    g1 = [[1,2,3],[0],[0],[0]]
    g2 = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    
    print(shortestPathLength(g1))
    print(shortestPathLength(g2))
