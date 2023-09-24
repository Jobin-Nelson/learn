'''
Created Date: 2023-09-20
Qn: You are given an integer array nums and an integer x. In one operation, you
    can either remove the leftmost or the rightmost element from the array nums
    and subtract its value from x. Note that this modifies the array for future
    operations.

    Return the minimum number of operations to reduce x to exactly 0 if it is
    possible, otherwise, return -1.
Link: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
Notes:
    - use sliding window
'''
def minOperations(nums: list[int], x: int) -> int:
    target, N = sum(nums) - x, len(nums)
    l = r = cur_sum = 0
    max_window = -1
    while r < N:
        cur_sum += nums[r]
        while l <= r and cur_sum > target:
            cur_sum -= nums[l]
            l += 1
        if cur_sum == target: max_window = max(max_window, r-l+1)
        r += 1
    return -1 if max_window == -1 else N - max_window

    # def dfs(l: int, r: int, n: int, steps: int) -> int:
    #     if n == 0: return steps
    #     if l > r or n < 0: return len(nums) + 1
    #     return min(
    #         dfs(l, r-1, n-nums[r], steps+1),
    #         dfs(l+1, r, n-nums[l], steps+1)
    #     )
    # res = dfs(0, len(nums)-1, x, 0)
    # return res if res < len(nums) else -1

if __name__ == '__main__':
    n1, x1 = [1,1,4,2,3], 5
    n2, x2 = [5,6,7,8,9], 4
    n3, x3 = [3,2,20,1,1,3], 10

    print(minOperations(n1, x1))
    print(minOperations(n2, x2))
    print(minOperations(n3, x3))
