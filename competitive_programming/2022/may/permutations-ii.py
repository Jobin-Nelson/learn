'''
Qn: Given a collection of numbers, nums, that might contain duplicates,
    return all possible unique permutations in any order
Link: https://leetcode.com/problems/permutations-ii/
Notes:
    - easy with itertools permutations
    - backtracking with two lists to track perm and total res
'''
from itertools import permutations

def permuteUnique(nums: list[int]) -> list[int]:
    return list(set(permutations(nums)))

def permuteUniqueBackTrack(nums: list[int]) -> list[int]:
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    res, perm = [], []
    N = len(nums)

    def dfs():
        if len(perm) == N:
            res.append(perm.copy())
            return
        for n in count:
            if count[n]:
                perm.append(n)
                count[n] -= 1
                dfs()
                count[n] += 1
                perm.pop()
    dfs()
    return res
if __name__ == '__main__':
    n1 = [1, 1, 2]
    n2 = [1, 2, 3]
    print('with itertools permutations')
    print(permuteUnique(n1))
    print(permuteUnique(n2))
    print('\nwith backtracking algorithm')
    print(permuteUnique(n1))
    print(permuteUnique(n2))
