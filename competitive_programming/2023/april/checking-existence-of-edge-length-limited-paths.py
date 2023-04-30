'''
Created Date: 2023-04-29
Qn: An undirected graph of n nodes is defined by edgeList, where edgeList[i] =
    [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi.
    Note that there may be multiple edges between two nodes.

    Given an array queries, where queries[j] = [pj, qj, limitj], your task is
    to determine for each queries[j] whether there is a path between pj and qj
    such that each edge on the path has a distance strictly less than limitj .

    Return a boolean array answer, where answer.length == queries.length and
    the jth value of answer is true if there is a path for queries[j] is true,
    and false otherwise.
Link: https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
Notes:
    - use union find
'''
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)

        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            elif self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[py] = px
                self.rank[px] += 1

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

def distanceLimitedPathsExist(n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:
    sorted_edges = sorted(edgeList, key = lambda x: x[2])
    uf = UnionFind(n)
    res = [False] * len(queries)
    i = 0

    sorted_queries = sorted(enumerate(queries), key= lambda x: x[1][2])
    for q_idx, (u, v, max_dist) in sorted_queries:
        while i < len(sorted_edges) and sorted_edges[i][2] < max_dist:
            uf.union(sorted_edges[i][0], sorted_edges[i][1])
            i += 1
        res[q_idx] = uf.is_connected(u, v)

    return res

if __name__ == '__main__':
    n1, e1, q1 = 3, [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], [[0,1,2],[0,2,5]]
    n2, e2, q2 = 5, [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], [[0,4,14],[1,4,13]]

    print(distanceLimitedPathsExist(n1, e1, q1))
    print(distanceLimitedPathsExist(n2, e2, q2))
