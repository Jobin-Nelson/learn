"""
Created Date: 2025-07-07
Qn: You are given an array of events where events[i] = [startDayi, endDayi].
    Every event i starts at startDayi and ends at endDayi.

    You can attend an event i at any day d where startTimei <= d <= endTimei.
    You can only attend one event at any time d.

    Return the maximum number of events you can attend.
Link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
Notes:
    - use min heap to store all end days of events that have started
    - greedily pick the events with earlier end days
"""

import heapq
import unittest


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        q = []
        events.sort()

        j, res = 0, 0
        for i in range(1, max_day+1):
            while j < n and events[j][0] <= i:
                heapq.heappush(q, events[j][1])
                j += 1
            while q and q[0] < i:
                heapq.heappop(q)
            if q:
                heapq.heappop(q)
                res += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxEvents1(self):
        e = [[1, 2], [2, 3], [3, 4]]
        expected = 3
        self.assertEqual(expected, self.sol.maxEvents(e))

    def test_maxEvents2(self):
        e = [[1, 2], [2, 3], [3, 4], [1, 2]]
        expected = 4
        self.assertEqual(expected, self.sol.maxEvents(e))

    def test_maxEvents3(self):
        e = [[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]
        expected = 5
        self.assertEqual(expected, self.sol.maxEvents(e))


if __name__ == '__main__':
    unittest.main()
