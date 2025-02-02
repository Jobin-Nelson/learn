"""
Created Date: 2025-01-30
Qn: You are given a positive integer n representing the number of nodes in an
    undirected graph. The nodes are labeled from 1 to n.

    You are also given a 2D integer array edges, where edges[i] = [ai, bi]
    indicates that there is a bidirectional edge between nodes ai and bi.
    Notice that the given graph may be disconnected.

    Divide the nodes of the graph into m groups (1-indexed) such that:

    - Each node in the graph belongs to exactly one group.
    - For every pair of nodes in the graph that are connected by an edge [ai,
      bi], if ai belongs to the group with index x, and bi belongs to the group
      with index y, then |y - x| = 1.

    Return the maximum number of groups (i.e., maximum m) into which you can
    divide the nodes. Return -1 if it is impossible to group the nodes with the
    given conditions.
Link: https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/
Notes:
"""

import unittest
from collections import defaultdict, deque


class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def longest_path(i: int) -> tuple[dict[int, int] | None, int]:
            q = deque([(i, 1)])
            dist = {i: 1}

            while q:
                node, length = q.popleft()
                for nei in adj[node]:
                    if nei in dist:
                        if dist[nei] == length:
                            return None, -1
                        continue
                    q.append((nei, length + 1))
                    dist[nei] = length + 1
                    visit.add(nei)
            return dist, max(dist.values())

        visit = set()
        res = 0
        for i in range(1, n + 1):
            if i in visit:
                continue
            visit.add(i)
            component, length = longest_path(i)
            if length == -1 or component is None:
                return -1

            res += max(longest_path(src)[1] for src in component)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_magnificentSets1(self):
        n = 6
        e = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]
        expected = 4
        self.assertEqual(expected, self.sol.magnificentSets(n, e))

    def test_magnificentSets2(self):
        n = 3
        e = [[1, 2], [2, 3], [3, 1]]
        expected = -1
        self.assertEqual(expected, self.sol.magnificentSets(n, e))


if __name__ == '__main__':
    unittest.main()
