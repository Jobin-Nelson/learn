'''
Created Date: 2023-06-04
Qn: There are n cities. Some of them are connected, while some are not. If city
    a is connected directly with city b, and city b is connected directly with
    city c, then city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cities and no
    other cities outside of the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if
    the ith city and the jth city are directly connected, and isConnected[i][j]
    = 0 otherwise.

    Return the total number of provinces.
Link: https://leetcode.com/problems/number-of-provinces/
Notes:
'''
from collections import defaultdict, deque

def findCircleNum(isConnected: list[list[int]]) -> int:
    N = len(isConnected)
    graph = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if isConnected[i][j]:
                graph[i].append(j)

    q = deque()

if __name__ == '__main__':
    i1 = [[1,1,0],[1,1,0],[0,0,1]]
    i2 = [[1,0,0],[0,1,0],[0,0,1]]

    print(findCircleNum(i1))
    print(findCircleNum(i2))
