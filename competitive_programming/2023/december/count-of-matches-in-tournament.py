"""
Created Date: 2023-12-05
Qn: You are given an integer n, the number of teams in a tournament that has
    strange rules:

        - If the current number of teams is even, each team gets paired with
          another team. A total of n / 2 matches are played, and n / 2 teams
          advance to the next round. 
        - If the current number of teams is odd, one team randomly advances in
          the tournament, and the rest gets paired. A total of (n - 1) /
          2 matches are played, and (n - 1) / 2 + 1 teams advance to the next
          round.

    Return the number of matches played in the tournament until a winner is
    decided.
Link: https://leetcode.com/problems/count-of-matches-in-tournament/
Notes:
    - there is n teams and n-1 teams will be eliminated.
    - n-1 matches will be played to eliminate n-1 teams
    - hence the number of matches is n-1
"""
def numberOfMatches(n: int) -> int:
    return n - 1
    # res = 0
    # while n != 1:
    #     if n & 1:
    #         n = ((n-1) >> 1) + 1
    #         res -= 1
    #     else:
    #         n >>= 1
    #     res += n
    # return res

if __name__ == '__main__':
    n1 = 7
    n2 = 14

    print(numberOfMatches(n1))
    print(numberOfMatches(n2))
