'''
Created Date: 2023-04-28
Qn: Two strings X and Y are similar if we can swap two letters (in different
    positions) of X, so that it equals Y. Also two strings X and Y are similar
    if they are equal.

    For example, "tars" and "rats" are similar (swapping at positions 0 and 2),
    and "rats" and "arts" are similar, but "star" is not similar to "tars",
    "rats", or "arts".

    Together, these form two connected groups by similarity: {"tars", "rats",
    "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group
    even though they are not similar.  Formally, each group is such that a word
    is in the group if and only if it is similar to at least one other word in
    the group.

    We are given a list strs of strings where every string in strs is an
    anagram of every other string in strs. How many groups are there?
Link: https://leetcode.com/problems/similar-string-groups/
Notes:
    - use connected graphs or union find
'''
from collections import defaultdict, deque

def numSimilarGroups(strs: list[str]) -> int:
    def areNeighbors(a: str, b: str) -> bool:
        dif = 0
        for i in range(len(a)):
            if a[i] != b[i]: dif += 1
        return dif == 0 or dif == 2

    graph = defaultdict(list)
    for i in range(len(strs)):
        for j in range(i+1, len(strs)):
            if areNeighbors(strs[i], strs[j]):
                graph[strs[i]].append(strs[j])
                graph[strs[j]].append(strs[i])

    visited = set()
    def bfs(node: str) -> None:
        q = deque([node])
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)

    res = 0
    for i in range(len(strs)):
        if strs[i] not in visited:
            visited.add(strs[i])
            bfs(strs[i])
            res += 1

    return res

if __name__ == '__main__':
    s1 = ["tars","rats","arts","star"]
    s2 = ["omv","ovm"]

    print(numSimilarGroups(s1))
    print(numSimilarGroups(s2))
