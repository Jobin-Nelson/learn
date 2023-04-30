'''
Created Date: 2023-04-30
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
    - use union find
'''
def maxNumEdgesToRemove(n: int, edges: list[list[int]]) -> int:
    parent = list(range(n+1))
    rank = [0] * (n+1)
    def find(x: int, parent: list[int]) -> int:
        if x != parent[x]:
            parent[x] = find(parent[x], parent)
        return parent[x]
    
    def union(x: int, y: int, parent: list[int]):
        px, py = find(x, parent), find(y, parent)
        if px == py: return False
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1
        return True

    res = alice_edges = bob_edges = 0
    
    # for type 3
    for t, u, v in edges:
        if t == 3:
            if union(u, v, parent):
                alice_edges += 1
                bob_edges += 1
            else:
                res += 1

    # for type 1
    parent1 = parent[:]
    for t, u, v in edges:
        if t == 1:
            if union(u, v, parent):
                alice_edges += 1
            else:
                res += 1

    # for type 2
    for t, u, v in edges:
        if t == 2:
            if union(u, v, parent1):
                bob_edges += 1
            else:
                res += 1

    return res if alice_edges == bob_edges == n-1 else -1

if __name__ == '__main__':
    n1, e1 = 4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
    n2, e2 = 4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
    n3, e3 = 4, [[3,2,3],[1,1,2],[2,3,4]]

    print(maxNumEdgesToRemove(n1, e1))
    print(maxNumEdgesToRemove(n2, e2))
    print(maxNumEdgesToRemove(n3, e3))
