'''
Created Date: 2023-02-13
Qn: Given two non-negative integers low and high. Return the count of odd
    numbers between low and high (inclusive).
Link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
Notes:
    - use math
    - half of difference + 1
'''
def countOdds(low: int, high: int) -> int:
    if (low & 1) == 0: low += 1

    return (high - low) // 2 + 1 if low < high else 0

if __name__ == '__main__':
    l1, h1 = 3, 7
    l2, h2 = 8, 10

    print(countOdds(l1, h1))
    print(countOdds(l2, h2))
