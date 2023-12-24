"""
Created Date: 2023-12-18
Qn: The product difference between two pairs (a, b) and (c, d) is defined as (a
    * b) - (c * d).

        - For example, the product difference between (5, 6) and (2, 7) is (5 *
        6) - (2 * 7) = 16.

    Given an integer array nums, choose four distinct indices w, x, y, and z
    such that the product difference between pairs (nums[w], nums[x]) and
    (nums[y], nums[z]) is maximized.

    Return the maximum such product difference.
Link: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
Notes:
    - sort and grab first 2 and last 2 elements
"""
def maxProductDifference(nums: list[int]) -> int:
    nums.sort()
    a, b, c, d = nums[0], nums[1], nums[-1], nums[-2]
    return (c * d) - (a * b)

if __name__ == '__main__':
    n1 = [5,6,2,7,4]
    n2 = [4,2,5,9,7,4,8]

    print(maxProductDifference(n1))
    print(maxProductDifference(n2))
