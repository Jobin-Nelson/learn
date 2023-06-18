'''
Created Date: 2023-06-16
Qn: Given an array nums that represents a permutation of integers from 1 to n.
    We are going to construct a binary search tree (BST) by inserting the
    elements of nums in order into an initially empty BST. Find the number of
    different ways to reorder nums so that the constructed BST is identical to
    that formed from the original array nums.

        For example, given nums = [2,1,3], we will have 2 as the root, 1 as a
        left child, and 3 as a right child. The array [2,3,1] also yields the
        same BST but [3,2,1] yields a different BST.

    Return the number of ways to reorder nums such that the BST formed is
    identical to the original BST formed from nums.

    Since the answer may be very large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
Notes:
    - use combination
'''
import math

def numOfWays(nums: list[int]) -> int:
    mod = 10**9 + 7

    def dfs(nums: list[int]) -> int:
        m = len(nums)
        if m < 3: return 1

        left_nodes = [a for a in nums if a < nums[0]]
        right_nodes = [a for a in nums if a > nums[0]]
        return dfs(left_nodes) * dfs(right_nodes) * math.comb(m-1, len(left_nodes)) % mod
    return (dfs(nums) - 1) % mod

if __name__ == '__main__':
    n1 = [2,1,3]
    n2 = [3,4,5,1,2]
    n3 = [1,2,3]

    print(numOfWays(n1))
    print(numOfWays(n2))
    print(numOfWays(n3))
