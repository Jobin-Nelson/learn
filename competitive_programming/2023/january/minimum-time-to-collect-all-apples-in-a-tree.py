'''
Created Date: 2023-01-11
Qn: Given an undirected tree consisting of n vertices numbered from 0 to n-1,
    which has some apples in their vertices. You spend 1 second to walk over
    one edge of the tree. Return the minimum time in seconds you have to spend
    to collect all apples in the tree, starting at vertex 0 and coming back to
    this vertex.

    The edges of the undirected tree are given in the array edges, where
    edges[i] = [ai, bi] means that exists an edge connecting the vertices ai
    and bi. Additionally, there is a boolean array hasApple, where hasApple[i]
    = true means that vertex i has an apple; otherwise, it does not have any
    apple.
Link: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
Notes:
    - use graph
    - count the number of nodes that have apple discounting the parent node
'''
def minTime(n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    def dfs(node: int, parent: int) -> int:
        res = 0
        for nei in graph[node]:
            if nei != parent:
                res += dfs(nei, node)
        if res or hasApple[node]:
            return res + 2
        return res
    return max(dfs(0, -1)-2, 0)

if __name__ == '__main__':
    n1, e1, h1 = 7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]
    n2, e2, h2 = 7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False]
    n3, e3, h3 = 7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False]

    print(minTime(n1, e1, h1))
    print(minTime(n2, e2, h2))
    print(minTime(n3, e3, h3))
