'''
Created Date: 2023-11-19
Qn: Given an integer array nums, your goal is to make all elements in nums
    equal. To complete one operation, follow these steps:

        - Find the largest value in nums. Let its index be i (0-indexed) and
          its value be largest. If there are multiple elements with the largest
          value, pick the smallest i. 
        - Find the next largest value in nums strictly smaller than largest.
          Let its value be nextLargest. 
        - Reduce nums[i] to nextLargest.

    Return the number of operations to make all elements in nums equal.
Link: https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
Notes:
    - sort and iterate from right to left
'''
def reductionOperations(nums: list[int]) -> int:
    nums.sort()
    res, N = 0, len(nums)
    for i in range(N-2, -1, -1):
        if nums[i] == nums[i+1]: continue
        res += (N - i - 1)
    return res

if __name__ == '__main__':
    n1 = [5, 1, 3]
    n2 = [1, 1, 1]
    n3 = [1, 1, 2, 2, 3]

    print(reductionOperations(n1))
    print(reductionOperations(n2))
    print(reductionOperations(n3))
