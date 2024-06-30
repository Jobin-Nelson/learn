"""
Created Date: 2024-06-30
Qn: Alice and Bob have an undirected graph of n nodes and three types of edges:

        - Type 1: Can be traversed by Alice only. 
        - Type 2: Can be traversed by Bob only. 
        - Type 3: Can be traversed by both Alice and Bob.

    Given an array edges where edges[i] = [typei, ui, vi] represents a
    bidirectional edge of type typei between nodes ui and vi, find the maximum
    number of edges you can remove so that after removing the edges, the graph
    can still be fully traversed by both Alice and Bob. The graph is fully
    traversed by Alice and Bob if starting from any node, they can reach all
    other nodes.

    Return the maximum number of edges you can remove, or return -1 if Alice
    and Bob cannot fully traverse the graph.
Link: https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
Notes:
    - use union find and keep track of edges you are going to keep
"""
class Union:
    def __init__(self, n: int):
        self.parents = list(range(n+1))
        self.components = n
        self.rank = [1] * (n+1)

    def find(self, x: int) -> int:
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[py] > self.rank[px]: px, py = py, px
        self.parents[py] = px
        self.rank[px] += self.rank[py]
        self.components -= 1
        return True

    def is_connected(self) -> bool:
        return self.components == 1

def maxNumEdgesToRemove(n: int, edges: list[list[int]]) -> int:
    alice = Union(n)
    bob = Union(n)

    count = 0

    for t, s, d in edges:
        if t == 3:
            count += (alice.union(s, d) | bob.union(s, d))

    for t, s, d in edges:
        if t == 1:
            count += alice.union(s, d)
        elif t == 2:
            count += bob.union(s, d)
    if alice.is_connected() and bob.is_connected():
        return len(edges) - count
    return -1

if __name__ == '__main__':
    n1, e1 = 4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
    n2, e2 = 4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
    n3, e3 = 4, [[3,2,3],[1,1,2],[2,3,4]]

    print(maxNumEdgesToRemove(n1, e1))
    print(maxNumEdgesToRemove(n2, e2))
    print(maxNumEdgesToRemove(n3, e3))
