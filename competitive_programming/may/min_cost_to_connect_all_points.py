'''
Qn: Return the minimum cost to make all points connected. 
    All points are connected if there is exactly one simple path between any two points.
    Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
Notes:
- build graph with cost and nodes
- use prims algorithm, min heap to pop the mininum cost node at each iteration
'''
import heapq

def minCostConnectPoints(points: list[list[int]]) -> int:
    num_points = len(points)

    # build graph
    adj = {i: [] for i in range(num_points)}
    for i in range(num_points):
        x1, y1 = points[i]
        for j in range(i+1, num_points):
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append((cost, j))
            adj[j].append((cost, i))

    # prim's algorithm
    visited = set()
    minh = [[0, 0]]
    res = 0
    while len(visited) < num_points:
        cost, i = heapq.heappop(minh)
        if i in visited:
            continue
        visited.add(i)
        res += cost
        for costnei, nei in adj[i]:
            if nei not in visited:
                heapq.heappush(minh, [costnei, nei])
    return res

if __name__ == '__main__':
    p1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    p2 = [[3,12],[-2,5],[-4,1]]
    print(minCostConnectPoints(p1))
    print(minCostConnectPoints(p2))

