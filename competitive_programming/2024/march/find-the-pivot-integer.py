"""
Created Date: 2024-03-13
Qn: Given a positive integer n, find the pivot integer x such that:

        - The sum of all elements between 1 and x inclusively equals the sum of
          all elements between x and n inclusively.

    Return the pivot integer x. If no such integer exists, return -1. It is
    guaranteed that there will be at most one pivot index for the given input.
Link: https://leetcode.com/problems/find-the-pivot-integer/
Notes:
    - use binary search
"""
def pivotInteger(n: int) -> int:
    total = n * (n+1) // 2
    l, r = 1, n
    while l <= r:
        m = (r+l) >> 1
        left_sum = m * (m+1) // 2
        right_sum = total - left_sum + m
        if left_sum < right_sum:
            l = m + 1
        elif left_sum > right_sum:
            r = m - 1
        else:
            return m
    return -1

if __name__ == '__main__':
    n1 = 8
    n2 = 1
    n3 = 4

    print(pivotInteger(n1))
    print(pivotInteger(n2))
    print(pivotInteger(n3))
