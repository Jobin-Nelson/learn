'''
Created Date: 2023-10-22
Qn: You are given an array of integers nums (0-indexed) and an integer k.

    The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ...,
    nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

    Return the maximum possible score of a good subarray.
Link: https://leetcode.com/problems/maximum-score-of-a-good-subarray/
Notes:
    - iterate on both sides from k
'''
def maximumScore(nums: list[int], k: int) -> int:
    l = r = k
    res = cur_min = nums[k]

    while l >= 0 and r < len(nums):
        nl = nums[l-1] if l > 0 else 0
        nr = nums[r+1] if r < len(nums)-1 else 0
        if nl > nr:
            l -= 1
            cur_min = min(cur_min, nl)
        else:
            r += 1
            cur_min = min(cur_min, nr)
        res = max(res, cur_min * (r-l+1))
    return res

if __name__ == '__main__':
    n1, k1 = [1,4,3,7,4,5], 3
    n2, k2 = [5,5,4,5,4,1,1,1], 0

    print(maximumScore(n1, k1))
    print(maximumScore(n2, k2))
