"""
Created Date: 2024-02-15
Qn: You are given an array of positive integers nums of length n.

    A polygon is a closed plane figure that has at least 3 sides. The longest
    side of a polygon is smaller than the sum of its other sides.

    Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ...,
    ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak,
    then there always exists a polygon with k sides whose lengths are a1, a2,
    a3, ..., ak.

    The perimeter of a polygon is the sum of lengths of its sides.

    Return the largest possible perimeter of a polygon whose sides can be
    formed from nums, or -1 if it is not possible to create a polygon.
Link: https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
Notes:
    - reverse sort and iterate through it till it meets the condition a1+a2+a3...a(k-1)>ak
"""
def largestPerimeter(nums: list[int]) -> int:
    nums.sort(reverse=True)
    total = sum(nums)

    for n in nums:
        total -= n
        if total > n:
            return total+n

    return -1

if __name__ == '__main__':
    n1 = [5, 5, 5]
    n2 = [1, 12, 1, 2, 5, 50, 3]
    n3 = [5, 5, 50]

    print(largestPerimeter(n1))
    print(largestPerimeter(n2))
    print(largestPerimeter(n3))
