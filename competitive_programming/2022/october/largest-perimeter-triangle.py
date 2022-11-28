'''
Created Date: 2022-10-12
Qn: Given an integer array nums, return the largest perimeter of a triangle
    with a non-zero area, formed from three of these lengths. If it is
    impossible to form any triangle of a non-zero area, return 0.
Link: https://leetcode.com/problems/largest-perimeter-triangle/
Notes:
    - sort
    - iterate from the back of the list
    - return the three consecutive number that staisfies the condition
    - nums[small side] + num[small side] > nums[large side]
'''
def largestPerimeter(nums: list[int]) -> int:
    N = len(nums)
    i, j = N-1, N-3
    nums.sort()

    while j >= 0:
        if nums[j] + nums[j+1] > nums[i]:
            return nums[j] + nums[j+1] + nums[i]
        i -= 1
        j -= 1
    return 0

if __name__ == '__main__':
    n1, n2 = [2, 1, 2], [1, 2, 1]

    print(largestPerimeter(n1))
    print(largestPerimeter(n2))
