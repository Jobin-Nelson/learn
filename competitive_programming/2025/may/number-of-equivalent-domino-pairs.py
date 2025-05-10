"""
Created Date: 2025-05-04
Qn: Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j]
    = [c, d] if and only if either (a == c and b == d), or (a == d and b == c)
    - that is, one domino can be rotated to be equal to another domino.

    Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length,
    and dominoes[i] is equivalent to dominoes[j].
Link: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
Notes:
    - transform tuple into a single number
"""

import unittest


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        lookup = {}
        res = 0
        for d1, d2 in dominoes:
            val = d1 * 10 + d2 if d1 < d2 else d2 * 10 + d1
            res += lookup.get(val, 0)
            lookup[val] = lookup.get(val, 0) + 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_numEquivDominoPairs1(self):
        d = [[1,2],[2,1],[3,4],[5,6]]
        expected = 1
        self.assertEqual(expected, self.sol.numEquivDominoPairs(d))

    def test_numEquivDominoPairs2(self):
        d = [[1,2],[1,2],[1,1],[1,2],[2,2]]
        expected = 3
        self.assertEqual(expected, self.sol.numEquivDominoPairs(d))


if __name__ == '__main__':
    unittest.main()
