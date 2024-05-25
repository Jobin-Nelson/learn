"""
Created Date: 2024-05-20
Qn: The XOR total of an array is defined as the bitwise XOR of all its
    elements, or 0 if the array is empty.

        - For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.

    Given an array nums, return the sum of all XOR totals for every subset of
    nums. 

    Note: Subsets with the same elements should be counted multiple times.

    An array a is a subset of an array b if a can be obtained from b by
    deleting some (possibly zero) elements of b.


Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
Notes:
    - use dfs
"""
def subsetXORSum(nums: list[int]) -> int:
    def dfs(i: int, total: int) -> int:
        if i == len(nums): return total
        return dfs(i+1, nums[i] ^ total) + dfs(i+1, total)
    return dfs(0, 0)

if __name__ == '__main__':
    n1 = [1,3]
    n2 = [5,1,6]
    n3 = list(range(3, 9))

    print(subsetXORSum(n1))
    print(subsetXORSum(n2))
    print(subsetXORSum(n3))
