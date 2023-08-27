'''
Created Date: 2023-08-26
Qn: You are given an array of n pairs pairs where pairs[i] = [lefti, righti]
    and lefti < righti.

    A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs
    can be formed in this fashion.

    Return the length longest chain which can be formed.

    You do not need to use up all the given intervals. You can select pairs in
    any order.
Link: https://leetcode.com/problems/maximum-length-of-pair-chain/
Notes:
    - sort by second element
'''
def findLongestChain(pairs: list[list[int]]) -> int:
    pairs.sort(key=lambda x: x[1])
    res, cur = 0, float('-inf')

    for pair in pairs:
        if cur < pair[0]:
            cur = pair[1]
            res += 1
    return res

if __name__ == '__main__':
    p1 = [[1,2],[2,3],[3,4]]
    p2 = [[1,2],[7,8],[4,5]]

    print(findLongestChain(p1))
    print(findLongestChain(p2))
