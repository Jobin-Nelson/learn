"""
Created Date: 2024-12-15
Qn: There is a school that has classes of students and each class will be
    having a final exam. You are given a 2D integer array classes, where
    classes[i] = [passi, totali]. You know beforehand that in the ith class,
    there are totali total students, but only passi number of students will
    pass the exam.

    You are also given an integer extraStudents. There are another
    extraStudents brilliant students that are guaranteed to pass the exam of
    any class they are assigned to. You want to assign each of the
    extraStudents students to a class in a way that maximizes the average pass
    ratio across all the classes.

    The pass ratio of a class is equal to the number of students of the class
    that will pass the exam divided by the total number of students of the
    class. The average pass ratio is the sum of pass ratios of all the classes
    divided by the number of the classes.

    Return the maximum possible average pass ratio after assigning the
    extraStudents students. Answers within 10-5 of the actual answer will be
    accepted.
Link: https://leetcode.com/problems/maximum-average-pass-ratio/
Notes:
    - use heap
"""

import unittest
import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        def calculate_gain(passes: int, total_students: int) -> float:
            return (passes + 1) / (total_students + 1) - passes / total_students

        heap = [
            (-calculate_gain(passes, total_students), passes, total_students)
            for passes, total_students in classes
        ]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            _, passes, total_students = heapq.heappop(heap)
            heapq.heappush(
                heap,
                (
                    -calculate_gain(passes + 1, total_students + 1),
                    passes + 1,
                    total_students + 1,
                ),
            )

        return sum(passes / total_students for _, passes, total_students in heap) / len(
            classes
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxAverageRatio1(self):
        c = [[1, 2], [3, 5], [2, 2]]
        e = 2
        expected = 0.78333
        self.assertAlmostEqual(expected, self.sol.maxAverageRatio(c, e), places=5)

    def test_maxAverageRatio2(self):
        c = [[2, 4], [3, 9], [4, 5], [2, 10]]
        e = 4
        expected = 0.53485
        self.assertAlmostEqual(expected, self.sol.maxAverageRatio(c, e), places=5)


if __name__ == '__main__':
    unittest.main()
