'''
Created Date: 2023-08-14
Qn: Given an integer array nums and an integer k, return the kth largest
    element in the array.

    Note that it is the kth largest element in the sorted order, not the kth
    distinct element.

    Can you solve it without sorting?
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Notes:
    - use counting sort
'''
def findKthLargest(nums: list[int], k: int) -> int:
    min_value = min(nums)
    max_value = max(nums)

    count = [0] * (max_value - min_value + 1)

    for num in nums:
        count[num - min_value] += 1

    remain = k
    for num in range(len(count)-1, -1, -1):
        remain -= count[num]
        if remain <= 0:
            return num + min_value
    return -1

if __name__ == '__main__':
    n1, k1 = [3,2,1,5,6,4], 2
    n2, k2 = [3,2,3,1,2,4,5,5,6], 4

    print(findKthLargest(n1, k1))
    print(findKthLargest(n2, k2))
