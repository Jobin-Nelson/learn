"""
Created Date: 2024-11-07
Qn: The bitwise AND of an array nums is the bitwise AND of all integers in
    nums.

    - For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3
      = 1.
    - Also, for nums = [7], the bitwise AND is 7.

    You are given an array of positive integers candidates. Evaluate the
    bitwise AND of every combination of numbers of candidates. Each number in
    candidates may only be used once in each combination.

    Return the size of the largest combination of candidates with a bitwise AND
    greater than 0.
Link: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
Notes:
    - count each bit and return max
"""

import unittest


class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        # functional approach
        def get_count(i: int) -> int:
            return sum(1 for n in candidates if (1<<i) & n)

        counts = map(get_count, range(32))
        return max(counts, default=0)

        # res = 0
        # for i in range(32):
        #     count = 0
        #     for n in candidates:
        #         if (1 << i) & n:
        #             count += 1
        #     res = max(res, count)
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_largestCombination1(self):
        c = [16, 17, 71, 62, 12, 24, 14]
        self.assertEqual(self.sol.largestCombination(c), 4)

    def test_largestCombination2(self):
        c = [8, 8]
        self.assertEqual(self.sol.largestCombination(c), 2)


if __name__ == '__main__':
    unittest.main()
