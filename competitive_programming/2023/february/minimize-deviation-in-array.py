'''
Created Date: 2023-02-24
Qn: You are given an array nums of n positive integers.

    You can perform two types of operations on any element of the array any
    number of times:

    - If the element is even, divide it by 2. 
        - For example, if the array is [1,2,3,4], then you can do this
          operation on the last element, and the array will be [1,2,3,2].
    - If the element is odd, multiply it by 2.
        - For example, if the array is [1,2,3,4], then you can do this
          operation on the first element, and the array will be [2,2,3,4].

    The deviation of the array is the maximum difference between any two
    elements in the array.

    Return the minimum deviation the array can have after performing some
    number of operations.
Link: https://leetcode.com/problems/minimize-deviation-in-array/
Notes:
    - use heap
'''
import heapq

def minimumDeviation(nums: list[int]) -> int:
    if nums is None: return float('inf')
    nums = [-(n << 1) if n & 1 else -n for n in nums]
    min_val = -max(nums)
    res = float('inf')
    heapq.heapify(nums)

    while nums[0] & 1 == 0:
        n = -nums[0]
        res = min(res, n - min_val)
        n >>= 1
        heapq.heapreplace(nums, -n)
        min_val = min(min_val, n)
    return min(res, -nums[0] - min_val)

if __name__ == '__main__':
    n1 = [1, 2, 3, 4]
    n2 = [4, 1, 5, 20, 3]
    n3 = [2, 10, 8]

    print(minimumDeviation(n1))
    print(minimumDeviation(n2))
    print(minimumDeviation(n3))
