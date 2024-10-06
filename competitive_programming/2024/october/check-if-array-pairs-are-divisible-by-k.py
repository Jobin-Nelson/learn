"""
Created Date: 2024-10-01
Qn: Given an array of integers arr of even length n and an integer k.

    We want to divide the array into exactly n / 2 pairs such that the sum of
    each pair is divisible by k.

    Return true If you can find a way to do that or false otherwise.
Link: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
Notes:
    - use remainder count, each same remainder should be even
"""


def canArrange(arr: list[int], k: int) -> bool:
    remainder_count = {}
    for i in arr:
        remainder_count[(i % k + k) % k] = remainder_count.get((i % k + k) % k, 0) + 1

    for i in arr:
        rem = (i % k + k) % k
        if rem == 0:
            if remainder_count[rem] & 1:
                return False
        elif remainder_count[rem] != remainder_count.get(k - rem, 0):
            return False
    return True


if __name__ == '__main__':
    arr1, k1 = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5
    arr2, k2 = list(range(1, 7)), 7
    arr3, k3 = list(range(1, 7)), 10

    print(canArrange(arr1, k1))
    print(canArrange(arr2, k2))
    print(canArrange(arr3, k3))
