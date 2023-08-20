'''
Created Date: 2023-08-19
Qn: Given a weighted undirected connected graph with n vertices numbered from 0
    to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents
    a bidirectional and weighted edge between nodes ai and bi. A minimum
    spanning tree (MST) is a subset of the graph's edges that connects all
    vertices without cycles and with the minimum possible total edge weight.

    Find all the critical and pseudo-critical edges in the given graph's
    minimum spanning tree (MST). An MST edge whose deletion from the graph
    would cause the MST weight to increase is called a critical edge. On the
    other hand, a pseudo-critical edge is that which can appear in some MSTs
    but not all.

    Note that you can return the indices of the edges in any order.
Link: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
Notes:
    - use union find data structure
    - ignore each weight and check if weight of MST changes
'''
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.max_size = 1

    def find(self, n: int) -> int:
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return self.parent[n]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]
        self.max_size = max(self.max_size, self.rank[px])
        return True

def findCriticalAndPseudoCriticalEdges(n: int, edges: list[list[int]]) -> list[list[int]]:
    new_edges = [edge.copy() for edge in edges]
    for i, edge in enumerate(new_edges): edge.append(i)
    new_edges.sort(key=lambda x: x[2])

    uf_std = UnionFind(n)
    std_weight = 0
    for u, v, w, _ in new_edges:
        if uf_std.union(u, v):
            std_weight += w

    critical, pseudo_critical = [], []
    for u, v, w, i in new_edges:
        uf_ignore = UnionFind(n)
        ignore_weight = 0
        for x, y, w_ignore, j in new_edges:
            if i != j and uf_ignore.union(x, y):
                ignore_weight += w_ignore

        if uf_ignore.max_size < n or ignore_weight > std_weight:
            critical.append(i)
            continue

        uf_force = UnionFind(n)
        force_weight = w
        uf_force.union(u, v)
        for x, y, w_force, j in new_edges:
            if i != j and uf_force.union(x, y):
                force_weight += w_force

        if force_weight == std_weight:
            pseudo_critical.append(i)

    return [critical, pseudo_critical]

if __name__ == '__main__':
    n1, e1 = 5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    n2, e2 = 4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]

    print(findCriticalAndPseudoCriticalEdges(n1, e1))
    print(findCriticalAndPseudoCriticalEdges(n2, e2))
