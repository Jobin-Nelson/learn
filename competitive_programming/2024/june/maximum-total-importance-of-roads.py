"""
Created Date: 2024-06-28
Qn: You are given an integer n denoting the number of cities in a country. The
    cities are numbered from 0 to n - 1.

    You are also given a 2D integer array roads where roads[i] = [ai, bi]
    denotes that there exists a bidirectional road connecting cities ai and bi.

    You need to assign each city with an integer value from 1 to n, where each
    value can only be used once. The importance of a road is then defined as
    the sum of the values of the two cities it connects.

    Return the maximum total importance of all roads possible after assigning
    the values optimally.
Link: https://leetcode.com/problems/maximum-total-importance-of-roads/
Notes:
    - use indegrees
"""
def maximumImportance(n: int, roads: list[list[int]]) -> int:
    indegrees = [0] * n
    for s, d in roads:
        indegrees[s] += 1
        indegrees[d] += 1
        
    indegrees.sort()
    value = 1
    res = 0
    for d in indegrees:
        res += value * d
        value += 1
    return res

if __name__ == '__main__':
    n1, r1 = 5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
    n2, r2 = 5, [[0,3],[2,4],[1,3]]

    print(maximumImportance(n1, r1))
    print(maximumImportance(n2, r2))
