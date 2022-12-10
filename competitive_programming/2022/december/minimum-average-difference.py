'''
Created Date: 2022-12-04
Qn: You are given a 0-indexed integer array nums of length n.

    The average difference of the index i is the absolute difference between the
    average of the first i + 1 elements of nums and the average of the last n - i -
    1 elements. Both averages should be rounded down to the nearest integer.

    Return the index with the minimum average difference. If there are multiple
    such indices, return the smallest one.

    Note:

        - The absolute difference of two numbers is the absolute value of their
          difference. 
        - The average of n elements is the sum of the n elements divided
          (integer division) by n. 
        - The average of 0 elements is considered to be 0.
Link: https://leetcode.com/problems/minimum-average-difference/
Notes:
    - variables to maintain
    - l_sum, l_len, r_sum(total - l_sum), r_len
'''
def minimumAverageDifference(nums: list[int]) -> int:
    res_avg = float('inf')
    res_ind = None
    l_sum, l_num, r_num = 0, 0, len(nums)
    total_sum = sum(nums)
    for i, n in enumerate(nums):
        l_sum += n
        l_num += 1
        r_num -= 1

        if r_num:
            r_diff = (total_sum - l_sum) // r_num
        else:
            r_diff = 0

        l_diff = l_sum // l_num

        cur_diff = abs(l_diff - r_diff)

        if cur_diff < res_avg:
            res_avg = cur_diff
            res_ind = i
    return res_ind

if __name__ == '__main__':
    n1 = [2,5,3,9,5,3]
    n2 = [0]
    n3 = [1]
    
    print(minimumAverageDifference(n1))
    print(minimumAverageDifference(n2))
    print(minimumAverageDifference(n3))
