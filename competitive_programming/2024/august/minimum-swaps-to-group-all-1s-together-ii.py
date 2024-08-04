"""
Created Date: 2024-08-02
Qn: A swap is defined as taking two distinct positions in an array and swapping
    the values in them.

    A circular array is defined as an array where we consider the first element
    and the last element to be adjacent.

    Given a binary circular array nums, return the minimum number of swaps
    required to group all 1's present in the array together at any location.
Link: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
Notes:
    - use sliding window
"""


def minSwaps(nums: list[int]) -> int:
    N = len(nums)
    ones = sum(nums)
    l = 0
    max_ones = 0
    cur_ones = 0
    for r in range(2 * N):
        if r - l + 1 > ones:
            cur_ones -= nums[l % N]
            l += 1
        if nums[r % N] == 1:
            cur_ones += 1
        max_ones = max(max_ones, cur_ones)
    return ones - max_ones


if __name__ == '__main__':
    n1 = [0, 1, 0, 1, 1, 0, 0]
    n2 = [0, 1, 1, 1, 0, 0, 1, 1, 0]
    n3 = [1, 1, 0, 0, 1]

    print(minSwaps(n1))
    print(minSwaps(n2))
    print(minSwaps(n3))
