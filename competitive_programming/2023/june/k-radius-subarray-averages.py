'''
Created Date: 2023-06-20
Qn: You are given a 0-indexed array nums of n integers, and an integer k.

    The k-radius average for a subarray of nums centered at some index i with
    the radius k is the average of all elements in nums between the indices i -
    k and i + k (inclusive). If there are less than k elements before or after
    the index i, then the k-radius average is -1.

    Build and return an array avgs of length n where avgs[i] is the k-radius
    average for the subarray centered at index i.

    The average of x elements is the sum of the x elements divided by x, using
    integer division. The integer division truncates toward zero, which means
    losing its fractional part.

        - For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 +
          1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

Link: https://leetcode.com/problems/k-radius-subarray-averages/
Notes:
    - use sliding window
'''
def getAverages(nums: list[int], k: int) -> list[int]:
    i = k
    l, r = 0, 2*k
    N = len(nums)
    res = [-1] * N
    cur_sum = sum(nums[:r])

    while r < N:
        cur_sum += nums[r]
        res[i] = cur_sum // (2 * k + 1)
        cur_sum -= nums[l]
        r += 1
        i += 1
        l += 1
    return res

if __name__ == '__main__':
    n1, k1 = [7,4,3,9,1,8,5,2,6], 3
    n2, k2 = [100000], 0
    n3, k3 = [8], 100_000

    print(getAverages(n1, k1))
    print(getAverages(n2, k2))
    print(getAverages(n3, k3))
