'''
Created Date: 2023-11-15
Qn: You are given an array of positive integers arr. Perform some operations
    (possibly none) on arr so that it satisfies these conditions:

        The value of the first element in arr must be 1. The absolute
        difference between any 2 adjacent elements must be less than or equal
        to 1. In other words, abs(arr[i] - arr[i - 1]) <= 1 for each i where 1
        <= i < arr.length (0-indexed). abs(x) is the absolute value of x.

    There are 2 types of operations that you can perform any number of times:

        Decrease the value of any element of arr to a smaller positive integer.
        Rearrange the elements of arr to be in any order.

    Return the maximum possible value of an element in arr after performing the
    operations to satisfy the conditions.
Link: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
Notes:
    - sort or count frequency then increment while iterating over
'''
def maximumElementAfterDecrementingAndRearranging(arr: list[int]) -> int:
    N = len(arr)
    count = [0] * (N + 1)
    for num in arr:
        count[min(num, N)] += 1

    res = 1
    for n in range(2, N+1):
        res = min(res + count[n], n)
    return res

    # arr.sort()
    # max_el = 0
    # for e in arr:
    #     max_el = min(max_el+1, e)
    # return max_el

if __name__ == '__main__':
    a1 = [2, 2, 1, 2, 1]
    a2 = [100, 1, 1000]
    a3 = [1, 2, 3, 4, 5]

    print(maximumElementAfterDecrementingAndRearranging(a1))
    print(maximumElementAfterDecrementingAndRearranging(a2))
    print(maximumElementAfterDecrementingAndRearranging(a3))
