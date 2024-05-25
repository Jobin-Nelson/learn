"""
Created Date: 2024-05-23
Qn: You are given an array nums of positive integers and a positive integer k.

    A subset of nums is beautiful if it does not contain two integers with an
    absolute difference equal to k.

    Return the number of non-empty beautiful subsets of the array nums.

    A subset of nums is an array that can be obtained by deleting some
    (possibly none) elements from nums. Two subsets are different if and only
    if the chosen indices to delete are different.
Link: https://leetcode.com/problems/the-number-of-beautiful-subsets/
Notes:
    - use dfs
"""
from collections import Counter

def beautifulSubsets(nums: list[int], k: int) -> int:
    cnt = Counter(nums)

    groups = []
    visit = set()

    cache = {}
    def helper(n: int, g: dict[int, int]) -> int:
        if n not in g: return 1
        if n in cache: return cache[n]
        skip = helper(n+k, g)
        include = (2**g[n]-1) * helper(n+2*k, g)
        cache[n] = skip + include
        return skip + include

    for n in cnt.keys():
        if n in visit:
            continue
        while n - k in cnt:
            n -= k
        g = {}
        while n in cnt:
            g[n] = cnt[n]
            visit.add(n)
            n += k
        groups.append(g)

    res = 1
    for g in groups:
        n = min(g.keys())
        res *= helper(n, g)
    return res -1


    # def dfs(i: int, sub: dict[int, int]) -> int:
    #     if i == len(nums):
    #         return 1
    #     res = dfs(i+1, sub)
    #     if not sub[nums[i]+k] and not sub[nums[i]-k]:
    #         sub[nums[i]] += 1
    #         res += dfs(i+1, sub)
    #         sub[nums[i]] -= 1
    #     return res
    # return dfs(0, defaultdict(int))



if __name__ == '__main__':
    n1, k1 = [2, 4, 6], 2
    n2, k2 = [1], 1

    print(beautifulSubsets(n1, k1))
    print(beautifulSubsets(n2, k2))
    
