'''
Created Date: 2023-08-02
Qn: Given an array nums of distinct integers, return all the possible
    permutations. You can return the answer in any order.
Link: https://leetcode.com/problems/permutations/
Notes:
    - use backtracking
'''
def permute(nums: list[int]) -> list[list[int]]:
    res = []
    if len(nums) == 1: return [nums[:]]

    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res

    # return list(map(list, itertools.permutations(nums)))

if __name__ == '__main__':
    n1 = [1,2,3]
    n2 = [0,1]
    n3 = [1]

    print(permute(n1))
    print(permute(n2))
    print(permute(n3))
