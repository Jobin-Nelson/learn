'''
Created Date: 2023-02-12
Qn: There is a tree (i.e., a connected, undirected graph with no cycles)
    structure country network consisting of n cities numbered from 0 to n - 1
    and exactly n - 1 roads. The capital city is city 0. You are given a 2D
    integer array roads where roads[i] = [ai, bi] denotes that there exists a
    bidirectional road connecting cities ai and bi.

    There is a meeting for the representatives of each city. The meeting is in
    the capital city.

    There is a car in each city. You are given an integer seats that indicates
    the number of seats in each car.

    A representative can use the car in their city to travel or change the car
    and ride with another representative. The cost of traveling between two
    cities is one liter of fuel.

    Return the minimum number of liters of fuel to reach the capital city.
Link: https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
Notes:
    - use dfs
    - use formulae res += ceil(p / seats) for p people from node to parent
'''
import math

def minimumFuelCost(roads: list[list[int]], seats: int) -> int:
    graph = [[] for _ in range(len(roads) + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    res = 0
    def dfs(node: int, parent: int) -> int:
        nonlocal res
        people = 1
        for nei in graph[node]:
            if nei == parent: continue
            people += dfs(nei, node)

        if node > 0: res += int(math.ceil(people / seats))
        return people
    dfs(0, -1)
    return res

if __name__ == '__main__':
    r1, s1 = [[0,1],[0,2],[0,3]], 5
    r2, s2 = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], 2

    print(minimumFuelCost(r1, s1))
    print(minimumFuelCost(r2, s2))
