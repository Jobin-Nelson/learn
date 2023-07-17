'''
Created Date: 2023-07-13
Qn: There are a total of numCourses courses you have to take, labeled from 0 to
    numCourses - 1. You are given an array prerequisites where prerequisites[i]
    = [ai, bi] indicates that you must take course bi first if you want to take
    course ai.

        - For example, the pair [0, 1], indicates that to take course 0 you
          have to first take course 1.

    Return true if you can finish all courses. Otherwise, return false.
Link: https://leetcode.com/problems/course-schedule/
Notes:
    - Khan's algorithm
        - bfs traversal start from node with indegree = 0
        - decrement indegree for each neighbours
        - add neighbours to queue if indegree = 0
        - at the end check cycles by visited nodes == total nodes
    - DFS
        - dfs and keep track of instack nodes
'''
from collections import deque

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # DFS
    def dfs(node: int, visited: list[bool], inStack: list[bool]) -> bool:
        if inStack[node]: return True
        if visited[node]: return False
        visited[node] = True
        inStack[node] = True
        for nei in adj[node]:
            if dfs(nei, visited, inStack): return True
        inStack[node] = False
        return False

    adj = [[] for _ in range(numCourses)]
    for u, v in prerequisites: adj[v].append(u)
    inStack = [False] * numCourses
    visited = [False] * numCourses

    for i in range(numCourses):
        if dfs(i, visited, inStack): return False
    return True

    # # Topological sort (Kahn's algorithm)
    # indegrees = [0] * numCourses
    # adj = [[] for _ in range(numCourses)]
    #
    # for u, v in prerequisites:
    #     adj[v].append(u)
    #     indegrees[u] += 1
    #
    # q = deque(i for i in range(numCourses) if indegrees[i] == 0)
    # visited = 0
    #
    # while q:
    #     node = q.popleft()
    #     visited += 1
    #     for nei in adj[node]:
    #         indegrees[nei] -= 1
    #         if indegrees[nei] == 0: q.append(nei)
    # return visited == numCourses

if __name__ == '__main__':
    n1, p1 = 2, [[1,0]]
    n2, p2 = 2, [[1,0],[0,1]]

    print(canFinish(n1, p1))
    print(canFinish(n2, p2))
