'''
Created Date: 2022-09-11
Qn: You are given two integers n and k and two integer arrays speed and
    efficiency both of length n. There are n engineers numbered from 1 to n.
    speed[i] and efficiency[i] represent the speed and efficiency of the ith
    engineer respectively.

    Choose at most k different engineers out of the n engineers to form a team with
    the maximum performance.

    The performance of a team is the sum of their engineers' speeds multiplied by
    the minimum efficiency among their engineers.

    Return the maximum performance of this team. Since the answer can be a huge
    number, return it modulo 10^9 + 7.
Link: https://leetcode.com/problems/maximum-performance-of-a-team/
Notes:
    - sort in descending order of efficiency
    - store the speed in min heap and pop to keep the len below or equal to k
    - return the max performance speed * eff
'''
import heapq

def maxPerformance(n: int, speed: list[int], efficiency: list[int], k: int) -> int:
    eng = [ [eff, spd] for eff, spd in zip(efficiency, speed) ]
    eng.sort(reverse=True)

    result = cum_speed = 0

    min_heap = []
    for eff, spd in eng:
        if len(min_heap) == k: cum_speed -= heapq.heappop(min_heap)
        cum_speed += spd
        heapq.heappush(min_heap, spd)
        result = max(result, eff * cum_speed)
    return result % (10**9 + 7)

if __name__ == '__main__':
    n1, k1, s1, e1 = 6, 2, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2]
    n2, k2, s2, e2 = 6, 3, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2]
    n3, k3, s3, e3 = 6, 4, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2]

    print(maxPerformance(n1, s1, e1, k1))
    print(maxPerformance(n2, s2, e2, k2))
    print(maxPerformance(n3, s3, e3, k3))
