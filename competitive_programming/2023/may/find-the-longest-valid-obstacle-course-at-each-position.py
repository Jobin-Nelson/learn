'''
Created Date: 2023-05-07
Qn: You want to build some obstacle courses. You are given a 0-indexed integer
    array obstacles of length n, where obstacles[i] describes the height of the
    ith obstacle.

    For every index i between 0 and n - 1 (inclusive), find the length of the
    longest obstacle course in obstacles such that:

        - You choose any number of obstacles between 0 and i inclusive. 
        - You must include the ith obstacle in the course. 
        - You must put the chosen obstacles in the same order as they appear in
          obstacles. 
        - Every obstacle (except the first) is taller than or the same height
          as the obstacle immediately before it.

    Return an array ans of length n, where ans[i] is the length of the longest
    obstacle course for index i as described above.
Link: https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
Notes:
    - like longest increasing subsequence
    - bisect right and append if index is higher than length of dp
'''
from bisect import bisect_right

def longestObstacleCourseAtEachPosition(obstacles: list[int]) -> list[int]:
    dp = []
    res = []

    for o in obstacles:
        index = bisect_right(dp, o)

        if index < len(dp):
            dp[index] = o
        else:
            dp.append(o)

        res.append(index + 1)
    return res

if __name__ == '__main__':
    o1 = [1,2,3,2]
    o2 = [2,2,1]
    o3 = [3,1,5,6,4,2]

    print(longestObstacleCourseAtEachPosition(o1))
    print(longestObstacleCourseAtEachPosition(o2))
    print(longestObstacleCourseAtEachPosition(o3))
