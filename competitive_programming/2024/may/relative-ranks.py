"""
Created Date: 2024-05-08
Qn: You are given an integer array score of size n, where score[i] is the score
    of the ith athlete in a competition. All the scores are guaranteed to be
    unique.

    The athletes are placed based on their scores, where the 1st place athlete
    has the highest score, the 2nd place athlete has the 2nd highest score, and
    so on. The placement of each athlete determines their rank:

        - The 1st place athlete's rank is "Gold Medal". 
        - The 2nd place athlete's rank is "Silver Medal". 
        - The 3rd place athlete's rank is "Bronze Medal".
        - For the 4th place to the nth place athlete, their rank is their
          placement number (i.e., the xth place athlete's rank is "x").

    Return an array answer of size n where answer[i] is the rank of the ith
    athlete.
Link: https://leetcode.com/problems/relative-ranks/
Notes:
    - use hashtable
"""
def findRelativeRanks(score: list[int]) -> list[str]:
    lookup = {}
    for i, n in enumerate(sorted(score, reverse=True), start=1):
        if i == 1:
            i = 'Gold Medal'
        elif i == 2:
            i = 'Silver Medal'
        elif i == 3:
            i = 'Bronze Medal'
        lookup[n] = str(i)
    res = [lookup[n] for n in score]
    return res

if __name__ == '__main__':
    s1 = [5,4,3,2,1]
    s2 = [10,3,8,9,4]

    print(findRelativeRanks(s1))
    print(findRelativeRanks(s2))
