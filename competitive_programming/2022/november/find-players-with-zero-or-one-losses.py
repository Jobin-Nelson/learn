'''
Created Date: 2022-11-28
Qn: You are given an integer array matches where 
    matches[i] = [winneri, loseri] indicates that the player winneri defeated
    player loseri in a match.

    Return a list answer of size 2 where:
        - answer[0] is a list of all players that have not lost any matches.
        - answer[1] is a list of all players that have lost exactly one
          match.

    The values in the two lists should be returned in increasing order.

    Note:
        - You should only consider the players that have played at least one
          match. 
        - The testcases will be generated such that no two matches will have
          the same outcome.
Link: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
Notes:
    - use hashmap
'''
def findWinners(matches: list[list[int]]) -> list[list[int]]:
    winners, losers = dict(), dict()

    for winner, loser in matches:
        if winner not in winners:
            winners[winner] = 1
        else:
            winners[winner] += 1

        if loser not in losers:
            losers[loser] = 1
        else:
            losers[loser] += 1
    res0 = [w for w in winners if w not in losers]
    res1 = [l for l, v in losers.items() if v == 1]

    return [sorted(res0), sorted(res1)]

if __name__ == '__main__':
    m1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    m2 = [[2,3],[1,3],[5,4],[6,4]]
    
    print(findWinners(m1))
    print(findWinners(m2))
