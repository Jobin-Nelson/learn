'''
Created Date: 2023-10-18
Qn: You are given an integer n, which indicates that there are n courses
    labeled from 1 to n. You are also given a 2D integer array relations where
    relations[j] = [prevCoursej, nextCoursej] denotes that course prevCoursej
    has to be completed before course nextCoursej (prerequisite relationship).
    Furthermore, you are given a 0-indexed integer array time where time[i]
    denotes how many months it takes to complete the (i+1)th course.

    You must find the minimum number of months needed to complete all the
    courses following these rules:

        - You may start taking a course at any time if the prerequisites are
          met.
        - Any number of courses can be taken at the same time.

    Return the minimum number of months needed to complete all the courses.

    Note: The test cases are generated such that it is possible to complete
    every course (i.e., the graph is a directed acyclic graph).
Link: https://leetcode.com/problems/parallel-courses-iii/
Notes:
    - use topological sort or dfs
'''
from functools import cache
from collections import deque

def minimumTime(n: int, relations: list[list[int]], time: list[int]) -> int:
    # topological sort
    max_time = [0] * n
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for prev, nex in relations:
        graph[prev-1].append(nex-1)
        indegree[nex-1] += 1

    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            max_time[i] = time[i]
            q.append(i)

    while q:
        node = q.popleft()
        for nei in graph[node]:
            max_time[nei] = max(max_time[nei], max_time[node] + time[nei])
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return max(max_time)

    # dfs
    # @cache
    # def dfs(node: int) -> int:
    #     if not graph[node]: return time[node]
    #     res = 0
    #     for nei in graph[node]:
    #         res = max (res, dfs(nei))
    #     return time[node] + res
    # graph = [[] for _ in range(n+1)]
    # for prev, nex in relations:
    #     graph[prev-1].append(nex-1)
    # return max(dfs(node) for node in range(n))

if __name__ == '__main__':
    n1, r1, t1 = 3, [[1,3], [2,3]], [3,2,5]
    n2, r2, t2 = 5, [[1,5],[2,5],[3,5],[3,4],[4,5]], [1,2,3,4,5]

    print(minimumTime(n1, r1, t1))
    print(minimumTime(n2, r2, t2))
