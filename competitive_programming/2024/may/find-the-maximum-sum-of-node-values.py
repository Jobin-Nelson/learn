"""
Created Date: 2024-05-19
Qn: There exists an undirected tree with n nodes numbered 0 to n - 1. You are
    given a 0-indexed 2D integer array edges of length n - 1, where edges[i] =
    [ui, vi] indicates that there is an edge between nodes ui and vi in the
    tree. You are also given a positive integer k, and a 0-indexed array of
    non-negative integers nums of length n, where nums[i] represents the value
    of the node numbered i.

    Alice wants the sum of values of tree nodes to be maximum, for which Alice
    can perform the following operation any number of times (including zero) on
    the tree:

        - Choose any edge [u, v] connecting the nodes u and v, and update their
        values as follows:
            - nums[u] = nums[u] XOR k
            - nums[v] = nums[v] XOR k

    Return the maximum possible sum of the values Alice can achieve by
    performing the operation any number of times.
Link: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
Notes:
    - find delta and sort the array in reverse order
    - sum the even number of delta
"""
def maximumValueSum(nums: list[int], k: int, edges: list[list[int]]) -> int:
    delta = [(n^k)-n for n in nums]
    delta.sort(reverse=True)
    res = sum(nums)

    for i in range(0, len(nums)-1, 2):
        path_delta = delta[i] + delta[i+1]
        if path_delta <= 0: break
        res += path_delta
    return res

if __name__ == '__main__':
    n1, k1, e1 = [1,2,1], 3, [[0,1], [0,2]]
    n2, k2, e2 = [2,3], 7, [[0,1]]
    n3, k3, e3 = [7] * 6, 3, [[0, i] for i in range(1,6)]

    print(maximumValueSum(n1, k1, e1))
    print(maximumValueSum(n2, k2, e2))
    print(maximumValueSum(n3, k3, e3))
