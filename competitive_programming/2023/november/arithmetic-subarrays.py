'''
Created Date: 2023-11-23
Qn: A sequence of numbers is called arithmetic if it consists of at least two
    elements, and the difference between every two consecutive elements is the
    same. More formally, a sequence s is arithmetic if and only if s[i+1] -
    s[i] == s[1] - s[0] for all valid i.

    For example, these are arithmetic sequences:

    1, 3, 5, 7, 9
    7, 7, 7, 7 
    3, -1, -5, -9

    The following sequence is not arithmetic:

    1, 1, 2, 5, 7

    You are given an array of n integers, nums, and two arrays of m integers
    each, l and r, representing the m range queries, where the ith query is the
    range [l[i], r[i]]. All the arrays are 0-indexed.

    Return a list of boolean elements answer, where answer[i] is true if the
    subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to
    form an arithmetic sequence, and false otherwise.
Link: https://leetcode.com/problems/arithmetic-subarrays/
Notes:
    - use hashset to check each num + diff is present
'''
def checkArithmeticsSubArrays(nums: list[int], l: list[int], r: list[int]) -> list[bool]:
    def check(arr: list[int]) -> bool:
        min_el = min(arr)
        max_el = max(arr)
        el_set = set(arr)

        if (max_el - min_el) % (len(arr) - 1) != 0: return False
        d = (max_el - min_el) / (len(arr) - 1)
        cur = min_el + d
        while cur < max_el:
            if cur not in el_set:
                return False
            cur += d
        return True

        # if len(arr) < 2: return False
        # arr.sort()
        # d = arr[1] - arr[0]
        # for i in range(2, len(arr)):
        #     if arr[i] - arr[i-1] != d:
        #         return False
        # return True

    return [check(nums[s:e+1]) for s, e in zip(l,r)]


if __name__ == '__main__':
    n1, l1, r1 = [4,6,5,9,3,7], [0,0,2], [2,3,5]
    n2, l2, r2 = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10]

    print(checkArithmeticsSubArrays(n1, l1, r1))
    print(checkArithmeticsSubArrays(n2, l2, r2))
