'''
Created Date: 2023-07-28
Qn: You are given an integer array nums. Two players are playing a game with
    this array: player 1 and player 2.

    Player 1 and player 2 take turns, with player 1 starting first. Both
    players start the game with a score of 0. At each turn, the player takes
    one of the numbers from either end of the array (i.e., nums[0] or
    nums[nums.length - 1]) which reduces the size of the array by 1. The player
    adds the chosen number to their score. The game ends when there are no more
    elements in the array.

    Return true if Player 1 can win the game. If the scores of both players are
    equal, then player 1 is still the winner, and you should also return true.
    You may assume that both players are playing optimally.
Link: https://leetcode.com/problems/predict-the-winner/
Notes:
    - use dfs
'''
from collections import defaultdict

def PredictTheWinner(nums: list[int]) -> bool:
    N = len(nums)
    memo = defaultdict(int)
    def maxDiff(left: int, right: int) -> int:
        if left == right: return nums[left]
        left_score = nums[left] - maxDiff(left + 1, right)
        right_score = nums[right] - maxDiff(left, right - 1)
        memo[(left, right)] = max(left_score, right_score)
        return memo[(left, right)]
    return maxDiff(0, N -1) >= 0

if __name__ == '__main__':
    n1 = [1,5,2]
    n2 = [1,5,233,7]

    print(PredictTheWinner(n1))
    print(PredictTheWinner(n2))
