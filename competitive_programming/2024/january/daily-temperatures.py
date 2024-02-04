"""
Created Date: 2024-01-31
Qn: Given an array of integers temperatures represents the daily temperatures,
    return an array answer such that answer[i] is the number of days you have
    to wait after the ith day to get a warmer temperature. If there is no
    future day for which this is possible, keep answer[i] == 0 instead.
Link: https://leetcode.com/problems/daily-temperatures/
Notes:
    - use monotonically decreasing stack
"""
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    # brute force
    # n = len(temperatures)
    # res = [0] * n
    # for i in range(n):
    #     for j in range(i, n):
    #         if temperatures[i] < temperatures[j]:
    #             res[i] = j-i
    #             break
    # return res

    # iterate backwards
    # n = len(temperatures)
    # res = [0] * n
    # stack = []
    # for i in range(n-1, -1, -1):
    #     while stack and stack[-1][0] <= temperatures[i]:
    #         stack.pop()
    #     if stack:
    #         res[i] = stack[-1][1] - i
    #     else:
    #         res[i] = 0
    #     stack.append((temperatures[i], i))
    # return res

    # monotonically decreasing
    res = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and stack[-1][0] < t:
            _, pi = stack.pop()
            res[pi] = i - pi
        stack.append((t, i))
    return res

if __name__ == '__main__':
    t1 = [73,74,75,71,69,72,76,73]
    t2 = [30,40,50,60]
    t3 = [30,60,90]

    print(dailyTemperatures(t1))
    print(dailyTemperatures(t2))
    print(dailyTemperatures(t3))
