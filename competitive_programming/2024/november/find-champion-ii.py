"""
Created Date: 2024-11-26
Qn: There are n teams numbered from 0 to n - 1 in a tournament; each team is
    also a node in a DAG.

    You are given the integer n and a 0-indexed 2D integer array edges of
    length m representing the DAG, where edges[i] = [ui, vi] indicates that
    there is a directed edge from team ui to team vi in the graph.

    A directed edge from a to b in the graph means that team a is stronger than
    team b and team b is weaker than team a.

    Team a will be the champion of the tournament if there is no team b that is
    stronger than team a.

    Return the team that will be the champion of the tournament if there is a
    unique champion, otherwise, return -1.

    Notes

        - A cycle is a series of nodes a1, a2, ..., an, an+1 such that node a1
          is the same node as node an+1, the nodes a1, a2, ..., an are
          distinct, and there is a directed edge from the node ai to node ai+1
          for every i in the range [1, n].
        - A DAG is a directed graph that does not have any cycle.
Link: https://leetcode.com/problems/find-champion-ii/
Notes:
    - count incoming edges and return the node which doesn't have any incoming
      edges
"""

import unittest

class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        incoming = [0] * n
        for _, dst in edges:
            incoming[dst] += 1
        champion = [i for i, incoming_count in enumerate(incoming) if incoming_count == 0]
        return champion[0] if len(champion) == 1 else -1



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findChampion1(self):
        n, e = 3, [[0,1], [1,2]]
        self.assertEqual(self.sol.findChampion(n, e), 0)
    def test_findChampion2(self):
        n, e = 4, [[0,2],[1,3],[1,2]]
        self.assertEqual(self.sol.findChampion(n, e), -1)


if __name__ == '__main__':
    unittest.main()
