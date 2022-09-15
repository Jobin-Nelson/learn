'''
Created Date: 11-06-2022
Qn: You are given an integer array nums and an integer x. In one operation, 
    you can either remove the leftmost or the rightmost element from the array nums 
    and subtract its value from x. Note that this modifies the array for future operations.
    Return the minimum number of operations to reduce x to exactly 0 if it is possible, 
    otherwise, return -1.
Link: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
Notes:
    - hashmap the cumulative sum
    - find if the difference between sum of nums and x is betweent the cumulative sum
'''
def minOperations(nums: list[int], x: int) -> int:
    z, dp = 0, [0]
    for n in nums:
        z += n
        dp.append(z)
    lookup = {v:i for i, v in enumerate(dp)}

    y = sum(nums) - x
    res = -1
    for l_val, l_ind in lookup.items():
        if l_val + y in lookup:
            res = max(res, lookup[l_val+y] - l_ind)
    return len(nums) - res if res != 1 else res

if __name__ == '__main__':
    n1, x1 = [1, 1, 4, 2, 3], 5
    n2, x2 = [5, 6, 7, 8, 9], 4
    n3, x3 = [3, 2, 20, 1, 1, 3], 10
    print(minOperations(n1, x1))
    print(minOperations(n2, x2))
    print(minOperations(n3, x3))
