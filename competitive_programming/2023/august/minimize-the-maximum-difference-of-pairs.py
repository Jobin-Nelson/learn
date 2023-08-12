'''
Created Date: 2023-08-09
Qn: You are given a 0-indexed integer array nums and an integer p. Find p pairs
    of indices of nums such that the maximum difference amongst all the pairs
    is minimized. Also, ensure no index appears more than once amongst the p
    pairs.

    Note that for a pair of elements at the index i and j, the difference of
    this pair is |nums[i] - nums[j]|, where |x| represents the absolute value
    of x.

    Return the minimum maximum difference among all p pairs. We define the
    maximum of an empty set to be zero.
Link: https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
Notes:
    - use binary search
'''
def minimizeMax(nums: list[int], p: int) -> int:
    nums.sort()
    N = len(nums)

    def count_pairs(threshold: int) -> int:
        index, count = 0, 0
        while index < N-1:
            if nums[index+1] - nums[index] <= threshold:
                count += 1
                index += 1
            index += 1
        return count
    
    l, r = 0, nums[-1] - nums[0]
    while l < r:
        m = l + ((r - l) >> 1)
        if count_pairs(m) >= p:
            r = m
        else:
            l = m + 1
    return l

if __name__ == '__main__':
    n1, p1 = [10,1,2,7,1,3], 2
    n2, p2 = [4,2,1,2], 1

    print(minimizeMax(n1, p1))
    print(minimizeMax(n2, p2))
