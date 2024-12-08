"""
Created Date: 2024-12-08
Qn: You are given a 0-indexed 2D integer array of events where events[i] =
    [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends
    at endTimei, and if you attend this event, you will receive a value of
    valuei. You can choose at most two non-overlapping events to attend such
    that the sum of their values is maximized.

    Return this maximum sum.

    Note that the start time and end time is inclusive: that is, you cannot
    attend two events where one of them starts and the other ends at the same
    time. More specifically, if you attend an event with end time t, the next
    event must start at or after t + 1.
Link: https://leetcode.com/problems/two-best-non-overlapping-events/
Notes:
    - split into both (start, 1, value), (end+1, 0, value)
    - sort so that end time appears first, +1 is to ensure we don't have
      an overlapping
"""

import unittest
from itertools import chain
from functools import reduce


class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        # Functional approach
        def split_start_end(time: list[int]) -> list[tuple[int, int, int]]:
            return [(time[0], 1, time[2]), (time[1] + 1, 0, time[2])]

        times = sorted(chain.from_iterable(map(split_start_end, events)))

        def max_from_times(
            acc: tuple[int, int], time: tuple[int, int, int]
        ) -> tuple[int, int]:
            _, is_start, value = time
            max_val, res = acc
            return (
                (max_val, max(res, value + max_val))
                if is_start
                else (max(max_val, value), res)
            )

        return reduce(max_from_times, times, (0, 0))[1]

        # Imperative approach
        # times = []
        # for start, end, value in events:
        #     times.append((start, 1, value))
        #     times.append((end + 1, 0, value))
        # times.sort()
        # max_val, res = 0, 0
        # for _, is_start, value in times:
        #     if is_start:
        #         res = max(res, value + max_val)
        #     else:
        #         max_val = max(max_val, value)
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxTwoEvents1(self):
        events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
        expected = 4
        self.assertEqual(expected, self.sol.maxTwoEvents(events))

    def test_maxTwoEvents2(self):
        events = [[1, 3, 2], [4, 5, 2], [1, 5, 5]]
        expected = 5
        self.assertEqual(expected, self.sol.maxTwoEvents(events))

    def test_maxTwoEvents3(self):
        events = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]
        expected = 8
        self.assertEqual(expected, self.sol.maxTwoEvents(events))


if __name__ == '__main__':
    unittest.main()
