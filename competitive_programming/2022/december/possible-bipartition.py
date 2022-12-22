'''
Created Date: 2022-12-21
Qn: We want to split a group of n people (labeled from 1 to n) into two groups
    of any size. Each person may dislike some other people, and they should not
    go into the same group.

    Given the integer n and the array dislikes where dislikes[i] = [ai, bi]
    indicates that the person labeled ai does not like the person labeled bi,
    return true if it is possible to split everyone into two groups in this
    way.
Link: https://leetcode.com/problems/possible-bipartition/
Notes:
    - use bipartite graph
    - adjacency list and an array to keep track of the colors or dislikes
'''
from collections import deque

def possibleBipartition(n:int, dislikes: list[list[int]]) -> bool:
    def bfs(source: int) -> bool:
        q = deque([source])
        color[source] = 0
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if color[nei] == color[node]: return False
                if color[nei] == -1:
                    color[nei] = 1 - color[node]
                    q.append(nei)
        return True

    adj = [[] for _ in range(n+1)]
    for a, b in dislikes:
        adj[a].append(b)
        adj[b].append(a)

    color = [-1] * (n+1)
    for i in range(1, n+1):
        if color[i] == -1:
            if not bfs(i): return False
    return True

if __name__ == '__main__':
    n1, d1 = 4, [[1,2],[1,3],[2,4]]
    n2, d2 = 3, [[1,2],[1,3],[2,3]]
    n3, d3 = 5, [[1,2],[2,3],[3,4],[4,5],[1,5]]

    print(possibleBipartition(n1, d1))
    print(possibleBipartition(n2, d2))
    print(possibleBipartition(n3, d3))
