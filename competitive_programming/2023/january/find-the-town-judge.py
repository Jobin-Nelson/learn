'''
Created Date: 2023-01-23
Qn: In a town, there are n people labeled from 1 to n. There is a rumor that
    one of these people is secretly the town judge.

    If the town judge exists, then:

        - The town judge trusts nobody. 
        - Everybody (except for the town judge) trusts the town judge. 

    There is exactly one person that satisfies properties 1 and 2. You are
    given an array trust where trust[i] = [ai, bi] representing that the person
    labeled ai trusts the person labeled bi.

    Return the label of the town judge if the town judge exists and can be
    identified, or return -1 otherwise.
Link: https://leetcode.com/problems/find-the-town-judge/
Notes:
    - use list to store the count of trusts
    - decrement truster so that only the judge would have (n-1) persons
      trusting him
    - increment trustee
'''
def findJudge(n: int, trust: list[list[int]]) -> int:
    count = [0] * (n+1)

    for a, b in trust:
        count[a] -= 1
        count[b] += 1
    for i, val in enumerate(count):
        if val == n-1: return i
    return -1

if __name__ == '__main__':
    n1, t1 = 2, [[1,2]]
    n2, t2 = 3, [[1,3],[2,3]]
    n3, t3 = 3, [[1,3],[2,3],[3,1]]

    print(findJudge(n1, t1))
    print(findJudge(n2, t2))
    print(findJudge(n3, t3))
