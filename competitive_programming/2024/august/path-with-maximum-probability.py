"""
Created Date: 2024-08-31
Qn: You are given an undirected weighted graph of n nodes (0-indexed),
    represented by an edge list where edges[i] = [a, b] is an undirected edge
    connecting the nodes a and b with a probability of success of traversing
    that edge succProb[i].

    Given two nodes start and end, find the path with the maximum probability
    of success to go from start to end and return its success probability.

    If there is no path from start to end, return 0. Your answer will be
    accepted if it differs from the correct answer by at most 1e-5.
Link: https://leetcode.com/problems/path-with-maximum-probability/
Notes:
    - use dijkstras
"""

import heapq


def maxProbability(
    n: int,
    edges: list[list[int]],
    succProb: list[float],
    start_node: int,
    end_node: int,
) -> float:
    graph = [[] for _ in range(n)]
    for edge, prob in zip(edges, succProb):
        graph[edge[0]].append((edge[1], prob))
        graph[edge[1]].append((edge[0], prob))

    max_prob = [0.0] * n
    max_prob[start_node] = 1.0

    q = [(-1.0, start_node)]
    while q:
        cur_prob, node = heapq.heappop(q)
        if node == end_node:
            return -cur_prob
        for next_node, prob in graph[node]:
            if -cur_prob * prob > max_prob[next_node]:
                max_prob[next_node] = -cur_prob * prob
                heapq.heappush(q, (-max_prob[next_node], next_node))
    return 0.0


if __name__ == '__main__':
    n1, e11, sp1, s1, e12 = 3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2
    n2, e21, sp2, s2, e22 = 3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2
    n3, e31, sp3, s3, e32 = 3, [[0, 1]], [0.5], 0, 2
    n4, e41, sp4, s4, e42 = (
        5,
        [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
        [0.37, 0.17, 0.93, 0.23, 0.39, 0.04],
        3,
        4,
    )

    print(maxProbability(n1, e11, sp1, s1, e12))
    print(maxProbability(n2, e21, sp2, s2, e22))
    print(maxProbability(n3, e31, sp3, s3, e32))
    print(maxProbability(n4, e41, sp4, s4, e42))
