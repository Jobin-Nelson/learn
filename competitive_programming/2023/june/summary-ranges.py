'''
Created Date: 2023-06-12
Qn: You are given a sorted unique integer array nums.

    A range [a,b] is the set of all integers from a to b (inclusive).

    Return the smallest sorted list of ranges that cover all the numbers in the
    array exactly. That is, each element of nums is covered by exactly one of the
    ranges, and there is no integer x such that x is in one of the ranges but not
    in nums.

    Each range [a,b] in the list should be output as:

        - "a->b" if a != b
        - "a" if a == b

Link: https://leetcode.com/problems/summary-ranges/
Notes:
    - use sliding window, 2 pointer
'''
def summaryPages(nums: list[int]) -> list[str]:
    N = len(nums)
    if N == 1: return [str(nums[0])]

    res = []
    l, r = 0, 0

    while r < N:
        k = 0
        while r < N and nums[l] + k == nums[r]:
            k += 1
            r += 1
        # res.append('->'.join(map(str, nums[l:r])))
        if l == r - 1:
            res.append(str(nums[l]))
        else:
            # res.append('->'.join(map(str, (nums[l], nums[r-1]))))
            res.append(str(nums[l]) + '->' + str(nums[r-1]))
        l = r

    return res

if __name__ == '__main__':
    n1 = [0,1,2,4,5,7]
    n2 = [0,2,3,4,6,8,9]

    print(summaryPages(n1))
    print(summaryPages(n2))
