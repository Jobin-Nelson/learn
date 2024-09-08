"""
Created Date: 2024-09-05
Qn: You have observations of n + m 6-sided dice rolls with each face numbered
    from 1 to 6. n of the observations went missing, and you only have the
    observations of m rolls. Fortunately, you have also calculated the average
    value of the n + m rolls.

    You are given an integer array rolls of length m where rolls[i] is the
    value of the ith observation. You are also given the two integers mean and
    n.

    Return an array of length n containing the missing observations such that
    the average value of the n + m rolls is exactly mean. If there are multiple
    valid answers, return any of them. If no such array exists, return an empty
    array.

    The average value of a set of k numbers is the sum of the numbers divided
    by k.

    Note that mean is an integer, so the sum of the n + m rolls should be
    divisible by n + m.
Link: https://leetcode.com/problems/find-missing-observations/
Notes:
    - use simulation
"""


def missingRolls(rolls: list[int], mean: int, n: int) -> list[int]:
    m = len(rolls)
    sum_n = mean * (m + n) - sum(rolls)
    if sum_n < n or sum_n > (n * 6):
        return []
    mean_n, mod_n = divmod(sum_n, n)
    res = [mean_n] * n
    for i in range(mod_n):
        res[i] += 1
    return res


if __name__ == '__main__':
    r1, m1, n1 = [3, 2, 4, 3], 4, 2
    r2, m2, n2 = [1, 5, 6], 3, 4
    r3, m3, n3 = list(range(1, 5)), 6, 4

    print(missingRolls(r1, m1, n1))
    print(missingRolls(r2, m2, n2))
    print(missingRolls(r3, m3, n3))
