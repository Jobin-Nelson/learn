'''
Created Date: 2023-11-20
Qn:  You are given a 0-indexed array of strings garbage where garbage[i]
    represents the assortment of garbage at the ith house. garbage[i] consists
    only of the characters 'M', 'P' and 'G' representing one unit of metal,
    paper and glass garbage respectively. Picking up one unit of any type of
    garbage takes 1 minute.

    You are also given a 0-indexed integer array travel where travel[i] is the
    number of minutes needed to go from house i to house i + 1.

    There are three garbage trucks in the city, each responsible for picking up
    one type of garbage. Each garbage truck starts at house 0 and must visit
    each house in order; however, they do not need to visit every house.

    Only one garbage truck may be used at any given moment. While one truck is
    driving or picking up garbage, the other two trucks cannot do anything.

    Return the minimum number of minutes needed to pick up all the garbage.
Link: https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
Notes:
    - use prefix sum for calculating the time
'''
def garbageCollection(garbage: list[str], travel: list[int]) -> int:
    waste_last = {
        'P': 0,
        'G': 0,
        'M': 0,
    }
    for i in range(1, len(travel)):
        travel[i] += travel[i-1]

    res = 0
    for i, w in enumerate(garbage):
        res += len(w)
        for c in w:
            waste_last[c] = i

    for c in 'MPG':
        res += (travel[waste_last[c]-1] if waste_last[c] else 0)
    return res

if __name__ == '__main__':
    g1, t1 = ["G","P","GP","GG"], [2,4,3]
    g2, t2 = ["MMM","PGM","GP"], [3,10]

    print(garbageCollection(g1, t1))
    print(garbageCollection(g2, t2))
