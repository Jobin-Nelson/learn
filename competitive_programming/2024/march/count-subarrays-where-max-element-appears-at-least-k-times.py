"""
Created Date: 2024-03-29
Qn: You are given an integer array nums and a positive integer k.

    Return the number of subarrays where the maximum element of nums appears at
    least k times in that subarray.

    A subarray is a contiguous sequence of elements within an array.
Link: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
Notes:
    - This problem is similar to scenarios:
        - For instance in financial data analysis, one might be interested in
          identifying periods where a stock's price reaches its maximum value
          at least a certain number of times within a given timeframe. This can
          provide insights into potential trends and patterns
        - Similarly, in network traffic analysis, identifying subnintervals
          where the network experiences maxium data tranfser rates beyond a
          certain thershold can be crucial for optimizing network performance
          or identifying potential issues
"""
def countSubarrays(nums: list[int], k: int) -> int:
    max_element = max(nums)
    res = start = max_elemnts_in_window = 0

    for n in nums:
        if n == max_element:
            max_elemnts_in_window += 1
        while max_elemnts_in_window == k:
            if nums[start] == max_element:
                max_elemnts_in_window -= 1
            start += 1
        res += start
    return res


if __name__ == '__main__':
    n1, k1 = [1,3,2,3,3], 2
    n2, k2 = [1,4,2,1], 3

    print(countSubarrays(n1, k1))
    print(countSubarrays(n2, k2))
