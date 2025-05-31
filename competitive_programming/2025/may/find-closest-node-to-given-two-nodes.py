"""
Created Date: 2025-05-30
Qn: You are given a directed graph of n nodes numbered from 0 to n - 1, where
    each node has at most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size n,
    indicating that there is a directed edge from node i to node edges[i]. If
    there is no outgoing edge from i, then edges[i] == -1.

    You are also given two integers node1 and node2.

    Return the index of the node that can be reached from both node1 and node2,
    such that the maximum between the distance from node1 to that node, and
    from node2 to that node is minimized. If there are multiple answers, return
    the node with the smallest index, and if no possible answer exists, return
    -1.

    Note that edges may contain cycles.
Link: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
Notes:
"""

import unittest
from collections import deque
from sys import maxsize


class Solution:
    def closestMeetingNodes(self, edges: list[int], node1: int, node2: int) -> int:
        n = len(edges)

        def bfs(start_node: int) -> list[int]:
            q = deque([start_node])
            visited = [False] * n
            dist = [maxsize] * n
            dist[start_node] = 0
            while q:
                node = q.popleft()
                if visited[node]:
                    continue
                visited[node] = True
                nei = edges[node]
                if nei != -1 and not visited[nei]:
                    dist[nei] = 1 + dist[node]
                    q.append(nei)
            return dist

        dist1 = bfs(node1)
        dist2 = bfs(node2)

        min_dist_node = -1
        min_dist_till_now = maxsize
        for cur_node in range(n):
            if min_dist_till_now > max(dist1[cur_node], dist2[cur_node]):
                min_dist_node = cur_node
                min_dist_till_now = max(dist1[cur_node], dist2[cur_node])
        return min_dist_node


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_closestMeetingNodes1(self):
        e = [2, 2, 3, -1]
        n1 = 0
        n2 = 1
        expected = 2
        self.assertEqual(expected, self.sol.closestMeetingNodes(e, n1, n2))

    def test_closestMeetingNodes2(self):
        e = [1, 2, -1]
        n1 = 0
        n2 = 2
        expected = 2
        self.assertEqual(expected, self.sol.closestMeetingNodes(e, n1, n2))

    def test_closestMeetingNodes3(self):
        e = [5, 4, 5, 4, 3, 6, -1]
        n1 = 0
        n2 = 1
        expected = -1
        self.assertEqual(expected, self.sol.closestMeetingNodes(e, n1, n2))


if __name__ == '__main__':
    unittest.main()
