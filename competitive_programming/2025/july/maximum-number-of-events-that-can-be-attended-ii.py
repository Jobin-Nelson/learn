"""
Created Date: 2025-07-08
Qn: You are given an array of events where events[i] = [startDayi, endDayi,
    valuei]. The ith event starts at startDayi and ends at endDayi, and if you
    attend this event, you will receive a value of valuei. You are also given
    an integer k which represents the maximum number of events you can attend.

    You can only attend one event at a time. If you choose to attend an event,
    you must attend the entire event. Note that the end day is inclusive: that
    is, you cannot attend two events where one of them starts and the other
    ends on the same day.

    Return the maximum sum of values that you can receive by attending events.
Link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
Notes:
"""

import bisect
import unittest


class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        n = len(events)
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        events.sort()
        start_events = [start for start, _, _ in events]

        for cur_index in range(n - 1, -1, -1):
            next_index = bisect.bisect_right(start_events, events[cur_index][1])
            for i in range(1, k + 1):
                dp[i][cur_index] = max(
                    dp[i][cur_index + 1], events[cur_index][2] + dp[i - 1][next_index]
                )
        return dp[k][0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxValue1(self):
        e = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
        k = 2
        expected = 7
        self.assertEqual(expected, self.sol.maxValue(e, k))

    def test_maxValue2(self):
        e = [[1, 2, 4], [3, 4, 3], [2, 3, 10]]
        k = 2
        expected = 10
        self.assertEqual(expected, self.sol.maxValue(e, k))

    def test_maxValue3(self):
        e = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
        k = 3
        expected = 9
        self.assertEqual(expected, self.sol.maxValue(e, k))


if __name__ == '__main__':
    unittest.main()
