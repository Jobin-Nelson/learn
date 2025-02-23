"""
Created Date: 2025-02-16
Qn: Given an integer n, find a sequence that satisfies all of the following:

    - The integer 1 occurs once in the sequence.
    - Each integer between 2 and n occurs twice in the sequence.
    - For every integer i between 2 and n, the distance between the two
      occurrences of i is exactly i.

    The distance between two numbers on the sequence, a[i] and a[j], is the
    absolute difference of their indices, |j - i|.

    Return the lexicographically largest sequence. It is guaranteed that under
    the given constraints, there is always a solution.

    A sequence a is lexicographically larger than a sequence b (of the same
    length) if in the first position where a and b differ, sequence a has a
    number greater than the corresponding number in b. For example, [0,1,9,0]
    is lexicographically larger than [0,1,5,6] because the first position they
    differ is at the third number, and 9 is greater than 5.
Link: https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/
Notes:
    - use backtracking
"""

import unittest


class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        res = [0] * (2 * n - 1)
        used = set()

        def backtrack(i: int) -> bool:
            if i == len(res):
                return True
            for num in range(n, 0, -1):
                if num in used or (num > 1 and (i + num >= len(res) or res[i + num])):
                    continue

                used.add(num)
                res[i] = num
                if num > 1:
                    res[i + num] = num

                j = i + 1
                while j < len(res) and res[j]:
                    j += 1

                if backtrack(j):
                    return True

                used.remove(num)
                res[i] = 0
                if num > 1:
                    res[i + num] = 0
            return False

        backtrack(0)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_constructDistancedSequence1(self):
        n = 3
        expected = [3, 1, 2, 3, 2]
        self.assertEqual(expected, self.sol.constructDistancedSequence(n))

    def test_constructDistancedSequence2(self):
        n = 5
        expected = [5, 3, 1, 4, 3, 5, 2, 4, 2]
        self.assertEqual(expected, self.sol.constructDistancedSequence(n))


if __name__ == '__main__':
    unittest.main()
