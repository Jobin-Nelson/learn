'''
Created Date: 2023-08-31
qn: there is a one-dimensional garden on the x-axis. the garden starts at the
    point 0 and ends at the point n. (i.e the length of the garden is n).

    there are n + 1 taps located at points [0, 1, ..., n] in the garden.

    given an integer n and an integer array ranges of length n + 1 where
    ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i],
    i + ranges[i]] if it was open.

    return the minimum number of taps that should be open to water the whole
    garden, if the garden cannot be watered return -1.
Link: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
Notes:
    - use greedy dp
'''
def minTaps(n: int, ranges: list[int]) -> int:
    max_reach = [0] * (n+1)

    for i in range(len(ranges)):
        start = max(0, i-ranges[i])
        end = min(n, i+ranges[i])
        max_reach[start] = max(max_reach[start], end)

    taps = cur_end = next_end = 0
    for i in range(n+1):
        if i > next_end: return -1
        if i > cur_end:
            taps += 1
            cur_end = next_end
        next_end = max(next_end, max_reach[i])
    return taps

if __name__ == '__main__':
    n1, r1 = 5, [3,4,1,1,0,0]
    n2, r2 = 3, [0,0,0,0]

    print(minTaps(n1, r1))
    print(minTaps(n2, r2))
