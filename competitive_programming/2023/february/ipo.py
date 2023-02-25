'''
Created Date: 2023-02-23
Qn: Suppose LeetCode will start its IPO soon. In order to sell a good price of
    its shares to Venture Capital, LeetCode would like to work on some projects
    to increase its capital before the IPO. Since it has limited resources, it
    can only finish at most k distinct projects before the IPO. Help LeetCode
    design the best way to maximize its total capital after finishing at most k
    distinct projects.

    You are given n projects where the ith project has a pure profit profits[i]
    and a minimum capital of capital[i] is needed to start it.

    Initially, you have w capital. When you finish a project, you will obtain
    its pure profit and the profit will be added to your total capital.

    Pick a list of at most k distinct projects from given projects to maximize
    your final capital, and return the final maximized capital.

    The answer is guaranteed to fit in a 32-bit signed integer.
Link: https://leetcode.com/problems/ipo/
Notes:
    - use priority queue (max heap)
'''
import heapq

def findMaximizedCapital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    N = len(profits)
    projects = list(zip(capital, profits))
    projects.sort()
    q = []
    ptr = 0

    for _ in range(k):
        while ptr < N and projects[ptr][0] <= w:
            heapq.heappush(q, -projects[ptr][1])
            ptr += 1
        if not q: break
        w += -heapq.heappop(q)
    return w

if __name__ == '__main__':
    k1, w1, p1, c1 = 2, 0, [1,2,3], [0,1,1]
    k2, w2, p2, c2 = 3, 0, [1,2,3], [0,1,2]

    print(findMaximizedCapital(k1, w1, p1, c1))
    print(findMaximizedCapital(k2, w2, p2, c2))
