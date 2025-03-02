"""
Created Date: 2025-02-24
Qn: There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at
    node 0. You are given a 2D integer array edges of length n - 1 where
    edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi
    in the tree.

    At every node i, there is a gate. You are also given an array of even
    integers amount, where amount[i] represents:

    - the price needed to open the gate at node i, if amount[i] is negative,
      or,
    - the cash reward obtained on opening the gate at node i, otherwise.

    The game goes on as follows:

    - Initially, Alice is at node 0 and Bob is at node bob.
    - At every second, Alice and Bob each move to an adjacent node. Alice moves
      towards some leaf node, while Bob moves towards node 0.
    - For every node along their path, Alice and Bob either spend money to open
      the gate at that node, or accept the reward. Note that:
        - If the gate is already open, no price will be required, nor will
          there be any cash reward.
        - If Alice and Bob reach the node simultaneously, they share the
          price/reward for opening the gate there. In other words, if the price
          to open the gate is c, then both Alice and Bob pay c / 2 each.
          Similarly, if the reward at the gate is c, both of them receive c / 2
          each.
    - If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches
      node 0, he stops moving. Note that these events are independent of each
      other.

    Return the maximum net income Alice can have if she travels towards the
    optimal leaf node.
Link: https://leetcode.com/problems/most-profitable-path-in-a-tree/
Notes:
    - use dfs for bob and bfs for alice
"""

import unittest
from collections import defaultdict, deque


class Solution:
    def mostProfitablePath(
        self, edges: list[list[int]], bob: int, amount: list[int]
    ) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Bob simulation
        bob_times = {}

        def dfs(src: int, prev: int, time: int) -> bool:
            if src == 0:
                bob_times[src] = time
                return True
            for nei in graph[src]:
                if nei == prev:
                    continue
                if dfs(nei, src, time + 1):
                    bob_times[src] = time
                    return True
            return False

        dfs(bob, -1, 0)

        # Alice simulation
        q = deque([(0, 0, -1, amount[0])])  # node, time, previous node, profit
        res = float('-inf')
        while q:
            node, time, prev, profit = q.popleft()
            for nei in graph[node]:
                if nei == prev:
                    continue
                nei_time = time + 1
                nei_profit = amount[nei]
                if nei in bob_times:
                    if nei_time > bob_times[nei]:
                        nei_profit = 0
                    elif nei_time == bob_times[nei]:
                        nei_profit //= 2
                if len(graph[nei]) == 1:
                    res = max(res, profit + nei_profit)
                q.append((nei, nei_time, node, profit + nei_profit))
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_mostProfitablePath1(self):
        e = [[0, 1], [1, 2], [1, 3], [3, 4]]
        b = 3
        a = [-2, 4, 2, -4, 6]
        expected = 6
        self.assertEqual(expected, self.sol.mostProfitablePath(e, b, a))

    def test_mostProfitablePath2(self):
        e = [[0, 1]]
        b = 1
        a = [-7280, 2350]
        expected = -7280
        self.assertEqual(expected, self.sol.mostProfitablePath(e, b, a))


if __name__ == '__main__':
    unittest.main()
