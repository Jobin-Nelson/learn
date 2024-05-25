"""
Created Date: 2024-05-09
Qn: You are given an array happiness of length n, and a positive integer k.

    There are n children standing in a queue, where the ith child has happiness
    value happiness[i]. You want to select k children from these n children in
    k turns.

    In each turn, when you select a child, the happiness value of all the
    children that have not been selected till now decreases by 1. Note that the
    happiness value cannot become negative and gets decremented only if it is
    positive.

    Return the maximum sum of the happiness values of the selected children you
    can achieve by selecting k children.
Link: https://leetcode.com/problems/maximize-happiness-of-selected-children/
Notes:
    - sort
"""
def maximumHappinessSum(happiness: list[int], k: int) -> int :
    return sum(max(h - i, 0) for i, h in enumerate(sorted(happiness, reverse=True)[:k]))

if __name__ == '__main__':
    h1, k1 = list(range(1, 4)), 2
    h2, k2 = [1] * 4, 2
    h3, k3 = list(range(2, 6)), 1
    h4, k4 = [12, 1, 42], 3

    print(maximumHappinessSum(h1, k1))
    print(maximumHappinessSum(h2, k2))
    print(maximumHappinessSum(h3, k3))
    print(maximumHappinessSum(h4, k4))
