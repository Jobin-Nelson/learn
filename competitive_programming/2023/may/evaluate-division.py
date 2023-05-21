'''
Created Date: 2023-05-20
Qn: You are given an array of variable pairs equations and an array of real
    numbers values, where equations[i] = [Ai, Bi] and values[i] represent the
    equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a
    single variable.

    You are also given some queries, where queries[j] = [Cj, Dj] represents the
    jth query where you must find the answer for Cj / Dj = ?.

    Return the answers to all queries. If a single answer cannot be determined,
    return -1.0.

    Note: The input is always valid. You may assume that evaluating the queries
    will not result in division by zero and that there is no contradiction.
Link: https://leetcode.com/problems/evaluate-division/
Notes:
    - use graph
'''
from collections import defaultdict, deque

def calcEquation(
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]]
    ) -> list[float]:

    graph = defaultdict(list)
    for i, (s, d) in enumerate(equations):
        graph[s].append((d, values[i]))
        graph[d].append((s, 1 / values[i]))

    def bfs(src: str, dest: str) -> float:
        if src not in graph or dest not in graph: return -1.0
        q, visited = deque([(src, 1)]), set([src])

        while q:
            n, w = q.popleft()
            if n == dest: return w
            for nei, nei_w in graph[n]:
                if nei not in visited:
                    q.append((nei, w * nei_w))
                    visited.add(nei)
        return -1.0
    
    return [bfs(s, d) for s, d in queries]

if __name__ == '__main__':
    e1, v1, q1 = [["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    e2, v2, q2 = [["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    e3, v3, q3 = [["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]

    print(calcEquation(e1, v1, q1))
    print(calcEquation(e2, v2, q2))
    print(calcEquation(e3, v3, q3))
