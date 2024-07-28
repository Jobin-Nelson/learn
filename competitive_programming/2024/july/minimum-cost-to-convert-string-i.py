"""
Created Date: 2024-07-27
Qn: You are given two 0-indexed strings source and target, both of length n and
    consisting of lowercase English letters. You are also given two 0-indexed
    character arrays original and changed, and an integer array cost, where
    cost[i] represents the cost of changing the character original[i] to the
    character changed[i].

    You start with the string source. In one operation, you can pick a
    character x from the string and change it to the character y at a cost of z
    if there exists any index j such that cost[j] == z, original[j] == x, and
    changed[j] == y.

    Return the minimum cost to convert the string source to the string target
    using any number of operations. If it is impossible to convert source to
    target, return -1.

    Note that there may exist indices i, j such that original[j] == original[i]
    and changed[j] == changed[i].
Link: https://leetcode.com/problems/minimum-cost-to-convert-string-i/
Notes:
    - use dijstra
"""

import heapq
from collections import defaultdict
import string


def minimumCost(
    source: str, target: str, original: list[str], changed: list[str], cost: list[int]
) -> int:
    graph = defaultdict(list)

    for s, d, c in zip(original, changed, cost):
        graph[s].append((d, c))

    def dijkstra(src: str) -> dict[str, int]:
        heap = [(0, src)]
        min_cost_map = {}
        while heap:
            cost, node = heapq.heappop(heap)
            if node in min_cost_map:
                continue
            min_cost_map[node] = cost
            for nei, nei_cost in graph[node]:
                heapq.heappush(heap, (cost + nei_cost, nei))
        return min_cost_map

    min_cost_maps = {c: dijkstra(c) for c in string.ascii_lowercase}
    res = 0

    for src, dst in zip(source, target):
        if dst not in min_cost_maps[src]:
            return -1
        res += min_cost_maps[src][dst]
    return res


if __name__ == '__main__':
    s1, t1, o1, ch1, co1 = (
        "abcd",
        "acbe",
        ["a", "b", "c", "c", "e", "d"],
        ["b", "c", "b", "e", "b", "e"],
        [2, 5, 5, 1, 2, 20],
    )
    s2, t2, o2, ch2, co2 = "aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]
    s3, t3, o3, ch3, co3 = "abcd", "abce", ["a"], ["e"], [10000]

    print(minimumCost(s1, t1, o1, ch1, co1))
    print(minimumCost(s2, t2, o2, ch2, co2))
    print(minimumCost(s3, t3, o3, ch3, co3))
