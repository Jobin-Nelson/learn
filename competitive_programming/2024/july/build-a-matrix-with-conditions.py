"""
Created Date: 2024-07-21
Qn: You are given a positive integer k. You are also given:

    - a 2D integer array rowConditions of size n where rowConditions[i] =
      [abovei, belowi], and 
    - a 2D integer array colConditions of size m where colConditions[i] =
      [lefti, righti]. The two arrays contain integers from 1 to k.

    You have to build a k x k matrix that contains each of the numbers from 1
    to k exactly once. The remaining cells should have the value 0.

    The matrix should also satisfy the following conditions:

    - The number abovei should appear in a row that is strictly above the row
      at which the number belowi appears for all i from 0 to n - 1. 
    - The number lefti should appear in a column that is strictly left of the
      column at which the number righti appears for all i from 0 to m - 1. 

    Return any matrix that satisfies the conditions. If no answer exists,
    return an empty matrix.
Link: https://leetcode.com/problems/build-a-matrix-with-conditions/
Notes:
    - use topological ordering
"""
from collections import defaultdict

def buildMatrix(k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
    def dfs(src: int, graph: defaultdict[int, list[int]], visit: set[int], path: set[int], order: list[int]) -> bool:
        if src in path:
            return False
        if src in visit:
            return True

        visit.add(src)
        path.add(src)

        for nei in graph[src]:
            if not dfs(nei, graph, visit, path, order):
                return False

        path.remove(src)
        order.append(src)
        return True

    def topo(edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)

        visit, path = set(), set()
        order = []

        for src in range(1, k+1):
            if not dfs(src, graph, visit, path, order):
                return []
        return order[::-1]

    row_order = topo(rowConditions)
    col_order = topo(colConditions)

    if not row_order or not col_order:
        return []

    val_to_row = {n: i for i, n in enumerate(row_order)}
    val_to_col = {n: i for i, n in enumerate(col_order)}

    res = [[0] * k for _ in range(k)]

    for num in range(1,k+1):
        r, c = val_to_row[num], val_to_col[num]
        res[r][c] = num
    return res


if __name__ == '__main__':
    k1, r1, c1 = 3, [[1,2],[3,2]], [[2,1,],[3,2]]
    k2, r2, c2 = 3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]]

    print(buildMatrix(k1, r1, c1))
    print(buildMatrix(k2, r2, c2))
