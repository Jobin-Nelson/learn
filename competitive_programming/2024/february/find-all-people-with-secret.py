"""
Created Date: 2024-02-24
Qn: You are given an integer n indicating there are n people numbered from 0 to
    n - 1. You are also given a 0-indexed 2D integer array meetings where
    meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a
    meeting at timei. A person may attend multiple meetings at the same time.
    Finally, you are given an integer firstPerson.

    Person 0 has a secret and initially shares the secret with a person
    firstPerson at time 0. This secret is then shared every time a meeting
    takes place with a person that has the secret. More formally, for every
    meeting, if a person xi has the secret at timei, then they will share the
    secret with person yi, and vice versa.

    The secrets are shared instantaneously. That is, a person may receive the
    secret and share it with people in other meetings within the same time
    frame.

    Return a list of all the people that have the secret after all the meetings
    have taken place. You may return the answer in any order.
Link: https://leetcode.com/problems/find-all-people-with-secret/
Notes:
    - build a graph from time
"""
from collections import defaultdict

def findAllPeople(n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
    secrets = set([0, firstPerson])
    time_map = {}
    for src, dst, t in meetings:
        if t not in time_map:
            time_map[t] = defaultdict(list)
        time_map[t][src].append(dst)
        time_map[t][dst].append(src)

    def dfs(src: int, adj: dict[int, list[int]]):
        if src in visit: return
        visit.add(src)
        secrets.add(src)
        for nei in adj[src]:
            dfs(nei, adj)
    
    for t in sorted(time_map.keys()):
        visit = set()
        for src in time_map[t]:
            if src in secrets:
                dfs(src, time_map[t])
    return list(secrets)

if __name__ == '__main__':
    n1, m1, f1 = 6, [[1,2,5],[2,3,8],[1,5,10]], 1
    n2, m2, f2 = 4, [[3,1,3],[1,2,2],[0,3,3]], 3
    n3, m3, f3 = 5, [[3,4,2],[1,2,1],[2,3,1]], 1
    n4, m4, f4 = 5, [[1,4,3],[0,4,3]], 3

    print(findAllPeople(n1, m1, f1))
    print(findAllPeople(n2, m2, f2))
    print(findAllPeople(n3, m3, f3))
    print(findAllPeople(n4, m4, f4))


