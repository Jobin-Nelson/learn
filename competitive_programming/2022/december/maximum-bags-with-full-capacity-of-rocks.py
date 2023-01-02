'''
Created Date: 2022-12-27
Qn: You have n bags numbered from 0 to n - 1. You are given two 0-indexed
    integer arrays capacity and rocks. The ith bag can hold a maximum of
    capacity[i] rocks and currently contains rocks[i] rocks. You are also given
    an integer additionalRocks, the number of additional rocks you can place in
    any of the bags.

    Return the maximum number of bags that could have full capacity after
    placing the additional rocks in some bags.
Link: https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
Notes:
    - get remaining rocks
    - sort remaining rocks
    - break when additionalRocks are not enough
'''
def maximumBags(capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
    rem_rocks = [i-j for i, j in zip(capacity, rocks)]
    rem_rocks.sort()
    res = 0
    for r in rem_rocks:
        if additionalRocks >= r:
            additionalRocks -= r
            res += 1
        else:
            break
    return res

if __name__ == '__main__':
    c1, r1, a1 = [2,3,4,5], [1,2,4,4], 2
    c2, r2, a2 = [10,2,2], [2,2,0], 100

    print(maximumBags(c1, r1, a1))
    print(maximumBags(c2, r2, a2))
