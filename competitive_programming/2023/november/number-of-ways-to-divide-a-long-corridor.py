"""
Created Date: 2023-11-28
Qn: Along a long library corridor, there is a line of seats and decorative
    plants. You are given a 0-indexed string corridor of length n consisting of
    letters 'S' and 'P' where each 'S' represents a seat and each 'P'
    represents a plant.

    One room divider has already been installed to the left of index 0, and
    another to the right of index n - 1. Additional room dividers can be
    installed. For each position between indices i - 1 and i (1 <= i <= n - 1),
    at most one divider can be installed.

    Divide the corridor into non-overlapping sections, where each section has
    exactly two seats with any number of plants. There may be multiple ways to
    perform the division. Two ways are different if there is a position with a
    room divider installed in the first way but not in the second way.

    Return the number of ways to divide the corridor. Since the answer may be
    very large, return it modulo 109 + 7. If there is no way, return 0.
Link: https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
Notes:
    - use combinatorics
"""
def numberOfWays(corridor: str) -> int:
    MOD = 1_000_000_007
    count = 1
    seats = 0
    previous_pair_last = None
    for index, thing in enumerate(corridor):
        if thing == "S":
            seats += 1

            if seats == 2:
                previous_pair_last = index
                seats = 0
            
            elif seats == 1 and previous_pair_last is not None:
                count *= (index - previous_pair_last)
                count %= MOD
    if seats == 1 or previous_pair_last is None:
        return 0

    return count

if __name__ == '__main__':
    c1 = "SSPPSPS"
    c2 = "PPSPSP"
    c3 = "S"

    print(numberOfWays(c1))
    print(numberOfWays(c2))
    print(numberOfWays(c3))
