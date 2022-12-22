'''
Created Date: 2022-12-22
Qn: There is an undirected connected tree with n nodes labeled from 0 to n - 1
    and n - 1 edges.

    You are given the integer n and the array edges where edges[i] = [ai, bi]
    indicates that there is an edge between nodes ai and bi in the tree.

    Return an array answer of length n where answer[i] is the sum of the
    distances between the ith node in the tree and all other nodes.
Link: https://leetcode.com/problems/sum-of-distances-in-tree/
Notes:
'''
def sumOfDistancesInTree(n: int, edges: list[list[int]]) -> list[int]:
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    count = [1] * n
    res = [0] * n
    def dfs(node: int = 0, parent: int | None = None) -> None:
        for child in adj[node]:
            if child != parent:
                dfs(child, node)
                count[node] += count[child]
                res[node] += res[child] + count[child]
    def dfs2(node: int = 0, parent: int | None = None) -> None:
        for child in adj[node]:
            if child != parent:
                res[child] = res[node] - count[child] + n - count[child]
                dfs2(child, node)
    dfs()
    dfs2()

    return res

if __name__ == '__main__':
    n1, e1 = 6, [[0,1],[0,2],[2,3],[2,4],[2,5]]
    n2, e2 = 1, []
    n3, e3 = 2, [[1, 0]]

    print(sumOfDistancesInTree(n1, e1))
    print(sumOfDistancesInTree(n2, e2))
    print(sumOfDistancesInTree(n3, e3))
