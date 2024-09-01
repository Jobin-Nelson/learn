"""
Created Date: 2024-08-29
Qn: On a 2D plane, we place n stones at some integer coordinate points. Each
    coordinate point may have at most one stone.

    A stone can be removed if it shares either the same row or the same column
    as another stone that has not been removed.

    Given an array stones of length n where stones[i] = [xi, yi] represents the
    location of the ith stone, return the largest possible number of stones
    that can be removed.
Link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
Notes:
    - use dfs or union find and return len(stones) - num of connected component
"""


def removeStones(stones: list[list[int]]) -> int:
    n = len(stones)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                graph[i].append(j)
                graph[j].append(i)

    visited = [False] * n

    def dfs(stone: int) -> None:
        visited[stone] = True
        for nei in graph[stone]:
            if not visited[nei]:
                dfs(nei)

    connected = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            connected += 1

    return n - connected


if __name__ == '__main__':
    s1 = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    s2 = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    s3 = [[0, 0]]

    print(removeStones(s1))
    print(removeStones(s2))
    print(removeStones(s3))
