"""
Created Date: 2025-05-01
Qn: You have n tasks and m workers. Each task has a strength requirement stored
    in a 0-indexed integer array tasks, with the ith task requiring tasks[i]
    strength to complete. The strength of each worker is stored in a 0-indexed
    integer array workers, with the jth worker having workers[j] strength. Each
    worker can only be assigned to a single task and must have a strength
    greater than or equal to the task's strength requirement (i.e., workers[j]
    >= tasks[i]).

    Additionally, you have pills magical pills that will increase a worker's
    strength by strength. You can decide which workers receive the magical
    pills, however, you may only give each worker at most one magical pill.

    Given the 0-indexed integer arrays tasks and workers and the integers pills
    and strength, return the maximum number of tasks that can be completed.
Link: https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/
Notes:
    - use binary search and deque
"""

import unittest
from collections import deque


class Solution:
    def maxTaskAssign(
        self, tasks: list[int], workers: list[int], pills: int, strength: int
    ) -> int:
        tasks.sort()
        workers.sort()
        worker_len, task_len = len(workers), len(tasks)

        def check(mid: int) -> bool:
            p = pills
            ws = deque()
            ptr = worker_len - 1

            for i in range(mid - 1, -1, -1):
                while ptr >= worker_len - mid and workers[ptr] + strength >= tasks[i]:
                    ws.appendleft(workers[ptr])
                    ptr -= 1
                if not ws:
                    return False
                elif ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    p -= 1
                    ws.popleft()
            return True

        l, r, res = 1, min(worker_len, task_len), 0
        while l <= r:
            m = (r + (r-l)) >> 1
            if check(m):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxTaskAssign1(self):
        t, w, p, s = [3, 2, 1], [0, 3, 3], 1, 1
        expected = 3
        self.assertEqual(expected, self.sol.maxTaskAssign(t, w, p, s))

    def test_maxTaskAssign2(self):
        t, w, p, s = [3, 2, 1], [0, 3, 3], 1, 1
        expected = 3
        self.assertEqual(expected, self.sol.maxTaskAssign(t, w, p, s))


if __name__ == '__main__':
    unittest.main()
