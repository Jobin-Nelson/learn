'''
Created Date: 2023-07-02
Qn: We have n buildings numbered from 0 to n - 1. Each building has a number of
    employees. It's transfer season, and some employees want to change the
    building they reside in.

    You are given an array requests where requests[i] = [fromi, toi] represents
    an employee's request to transfer from building fromi to building toi.

    All buildings are full, so a list of requests is achievable only if for
    each building, the net change in employee transfers is zero. This means the
    number of employees leaving is equal to the number of employees moving in.
    For example if n = 3 and two employees are leaving building 0, one is
    leaving building 1, and one is leaving building 2, there should be two
    employees moving to building 0, one employee moving to building 1, and one
    employee moving to building 2.

    Return the maximum number of achievable requests.
Link: https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/
Notes:
    - use bit mask
'''
def maximumRequests(n: int, requests: list[list[int]]) -> int:
    res = 0
    N = len(requests)

    for mask in range(1 << N):
        bit_count = mask.bit_count()
        if bit_count <= res: continue

        pos = N - 1
        indegree = [0] * n
        while mask > 0:
            if mask & 1:
                indegree[requests[pos][0]] -= 1
                indegree[requests[pos][1]] += 1
            mask >>= 1
            pos -= 1
        if all(b == 0 for b in indegree):
            res = max(res, bit_count)
    return res

if __name__ == '__main__':
    n1, r1 = 5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
    n2, r2 = 3, [[0,0],[1,2],[2,1]]
    n3, r3 = 4, [[0,3],[3,1],[1,2],[2,0]]

    print(maximumRequests(n1, r1))
    print(maximumRequests(n2, r2))
    print(maximumRequests(n3, r3))
