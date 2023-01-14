'''
Created Date: 2023-01-14
Qn: You are given two strings of the same length s1 and s2 and a string baseStr.

    We say s1[i] and s2[i] are equivalent characters.

        - For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c',
          'b' == 'd', and 'c' == 'e'.

    Equivalent characters follow the usual rules of any equivalence relation:

        - Reflexivity: 'a' == 'a'.
        - Symmetry: 'a' == 'b' implies 'b' == 'a'.
        - Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.

    For example, given the equivalency information from s1 = "abc" and s2 =
    "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab"
    is the lexicographically smallest equivalent string of baseStr.

    Return the lexicographically smallest equivalent string of baseStr by using
    the equivalency information from s1 and s2.
Link: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
Notes:
'''
from collections import defaultdict

# def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
#     uf = dict()
#
#     def find(x: str) -> str:
#         uf.setdefault(x, x)
#         if x != uf[x]:
#             uf[x] = find(uf[x])
#         return uf[x]
#
#     def union(x: str, y: str) -> None:
#         rootx = find(x)
#         rooty = find(y)
#         if rootx > rooty:
#             uf[rootx] = rooty
#         else:
#             uf[rooty] = rootx
#
#     for i in range(len(s1)):
#         union(s1[i], s2[i])
#
#     return ''.join(find(c) for c in baseStr)

def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    graph = defaultdict(list)
    
    for a, b in zip(s1, s2):
        graph[a].append(b)
        graph[b].append(a)

    def find_min(s: str, visited: set) -> str:
        visited.add(s)
        for nei in graph[s]:
            if nei not in visited:
                s = min(s, find_min(nei, visited))
        return s

    res, memo = list(), dict()
    for c in baseStr:
        if c in memo: 
            res.append(memo[c])
            continue
        memo[c] = find_min(c, set())
        res.append(memo[c])
    return ''.join(res)

if __name__ == '__main__':
    s1, s1, b1 = "parker", "morris", "parser"
    s2, s2, b2 = "hello", "world", "hold"
    s3, s3, b3 = "leetcode", "programs", "sourcecode"

    print(smallestEquivalentString(s1, s1, b1))
    print(smallestEquivalentString(s2, s2, b2))
    print(smallestEquivalentString(s3, s3, b3))
