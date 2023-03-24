'''
Created Date: 2023-03-24
Qn: There are n cities numbered from 0 to n - 1 and n - 1 roads such that there
    is only one way to travel between two different cities (this network form a
    tree). Last year, The ministry of transport decided to orient the roads in
    one direction because they are too narrow.

    Roads are represented by connections where connections[i] = [ai, bi]
    represents a road from city ai to city bi.

    This year, there will be a big event in the capital (city 0), and many
    people want to travel to this city.

    Your task consists of reorienting some roads such that each city can visit
    the city 0. Return the minimum number of edges changed.

    It's guaranteed that each city can reach city 0 after reorder.
Link: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
Notes:
    - use bidirectional graph
    - dfs from 0 if there exists a reverse flow increment res
'''
from collections import defaultdict

def minReoder(n: int, connections: list[list[int]]) -> int:
    res = 0

    roads = set()
    adj = defaultdict(list)
    for a, b in connections:
        roads.add((a, b))
        adj[a].append(b)
        adj[b].append(a)

    def dfs(node: int, parent: int) -> None:
        nonlocal res
        res += (parent, node) in roads

        for nei in adj[node]:
            if nei == parent: continue
            dfs(nei, node)
    dfs(0, -1)
    return res
if __name__ == '__main__':
    n1, c1 = 6, [[0,1],[1,3],[2,3],[4,0],[4,5]]
    n2, c2 = 5, [[1,0],[1,2],[3,2],[3,4]]
    n3, c3 = 3, [[1,0],[2,0]]

    print(minReoder(n1, c1))
    print(minReoder(n2, c2))
    print(minReoder(n3, c3))
