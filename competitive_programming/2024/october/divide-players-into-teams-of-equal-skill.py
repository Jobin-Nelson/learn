"""
Created Date: 2024-10-04
Qn: You are given a positive integer array skill of even length n where
    skill[i] denotes the skill of the ith player. Divide the players into n / 2
    teams of size 2 such that the total skill of each team is equal.

    The chemistry of a team is equal to the product of the skills of the
    players on that team.

    Return the sum of the chemistry of all the teams, or return -1 if there is
    no way to divide the players into teams such that the total skill of each
    team is equal.
Link: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
Notes:
    - use sorting
"""

def dividePlayers(skill: list[int]) -> int:
    n = len(skill)
    skill.sort()
    res = 0
    teamSkill = skill[0] + skill[-1]
    for i in range(n>>1):
        if skill[i] + skill[n-i-1] != teamSkill:
            return -1
        res += skill[i] * skill[n-i-1]
    return res


if __name__ == '__main__':
    s1 = [3, 2, 5, 1, 3, 4]
    s2 = [3, 4]
    s3 = [1, 1, 2, 3]

    print(dividePlayers(s1))
    print(dividePlayers(s2))
    print(dividePlayers(s3))
