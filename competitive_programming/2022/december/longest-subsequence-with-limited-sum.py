'''
Created Date: 2022-12-25
Qn: You are given an integer array nums of length n, and an integer array
    queries of length m.

    Return an array answer of length m where answer[i] is the maximum size of a
    subsequence that you can take from nums such that the sum of its elements
    is less than or equal to queries[i].

    A subsequence is an array that can be derived from another array by
    deleting some or no elements without changing the order of the remaining
    elements.
Link: https://leetcode.com/problems/longest-subsequence-with-limited-sum/
Notes:
    - sort
    - get cumulative sum
    - binary search 
'''
import bisect

def answerQueries(nums: list[int], queries: list[int]) -> list[int]:
    nums.sort()

    for i in range(1, len(nums)):
        nums[i] += nums[i-1]

    res = []

    for q in queries:
        res.append(bisect.bisect_right(nums, q))

    return res

if __name__ == '__main__':
    n1, q1 = [4, 5, 2, 1], [3, 10, 21]
    n2, q2 = [2,3,4,5], [1]

    print(answerQueries(n1, q1))
    print(answerQueries(n2, q2))
