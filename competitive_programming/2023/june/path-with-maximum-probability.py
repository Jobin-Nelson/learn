'''
Created Date: 2023-06-28
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
    - use dijkstra's algorithm
'''
import heapq

def maxProbability(n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
    graph = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, succProb[i]))
        graph[v].append((u, succProb[i]))

    max_prob = [0.0] * n
    max_prob[start] = 1.0

    q = [(-1.0, start)]

    while q:
        cur_prob, cur_node = heapq.heappop(q)

        if cur_node == end: return -cur_prob
        
        for next_node, next_prob in graph[cur_node]:
            if -cur_prob * next_prob > max_prob[next_node]:
                max_prob[next_node] = -cur_prob * next_prob
                heapq.heappush(q, (-max_prob[next_node], next_node))
    return 0.0

if __name__ == '__main__':
    n1, ed1, su1, st1, en1 = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2
    n2, ed2, su2, st2, en2 = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2
    n3, ed3, su3, st3, en3 = 3, [[0,1]], [0.5], 0, 2

    print(maxProbability(n1, ed1, su1, st1, en1))
    print(maxProbability(n2, ed2, su2, st2, en2))
    print(maxProbability(n3, ed3, su3, st3, en3))
