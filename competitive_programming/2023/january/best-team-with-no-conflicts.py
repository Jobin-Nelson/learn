'''
Created Date: 2023-01-31
Qn: You are the manager of a basketball team. For the upcoming tournament, you
    want to choose the team with the highest overall score. The score of the
    team is the sum of scores of all the players in the team.

    However, the basketball team is not allowed to have conflicts. A conflict
    exists if a younger player has a strictly higher score than an older
    player. A conflict does not occur between players of the same age.

    Given two lists, scores and ages, where each scores[i] and ages[i]
    represents the score and age of the ith player, respectively, return the
    highest overall score of all possible basketball teams.
Link: https://leetcode.com/problems/best-team-with-no-conflicts/
Notes:
    - use dp
    - sorted and zip score_ages
'''
def bestTeamScore(scores: list[int], ages: list[int]) -> int:
    dp = [0] * (1 + max(ages))
    score_ages = sorted(zip(scores, ages))

    for score, age in score_ages:
        dp[age] = score + max(dp[:age+1])
    return max(dp)

if __name__ == '__main__':
    s1, a1 = [1,3,5,10,15], [1,2,3,4,5]
    s2, a2 = [4,5,6,5], [2,1,2,1]
    s3, a3 = [1,2,3,5], [8,9,10,1]

    print(bestTeamScore(s1, a1))
    print(bestTeamScore(s2, a2))
    print(bestTeamScore(s3, a3))
