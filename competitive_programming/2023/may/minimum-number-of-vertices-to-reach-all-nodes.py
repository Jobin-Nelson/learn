'''
Created Date: 2023-05-18
Qn: Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and
    an array edges where edges[i] = [fromi, toi] represents a directed edge
    from node fromi to node toi.

    Find the smallest set of vertices from which all nodes in the graph are
    reachable. It's guaranteed that a unique solution exists.

    Notice that you can return the vertices in any order.
Link: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
Notes:
    - use indegrees
    - return all vertices with an indegree of zero
'''
def findSmallestSetOfVertices(n: int, edges: list[list[int]]) -> list[int]:
    indegree = [False] * n

    for _, d in edges:
        indegree[d] = True

    return [i for i in range(n) if not indegree[i]]

if __name__ == '__main__':
    n1, e1 = 6, [[0,1],[0,2],[2,5],[3,4],[4,2]]
    n2, e2 = 5, [[0,1],[2,1],[3,1],[1,4],[2,4]]

    print(findSmallestSetOfVertices(n1, e1))
    print(findSmallestSetOfVertices(n2, e2))
