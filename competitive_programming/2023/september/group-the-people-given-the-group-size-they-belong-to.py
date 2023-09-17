'''
Created Date: 2023-09-11
Qn: There are n people that are split into some unknown number of groups. Each
    person is labeled with a unique ID from 0 to n - 1.

    You are given an integer array groupSizes, where groupSizes[i] is the size
    of the group that person i is in. For example, if groupSizes[1] = 3, then
    person 1 must be in a group of size 3.

    Return a list of groups such that each person i is in a group of size
    groupSizes[i].

    Each person should appear in exactly one group, and every person must be in
    a group. If there are multiple answers, return any of them. It is
    guaranteed that there will be at least one valid solution for the given
    input.
Link: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
Notes:
    - use hashmap
'''
from collections import defaultdict

def groupThePeople(groupSizes: list[int]) -> list[list[int]]:
    res, group_map = [], defaultdict(list)

    for i, g in enumerate(groupSizes):
        group_value = group_map[g]
        group_value.append(i)
        group_map[g] = group_value
        if len(group_value) == g:
            res.append(group_value)
            del group_map[g]
    return res

if __name__ == '__main__':
    g1 = [3,3,3,3,3,1,3]
    g2 = [2,1,3,3,3,2]

    print(groupThePeople(g1))
    print(groupThePeople(g2))
