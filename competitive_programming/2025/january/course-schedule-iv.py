"""
Created Date: 2025-01-27
Qn: There are a total of numCourses courses you have to take, labeled from 0 to
    numCourses - 1. You are given an array prerequisites where prerequisites[i]
    = [ai, bi] indicates that you must take course ai first if you want to take
    course bi.

    For example, the pair [0, 1] indicates that you have to take course 0
    before you can take course 1. Prerequisites can also be indirect. If course
    a is a prerequisite of course b, and course b is a prerequisite of course
    c, then course a is a prerequisite of course c.

    You are also given an array queries where queries[j] = [uj, vj]. For the
    jth query, you should answer whether course uj is a prerequisite of course
    vj or not.

    Return a boolean array answer, where answer[j] is the answer to the jth
    query.
Link: https://leetcode.com/problems/course-schedule-iv/
Notes:
    - use dfs and cache the results
"""

from collections import defaultdict
import unittest


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        prereqMap = {}

        def dfs(crs: int) -> set[int]:
            if crs in prereqMap:
                return prereqMap[crs]
            prereqMap[crs] = {crs}
            for prereq in adj[crs]:
                prereqMap[crs] |= dfs(prereq)
            return prereqMap[crs]

        for crs in range(numCourses):
            dfs(crs)

        return [u in prereqMap[v] for u, v in queries]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_checkIfPrerequisite1(self):
        n = 2
        p = [[1, 0]]
        q = [[0, 1], [1, 0]]
        expected = [False, True]
        self.assertEqual(expected, self.sol.checkIfPrerequisite(n, p, q))

    def test_checkIfPrerequisite2(self):
        n = 2
        p = []
        q = [[1, 0], [0, 1]]
        expected = [False, False]
        self.assertEqual(expected, self.sol.checkIfPrerequisite(n, p, q))

    def test_checkIfPrerequisite3(self):
        n = 3
        p = [[1, 2], [1, 0], [2, 0]]
        q = [[1, 0], [1, 2]]
        expected = [True, True]
        self.assertEqual(expected, self.sol.checkIfPrerequisite(n, p, q))


if __name__ == '__main__':
    unittest.main()
