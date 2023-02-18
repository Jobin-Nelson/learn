'''
Created Date: 2023-02-11
Qn: You are given an integer n, the number of nodes in a directed graph where
    the nodes are labeled from 0 to n - 1. Each edge is red or blue in this
    graph, and there could be self-edges and parallel edges.

    You are given two arrays redEdges and blueEdges where:

        - redEdges[i] = [ai, bi] indicates that there is a directed red edge
          from node ai to node bi in the graph, and 
        - blueEdges[j] = [uj, vj] indicates that there is a directed blue edge
          from node uj to node vj in the graph. 

    Return an array answer of length n, where each answer[x] is the length of
    the shortest path from node 0 to node x such that the edge colors alternate
    along the path, or -1 if such a path does not exist.
Link: https://leetcode.com/problems/shortest-path-with-alternating-colors/
Notes:
    - use bfs
    - use enum to alternate between two colors while iterating
'''
from collections import deque
from enum import Enum

class Color(Enum):
    Init = 0
    Red = 1
    Blue = 2

def shortestAlternatingPaths(n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
    res = [-1] * n
    graph = [[] for _ in range(n)]
    q = deque([(0, Color.Init)])

    for a, b in redEdges: graph[a].append((b, Color.Red))
    for a, b in blueEdges: graph[a].append((b, Color.Blue))

    step = 0
    while q:
        for _ in range(len(q)):
            node, prev_color = q.popleft()
            if res[node] == -1: res[node] = step

            for i, (nei, edge_color) in enumerate(graph[node]):
                if nei == -1 or edge_color == prev_color: continue
                q.append((nei, edge_color))
                graph[node][i] = (-1, edge_color)
        step += 1
    return res

if __name__ == '__main__':
    n1, r1, e1 = 3, [[0,1],[1,2]], []
    n2, r2, e2 = 3, [[0,1]], [[2,1]]

    print(shortestAlternatingPaths(n1, r1, e1))
    print(shortestAlternatingPaths(n2, r2, e2))
