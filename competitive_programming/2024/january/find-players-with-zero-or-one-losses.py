"""
Created Date: 2024-01-15
Qn: You are given an integer array matches where matches[i] = [winneri, loseri]
    indicates that the player winneri defeated player loseri in a match.

    Return a list answer of size 2 where:

        - answer[0] is a list of all players that have not lost any matches.
        - answer[1] is a list of all players that have lost exactly one match.

    The values in the two lists should be returned in increasing order.

    Note:

        - You should only consider the players that have played at least one
          match. 
        - The testcases will be generated such that no two matches will have
          the same outcome.

Link: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
Notes:
     - use either hashset or hashmap
"""
def findWinners(matches: list[list[int]]) -> list[list[int]]:
    tp, tl, ol = set(), set(), set()

    for w, l in matches:
        tp.add(w)
        if l in ol:
            ol.remove(l)
        elif l not in tl:
            ol.add(l)
        tl.add(l)
        tp.add(l)
    return [sorted(tp - tl), sorted(ol)]

    # ld = defaultdict(int)
    #
    # for w, l in matches:
    #     ld[l] += 1
    #     ld[w] += 0
    #
    # res = [[], []]
    # for k, v in ld.items():
    #     if v <= 1:
    #         res[v].append(k)
    # res[0].sort()
    # res[1].sort()
    # return res

if __name__ == '__main__':
    m1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    m2 = [[2,3],[1,3],[5,4],[6,4]]

    print(findWinners(m1))
    print(findWinners(m2))
