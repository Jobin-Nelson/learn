'''
Created Date: 2022-12-18
Qn: Given an array of integers temperatures represents the daily temperatures,
    return an array answer such that answer[i] is the number of days you have
    to wait after the ith day to get a warmer temperature. If there is no
    future day for which this is possible, keep answer[i] == 0 instead.
Link: https://leetcode.com/problems/daily-temperatures/
Notes:
    - use stack to hold onto index
    - reverse iterate and pop till you find a number greater than the current one
'''
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    N = len(temperatures)
    if N <= 1: return [0]
    stack = [N-1]
    res = [0]
    for i in range(N-2, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()
        if len(stack) == 0:
            res.append(0)
        else:
            res.append(stack[-1] - i)
        stack.append(i)
    res.reverse()
    return res

if __name__ == '__main__':
    t1 = [73,74,75,71,69,72,76,73]
    t2 = [30,40,50,60]
    t3 = [30,60,90]

    print(dailyTemperatures(t1))
    print(dailyTemperatures(t2))
    print(dailyTemperatures(t3))
