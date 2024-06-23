"""
Created Date: 2024-06-21
Qn: There is a bookstore owner that has a store open for n minutes. Every
    minute, some number of customers enter the store. You are given an integer
    array customers of length n where customers[i] is the number of the
    customer that enters the store at the start of the ith minute and all those
    customers leave after the end of that minute.

    On some minutes, the bookstore owner is grumpy. You are given a binary
    array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during
    the ith minute, and is 0 otherwise.

    When the bookstore owner is grumpy, the customers of that minute are not
    satisfied, otherwise, they are satisfied.

    The bookstore owner knows a secret technique to keep themselves not grumpy
    for minutes consecutive minutes, but can only use it once.

    Return the maximum number of customers that can be satisfied throughout the
    day.
Link: https://leetcode.com/problems/grumpy-bookstore-owner/
Notes:
    - use sliding window
"""
def maxSatisfied(customers: list[int], grumpy: list[int], minutes: int) -> int:
    l = 0
    window, max_window = 0, 0
    satisfied = 0

    for r in range(len(customers)):
        if grumpy[r]:
            window += customers[r]
        else:
            satisfied += customers[r]
        if r-l+1 > minutes:
            if grumpy[l]:
                window -= customers[l]
            l += 1
        max_window = max(max_window, window)
    return satisfied + max_window

if __name__ == '__main__':
    c1, g1, m1 = [1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3
    c2, g2, m2 = [1], [0], 1

    print(maxSatisfied(c1, g1, m1))
    print(maxSatisfied(c2, g2, m2))
