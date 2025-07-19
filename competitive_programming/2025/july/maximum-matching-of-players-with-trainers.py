"""
Created Date: 2025-07-13
Qn: You are given a 0-indexed integer array players, where players[i]
    represents the ability of the ith player. You are also given a 0-indexed
    integer array trainers, where trainers[j] represents the training capacity
    of the jth trainer.

    The ith player can match with the jth trainer if the player's ability is
    less than or equal to the trainer's training capacity. Additionally, the
    ith player can be matched with at most one trainer, and the jth trainer can
    be matched with at most one player.

    Return the maximum number of matchings between players and trainers that
    satisfy these conditions.
Link: https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
Notes:
    - sort both players and trainers to start matching optimally
"""

import unittest


class Solution:
    def matchPlayer(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        tn = len(trainers)
        res, ti = 0, 0
        for p in players:
            while ti < tn and p > trainers[ti]:
                ti += 1
            if ti == tn:
                break
            res += 1
            ti += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_matchPlayer1(self):
        p, t = [4, 7, 9], [8, 2, 5, 8]
        expected = 2
        self.assertEqual(expected, self.sol.matchPlayer(p, t))

    def test_matchPlayer2(self):
        p, t = [1, 1, 1], [10]
        expected = 1
        self.assertEqual(expected, self.sol.matchPlayer(p, t))


if __name__ == '__main__':
    unittest.main()
