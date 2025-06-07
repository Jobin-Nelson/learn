"""
Created Date: 2025-06-05
Qn: You are given two strings of the same length s1 and s2 and a string
    baseStr.

    We say s1[i] and s2[i] are equivalent characters.

    - For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b'
      == 'd', and 'c' == 'e'. Equivalent characters follow the usual rules of
      any equivalence relation:

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
    - use bfs
    - use hashmap to store the earliest node
"""

import unittest
from collections import defaultdict, deque
from string import ascii_lowercase


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(list)

        for c1, c2 in zip(s1, s2):
            adj[c1].append(c2)
            adj[c2].append(c1)

        earliest = {}
        for c in ascii_lowercase:
            if c not in earliest:
                earliest[c] = c
                q = deque([c])

                while q:
                    current = q.popleft()
                    for v in adj[current]:
                        if v not in earliest:
                            earliest[v] = c
                            q.append(v)

        return ''.join(earliest[c] for c in baseStr)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_smallestEquivalentString1(self):
        s1, s2 = "parker", "morris"
        baseStr = "parser"
        expected = "makkek"
        self.assertEqual(expected, self.sol.smallestEquivalentString(s1, s2, baseStr))

    def test_smallestEquivalentString2(self):
        s1, s2 = "hello", "world"
        baseStr = "hold"
        expected = "hdld"
        self.assertEqual(expected, self.sol.smallestEquivalentString(s1, s2, baseStr))

    def test_smallestEquivalentString3(self):
        s1, s2 = "leetcode", "programs"
        baseStr = "sourcecode"
        expected = "aauaaaaada"
        self.assertEqual(expected, self.sol.smallestEquivalentString(s1, s2, baseStr))


if __name__ == '__main__':
    unittest.main()
