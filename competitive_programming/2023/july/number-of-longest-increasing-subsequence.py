'''
Created Date: 2023-07-21
Qn: Given an integer array nums, return the number of longest increasing
    subsequences.

    Notice that the sequence has to be strictly increasing.
Link: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
Notes:
    - use 2 stacks
'''
def findNumberOfLIS(nums: list[int]) -> int:
    N = len(nums)
    length = [1] * N
    count = [1] * N

    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = 0
                if length[j] + 1 == length[i]:
                    count[i] += count[j]
    max_length = max(length)
    return sum(count[i] for i in range(N) if length[i] == max_length)

if __name__ == '__main__':
    n1 = [1,3,5,4,7]
    n2 = [2,2,2,2,2]

    print(findNumberOfLIS(n1))
    print(findNumberOfLIS(n2))
