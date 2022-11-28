'''
Created Date: 2022-09-21
Qn: You are given an integer array nums and an array queries where queries[i] =
    [vali, indexi].

    For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print
    the sum of the even values of nums.

    Return an integer array answer where answer[i] is the answer to the ith query.
Link: https://leetcode.com/problems/sum-of-even-numbers-after-queries/
Notes:
    - find the initial sum of even numbers
    - decrement and increment with value accordingly
'''
def sumEventAfterQueries(nums: list[int], queries: list[list[int]]) -> list[int]:
    even_sum = sum(n for n in nums if n % 2 == 0)
    res = []

    for val, ind in queries:
        cur_num = nums[ind]
        if cur_num % 2 == 0: even_sum -= cur_num
        cur_num += val
        if cur_num % 2 == 0: even_sum += cur_num
        nums[ind] = cur_num
        res.append(even_sum)
    return res

if __name__ == '__main__':
    n1, q1 = [1, 2, 3, 4], [[1,0],[-3,1],[-4,0],[2,3]]
    n2, q2 = [1], [[4, 0]]

    print(sumEventAfterQueries(n1, q1))
    print(sumEventAfterQueries(n2, q2))
