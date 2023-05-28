'''
Created Date: 2023-05-28
Qn: Given a wooden stick of length n units. The stick is labelled from 0 to n.
    For example, a stick of length 6 is labelled as follows:

    Given an integer array cuts where cuts[i] denotes a position you should
    perform a cut at.

    You should perform the cuts in order, you can change the order of the cuts
    as you wish.

    The cost of one cut is the length of the stick to be cut, the total cost is
    the sum of costs of all cuts. When you cut a stick, it will be split into
    two smaller sticks (i.e. the sum of their lengths is the length of the
    stick before the cut). Please refer to the first example for a better
    explanation.

    Return the minimum total cost of the cuts.
Link: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
Notes:
    - use dfs
'''
def minCost(n: int, cuts: list[int]) -> int:
    dp = {}

    def dfs(l: int, r: int) -> int:
        if r - l == 1: return 0
        if (l, r) in dp: return dp[(l, r)]

        res = float('inf')
        for c in cuts:
            if l < c < r:
                res = min(res, (r-l) + dfs(l, c) + dfs(c, r))
        dp[(l, r)] = 0 if res == float('inf') else res
        return dp[(l, r)]
    return dfs(0, n)

if __name__ == '__main__':
    n1, c1 = 7, [1,3,4,5]
    n2, c2 = 9, [5,6,1,4,2]

    print(minCost(n1, c1))
    print(minCost(n2, c2))

