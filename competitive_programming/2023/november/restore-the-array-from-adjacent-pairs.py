'''
Created Date: 2023-11-10
Qn: There is an integer array nums that consists of n unique elements, but you
    have forgotten it. However, you do remember every pair of adjacent elements
    in nums.

    You are given a 2D integer array adjacentPairs of size n - 1 where each
    adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are
    adjacent in nums.

    It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1]
    will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1],
    nums[i]]. The pairs can appear in any order.

    Return the original array nums. If there are multiple solutions, return any
    of them.
Link: https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
Notes:
    - use dfs or iterative approach
    - find root or an edge node, and iterate or dfs your way to the other end
'''
from collections import defaultdict

def restoreArray(adjacentPairs: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    for a, b in adjacentPairs:
        graph[a].append(b)
        graph[b].append(a)

    root = None
    for k, v in graph.items():
        if len(v) == 1:
            root = k
            break
    # dfs approach
    # res = []
    # def dfs(node: int, prev: int):
    #     res.append(node)
    #     for nei in graph[node]:
    #         if nei != prev:
    #             dfs(nei, node)
    # dfs(root, None)

    # iterative approach
    cur = root
    res = [root]
    prev = None
    while len(res) < len(graph):
        for nei in graph[cur]:
            if nei != prev:
                res.append(nei)
                prev = cur
                cur = nei
                break
    return res

if __name__ == '__main__':
    a1 = [[2,1],[3,4],[3,2]]
    a2 = [[4,-2],[1,4],[-3,1]]
    a3 = [[100000,-100000]]

    print(restoreArray(a1))
    print(restoreArray(a2))
    print(restoreArray(a3))
