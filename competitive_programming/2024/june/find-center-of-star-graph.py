"""
Created Date: 2024-06-27
Qn: There is an undirected star graph consisting of n nodes labeled from 1 to
    n. A star graph is a graph where there is one center node and exactly n - 1
    edges that connect the center node with every other node.

    You are given a 2D integer array edges where each edges[i] = [ui, vi]
    indicates that there is an edge between the nodes ui and vi. Return the
    center of the given star graph.
Link: https://leetcode.com/problems/find-center-of-star-graph/
Notes:
    - calculate indegrees
"""
def findCenter(edges: list[list[int]]) -> int:
    n = len(edges) + 2
    indegrees = [0] * n
    for s, d in edges:
        indegrees[s] += 1
        indegrees[d] += 1
    return next((i for i, indegree in enumerate(indegrees) if indegree == n-2), 0)

if __name__ == '__main__':
    e1 = [[1,2],[2,3],[4,2]]
    e2 = [[1,2],[5,1],[1,3],[1,4]]

    print(findCenter(e1))
    print(findCenter(e2))
