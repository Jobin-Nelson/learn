"""
Created Date: 2024-07-28
Qn: A city is represented as a bi-directional connected graph with n vertices
    where each vertex is labeled from 1 to n (inclusive). The edges in the
    graph are represented as a 2D integer array edges, where each edges[i] =
    [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
    Every vertex pair is connected by at most one edge, and no vertex has an
    edge to itself. The time taken to traverse any edge is time minutes.

    Each vertex has a traffic signal which changes its color from green to red
    and vice versa every change minutes. All signals change at the same time.
    You can enter a vertex at any time, but can leave a vertex only when the
    signal is green. You cannot wait at a vertex if the signal is green.

    The second minimum value is defined as the smallest value strictly larger
    than the minimum value.

    - For example the second minimum value of [2, 3, 4] is 3, and the second
      minimum value of [2, 2, 4] is 4. 

    Given n, edges, time, and change, return the second minimum time it will
    take to go from vertex 1 to vertex n.

    Notes:

        - You can go through any vertex any number of times, including 1 and n. 
        - You can assume that when the journey starts, all signals have just
          turned green.
Link: https://leetcode.com/problems/second-minimum-time-to-reach-destination/
Notes:
    - use bfs
"""

from collections import defaultdict, deque


def secondMinimum(n: int, edges: list[list[int]], time: int, change: int) -> int:
    graph = defaultdict(list)
    for s, d in edges:
        graph[s].append(d)
        graph[d].append(s)

    q = deque([1])
    cur_time = 0
    res = -1
    visit_times = defaultdict(list)

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node == n:
                if res != -1:
                    return cur_time
                res = cur_time
            for nei in graph[node]:
                nei_times = visit_times[nei]
                if len(nei_times) == 0 or (
                    len(nei_times) == 1 and nei_times[0] != cur_time
                ):
                    q.append(nei)
                    nei_times.append(cur_time)
        if (cur_time // change) & 1:
            cur_time += change - (cur_time % change)
        cur_time += time
    return -1


if __name__ == '__main__':
    n1, e1, t1, c1 = 5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5
    n2, e2, t2, c2 = 2, [[1, 2]], 3, 2

    print(secondMinimum(n1, e1, t1, c1))
    print(secondMinimum(n2, e2, t2, c2))
