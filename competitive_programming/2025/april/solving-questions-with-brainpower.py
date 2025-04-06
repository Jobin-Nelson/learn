"""
Created Date: 2025-04-01
Qn: You are given a 0-indexed 2D integer array questions where questions[i] =
    [pointsi, brainpoweri].

    The array describes the questions of an exam, where you have to process the
    questions in order (i.e., starting from question 0) and make a decision
    whether to solve or skip each question. Solving question i will earn you
    pointsi points but you will be unable to solve each of the next brainpoweri
    questions. If you skip question i, you get to make the decision on the next
    question.

    - For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
        - If question 0 is solved, you will earn 3 points but you will be
          unable to solve questions 1 and 2.
        - If instead, question 0 is skipped and question 1 is solved, you will
          earn
          4 points but you will be unable to solve questions 2 and 3.

    Return the maximum points you can earn for the exam.
Link: https://leetcode.com/problems/solving-questions-with-brainpower/
Notes:
"""

import unittest


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        # Tabulation (DP)
        dp = [0] * (len(questions) + 1)
        N = len(dp)
        for i in range(len(questions) - 1, -1, -1):
            points, brainpower = questions[i]
            dp[i] = max(points + dp[min(N - 1, i + brainpower + 1)], dp[i + 1])
        return dp[0]

        # DFS
        # def dfs(i: int) -> int:
        #     if i >= len(questions):
        #         return 0
        #     return max(questions[i][0] + dfs(i + questions[i][1] + 1), dfs(i + 1))
        #
        # return dfs(0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_mostPoints1(self):
        q = [[3, 2], [4, 3], [4, 4], [2, 5]]
        expected = 5
        self.assertEqual(expected, self.sol.mostPoints(q))

    def test_mostPoints2(self):
        q = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        expected = 7
        self.assertEqual(expected, self.sol.mostPoints(q))


if __name__ == '__main__':
    unittest.main()
