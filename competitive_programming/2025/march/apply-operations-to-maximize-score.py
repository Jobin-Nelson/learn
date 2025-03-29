"""
Created Date: 2025-03-29
Qn: You are given an array nums of n positive integers and an integer k.

    Initially, you start with a score of 1. You have to maximize your score by
    applying the following operation at most k times:

    - Choose any non-empty subarray nums[l, ..., r] that you haven't chosen
      previously.
    - Choose an element x of nums[l, ..., r] with the highest prime score. If
      multiple such elements exist, choose the one with the smallest index.
    - Multiply your score by x.

    Here, nums[l, ..., r] denotes the subarray of nums starting at index l and
    ending at the index r, both ends being inclusive.

    The prime score of an integer x is equal to the number of distinct prime
    factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 *
    3 *
    5 * 5.

    Return the maximum possible score after applying at most k operations.

    Since the answer may be large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/apply-operations-to-maximize-score/
Notes:
    - use heap and monotonic stack
"""

import unittest
import heapq
import math


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        N = len(nums)

        # Find prime scores
        primes_scores = []
        for n in nums:
            score = 0
            for f in range(2, int(math.sqrt(n) + 1)):
                if n % f == 0:
                    score += 1
                    while n % f == 0:
                        n //= f
            if n >= 2:
                score += 1
            primes_scores.append(score)

        # Find left and right bounds for each score
        left = [-1] * N
        right = [N] * N
        stack = []
        for i, s in enumerate(primes_scores):
            while stack and primes_scores[stack[-1]] < s:
                index = stack.pop()
                right[index] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # Calculate the res from left and right bounds
        h = [(-n, i) for i, n in enumerate(nums)]
        heapq.heapify(h)
        res = 1
        while k > 0:
            n, i = heapq.heappop(h)
            n = -n
            nl = i - left[i]
            nr = right[i] - i
            count = nl * nr
            operations = min(k, count)
            res = (res * pow(n, operations, MOD)) % MOD
            k -= operations
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumScore1(self):
        n = [8, 3, 9, 3, 8]
        k = 2
        expected = 81
        self.assertEqual(expected, self.sol.maximumScore(n, k))

    def test_maximumScore2(self):
        n = [19, 12, 14, 6, 10, 18]
        k = 3
        expected = 4788
        self.assertEqual(expected, self.sol.maximumScore(n, k))


if __name__ == '__main__':
    unittest.main()
