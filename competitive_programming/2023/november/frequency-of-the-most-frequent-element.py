'''
Created Date: 2023-11-18
Qn: The frequency of an element is the number of times it occurs in an array.

    You are given an integer array nums and an integer k. In one operation, you
    can choose an index of nums and increment the element at that index by 1.

    Return the maximum possible frequency of an element after performing at
    most k operations.
Link: https://leetcode.com/problems/frequency-of-the-most-frequent-element/
Notes:
    - use sliding window
'''
def maxFrequency(nums: list[int], k: int) -> int:
    # advanced sliding window approach
    nums.sort()
    l = cur = 0

    for r in range(len(nums)):
        target = nums[r]
        cur += target
        if ((r-l+1) * target) - cur > k:
            cur -= nums[l]
            l += 1
    return len(nums) - l
    
    # sliding window approach
    # nums.sort()
    # l = cur = res = 0
    #
    # for r in range(len(nums)):
    #     target = nums[r]
    #     cur += target
    #     while ((r-l+1) * target) - cur > k:
    #         cur -= nums[l]
    #         l += 1
    #     res = max(res, r-l+1)
    # return res

if __name__ == '__main__':
    n1, k1 = [1,2,4], 5
    n2, k2 = [1,4,8,13], 5
    n3, k3 = [3,9,6], 2

    print(maxFrequency(n1, k1))
    print(maxFrequency(n2, k2))
    print(maxFrequency(n3, k3))
