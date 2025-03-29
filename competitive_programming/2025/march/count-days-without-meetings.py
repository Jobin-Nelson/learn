"""
Created Date: 2025-03-24
Qn: You are given a positive integer days representing the total number of days
    an employee is available for work (starting from day 1). You are also given
    a 2D array meetings of size n where, meetings[i] = [start_i, end_i]
    represents the starting and ending days of meeting i (inclusive).

    Return the count of days when the employee is available for work but no
    meetings are scheduled.

    Note: The meetings may overlap.
Link: https://leetcode.com/problems/count-days-without-meetings/
Notes:
    - count the free days after sorting meetings
"""

from functools import reduce
import unittest


class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        # Functional approach
        def count(x: tuple[int, int], y: list[int]) -> tuple[int, int]:
            free_days, latest_end = x
            s, e = y
            return (
                free_days + s - latest_end - 1 if s > latest_end else free_days,
                max(latest_end, e),
            )

        free_days, latest_end = reduce(count, sorted(meetings), (0, 0))
        return free_days + (days - latest_end)

        # Imperative approach
        # free_days = 0
        # latest_end = 0
        # for s, e in sorted(meetings):
        #     if s > latest_end:
        #         free_days += s - latest_end - 1
        #     latest_end = max(latest_end, e)
        # free_days += days - latest_end
        # return free_days


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countDays1(self):
        d = 10
        m = [[5, 7], [1, 3], [9, 10]]
        expected = 2
        self.assertEqual(expected, self.sol.countDays(d, m))

    def test_countDays2(self):
        d = 5
        m = [[2, 4], [1, 3]]
        expected = 1
        self.assertEqual(expected, self.sol.countDays(d, m))

    def test_countDays3(self):
        d = 6
        m = [[1, 6]]
        expected = 0
        self.assertEqual(expected, self.sol.countDays(d, m))


if __name__ == '__main__':
    unittest.main()
