'''
Created Date: 2023-06-02
Qn: You are given a list of bombs. The range of a bomb is defined as the area
    where its effect can be felt. This area is in the shape of a circle with
    the center as the location of the bomb.

    The bombs are represented by a 0-indexed 2D integer array bombs where
    bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate
    of the location of the ith bomb, whereas ri denotes the radius of its
    range.

    You may choose to detonate a single bomb. When a bomb is detonated, it will
    detonate all bombs that lie in its range. These bombs will further detonate
    the bombs that lie in their ranges.

    Given the list of bombs, return the maximum number of bombs that can be
    detonated if you are allowed to detonate only one bomb.
Link: https://leetcode.com/problems/detonate-the-maximum-bombs/
Notes:
    - build graph
    - use dfs
'''
import math
from collections import defaultdict

def maximumDetonation(bombs: list[list[int]]) -> int:
    def distance(b1: list[int], b2: list[int]) -> float:
        return math.sqrt((b1[0]-b2[0])**2 + (b1[1]-b2[1])**2)
    
    graph = defaultdict(list)
    for i in range(len(bombs)):
        for j in range(i+1, len(bombs)):
            *b1, r1 = bombs[i]
            *b2, r2 = bombs[j]
            d = distance(b1, b2)
            if r1 >= d: graph[i].append(j)
            if r2 >= d: graph[j].append(i)

    def dfs(i: int, visited: set[int]) -> int:
        if i in visited: return 0
        visited.add(i)
        for nei in graph[i]:
            dfs(nei, visited)
        return len(visited)

    max_bombs = 1
    for i in range(len(bombs)):
        max_bombs = max(max_bombs, dfs(i, set()))
    return max_bombs

if __name__ == '__main__':
    b1 = [[2,1,3],[6,1,4]]
    b2 = [[1,1,5],[10,10,5]]
    b3 = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    b4 = [[1,1,100000],[100000,100000,1]]

    print(maximumDetonation(b1))
    print(maximumDetonation(b2))
    print(maximumDetonation(b3))
    print(maximumDetonation(b4))
