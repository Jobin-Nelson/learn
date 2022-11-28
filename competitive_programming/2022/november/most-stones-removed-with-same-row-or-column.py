'''
Created Date: 2022-11-14
Qn: On a 2D plane, we place n stones at some integer coordinate points. Each
    coordinate point may have at most one stone.

    A stone can be removed if it shares either the same row or the same column
    as another stone that has not been removed.

    Given an array stones of length n where stones[i] = [xi, yi] represents the
    location of the ith stone, return the largest possible number of stones
    that can be removed.
Link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
Notes:
    - answer should be len(stones) - non connected components
    - as all connected components can be removed
    - to find all non connected components traverse and add all connected nodes
      to visited set
'''
from collections import defaultdict, deque

def removeStones(stones: list[list[int]]) -> int:
    graph_x = defaultdict(list)
    graph_y = defaultdict(list)

    for x, y in stones:
        graph_x[x].append(y)
        graph_y[y].append(x)

    non_connected_components = 0
    visited = set()

    for x, y in stones:
        if (x, y) not in visited:
            q = deque([(x, y)])
            while q:
                xo, yo = q.popleft()

                if (xo, yo) not in visited:
                    visited.add((xo, yo))
                    for nei_y in graph_x[xo]:
                        q.append((xo, nei_y))
                    for nei_x in graph_y[yo]:
                        q.append((nei_x, yo))
            non_connected_components += 1

    return len(stones) - non_connected_components

if __name__ == '__main__':
    s1 = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    s2 = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    s3 = [[0,0]]

    print(removeStones(s1))
    print(removeStones(s2))
    print(removeStones(s3))
