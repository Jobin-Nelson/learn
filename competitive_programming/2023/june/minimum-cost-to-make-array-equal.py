'''
Created Date: 2023-06-21
Qn: You are given two 0-indexed arrays nums and cost consisting each of n
    positive integers.

    You can do the following operation any number of times:

        Increase or decrease any element of the array nums by 1.

    The cost of doing one operation on the ith element is cost[i].

    Return the minimum total cost such that all the elements of the array nums
    become equal.
Link: https://leetcode.com/problems/minimum-cost-to-make-array-equal/
Notes:
    - use binary search
'''
def minCost(nums: list[int], cost: list[int]) -> int:
    def get_cost(base) -> int:
        return sum(abs(base-n) * c for n, c in zip(nums, cost))
    l, r = min(nums), max(nums)
    res = get_cost(nums[0])
    while l < r:
        m = (l + r) // 2
        c1 = get_cost(m)
        c2 = get_cost(m+1)
        res = min(c1, c2)
        if c1 > c2:
            l = m + 1
        else:
            r = m
    return res

if __name__ == '__main__':
    n1, c1 = [1,3,5,2], [2,3,1,14]
    n2, c2 = [2,2,2,2,2], [4,2,8,1,3]

    print(minCost(n1, c1))
    print(minCost(n2, c2))
