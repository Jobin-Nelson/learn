"""
Created Date: 2024-02-22
Qn: In a town, there are n people labeled from 1 to n. There is a rumor that
    one of these people is secretly the town judge.

    If the town judge exists, then:

        - The town judge trusts nobody. 
        - Everybody (except for the town judge) trusts the town judge. 
        - There is exactly one person that satisfies properties 1 and 2.

    You are given an array trust where trust[i] = [ai, bi] representing that the
    person labeled ai trusts the person labeled bi. If a trust relationship does
    not exist in trust array, then such a trust relationship does not exist.

    Return the label of the town judge if the town judge exists and can be
    identified, or return -1 otherwise.
Link: https://leetcode.com/problems/find-the-town-judge/
Notes:
    - use hashmap
    - count incoming and outgoing
"""
from collections import Counter

def findJudge(n: int, trust: list[list[int]]) -> int:
    delta = Counter()

    for src, dst in trust:
        delta[src] -= 1
        delta[dst] += 1

    for i in range(1, n+1):
        if delta[i] == n-1:
            return i
    return -1

if __name__ == '__main__':
    n1, t1 = 2, [[1, 2]]
    n2, t2 = 3, [[1,3],[2,3]]
    n3, t3 = 3, [[1,3],[2,3],[3,1]]

    print(findJudge(n1, t1))
    print(findJudge(n2, t2))
    print(findJudge(n3, t3))
