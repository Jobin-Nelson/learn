"""
Created Date: 2024-05-30
Qn: Given an array of integers arr.

    We want to select three indices i, j and k where (0 <= i < j <= k <
    arr.length).

    Let's define a and b as follows:

        - a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
        - b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

    Note that ^ denotes the bitwise-xor operation.

    Return the number of triplets (i, j and k) Where a == b.
Link: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
Notes:
"""
def countTriplets(arr: list[int]) -> int:
    N = len(arr)
    res = 0

    for i in range(N-1):
        cur_xor = arr[i]
        for k in range(i+1, N):
            cur_xor ^= arr[k]
            if cur_xor == 0:
                res += (k-i)
    return res

if __name__ == '__main__':
    a1 = [2,3,1,6,7]
    a2 = [1,1,1,1,1]

    print(countTriplets(a1))
    print(countTriplets(a2))
