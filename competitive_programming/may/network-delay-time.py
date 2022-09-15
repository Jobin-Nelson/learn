'''
Qn: You are given a network of n nodes, labeled from 1 to n. You are also given times, 
    a list of travel times as directed edges times[i] = (ui, vi, wi), 
    where ui is the source node, vi is the target node, 
    and wi is the time it takes for a signal to travel from source to target.
    We will send a signal from a given node k. 
    Return the time it takes for all the n nodes to receive the signal. 
    If it is impossible for all the n nodes to receive the signal, return -1.
Link: https://leetcode.com/problems/network-delay-time/
Notes:
    - use djikstra's algorithm (min heap) to get the shortest time to every node 
'''
from collections import defaultdict
import heapq

def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)

    for source, target, time in times:
        graph[source].append((target, time))

    min_heap = [(0, k)]
    visited = set()
    delay = 0
    while min_heap:
        time, target = heapq.heappop(min_heap)
        if target in visited:
            continue
        visited.add(target)
        delay = max(delay, time)
        for nei_target, nei_time in graph[target]:
            if nei_target not in visited:
                heapq.heappush(min_heap, (nei_time + time, nei_target))
    return delay if len(visited) == n else -1

if __name__ == '__main__':
    t1, n1, k1 = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
    t2, n2, k2 = [[1,2,1]], 2, 1
    t3, n3, k3 = [[1,2,1]], 2, 2
    print(networkDelayTime(t1, n1, k1))
    print(networkDelayTime(t2, n2, k2))
    print(networkDelayTime(t3, n3, k3))
