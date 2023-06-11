'''
Created Date: 2023-06-04
Qn: There are n cities. Some of them are connected, while some are not. If city
    a is connected directly with city b, and city b is connected directly with
    city c, then city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cities and no
    other cities outside of the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if
    the ith city and the jth city are directly connected, and isConnected[i][j]
    = 0 otherwise.

    Return the total number of provinces.
Link: https://leetcode.com/problems/number-of-provinces/
Notes:
    - use union find for finding the number of connected components in a graph
'''
def findCircleNum(isConnected: list[list[int]]) -> int:
    N = len(isConnected)
    parent = list(range(N))
    rank = [1] * N

    def find(n: int) -> int:
        res = n
        while res != parent[res]:
            parent[res] = parent[parent[res]]
            res = parent[res]
        return res
    
    def union(n1: int, n2: int) -> int:
        p1, p2 = find(n1), find(n2)
        if p1 == p2: return 0
        if rank[p1] > rank[p2]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        return 1
    
    # return N - sum(union(i, j) for i in range(N) for j in range(N) if isConnected[i][j])
    res = N
    for i in range(N):
        for j in range(N):
            if isConnected[i][j]:
                res -= union(i, j)
    return res

# === UnionFind class ===
# class UnionFind:
#     def __init__(self, n: int):
#         self.parent = list(range(n))
#         self.rank = [1] * n
#
#     def find(self, n: int) -> int:
#         res = n
#         while res != self.parent[res]:
#             self.parent[res] = self.parent[self.parent[res]]
#             res = self.parent[res]
#         return res
#     
#     def union(self, n1: int, n2: int) -> int:
#         p1, p2 = self.find(n1), self.find(n2)
#         if p1 == p2: return 0
#         if self.rank[p1] > self.rank[p2]:
#             self.parent[p1] = p2
#             self.rank[p2] += self.rank[p1]
#         else:
#             self.parent[p2] = p1
#             self.rank[p1] += self.rank[p2]
#         return 1

# === BFS approach ===
# def findCircleNum(isConnected: list[list[int]]) -> int:
#     N = len(isConnected)
#     graph = [[] for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             if isConnected[i][j]:
#                 graph[i].append(j)
#                 graph[j].append(i)
#
#     visited = [False] * N
#     def bfs(n: int) -> bool:
#         if visited[n]: return False
#         visited[n] = True
#         q = deque([n])
#         while q:
#             city = q.popleft()
#             for nei in graph[city]:
#                 if not visited[nei]:
#                     visited[nei] = True
#                     q.append(nei)
#         return True
#     
#     return sum(bfs(i) for i in range(N))

if __name__ == '__main__':
    i1 = [[1,1,0],[1,1,0],[0,0,1]]
    i2 = [[1,0,0],[0,1,0],[0,0,1]]

    print(findCircleNum(i1))
    print(findCircleNum(i2))
