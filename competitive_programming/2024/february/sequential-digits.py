"""
Created Date: 2024-02-02
Qn: An integer has sequential digits if and only if each digit in the number is
    one more than the previous digit.

    Return a sorted list of all the integers in the range [low, high] inclusive
    that have sequential digits.
Link: https://leetcode.com/problems/sequential-digits/
Notes:
    - use queue to hold all valid numbers
"""
from collections import deque

def sequentialDigits(low: int, high: int) -> list[int]:
    # Queue approach
    q = deque(range(1, 10))

    res = []
    while q:
        n = q.popleft()
        if n > high: continue
        if low <= n <= high:
            res.append(n)
        last_digit = n % 10
        if last_digit < 9:
            q.append(n * 10 + (last_digit + 1))
    return res
    

    # O(1)
    # low_digit, high_digit = int(math.log10(low) + 1), int(math.log10(high) + 1)
    #
    # res = []
    # for digits in range(low_digit, high_digit+1):
    #     for start in range(1, 9):
    #         if start + digits > 10: break
    #         prev = num = start
    #
    #         for _ in range(digits-1):
    #             num *= 10
    #             prev += 1
    #             num += prev
    #         if low <= num <= high:
    #             res.append(num)
    # return res

    # slow sliding window
    # all = ''.join(map(str, range(1, 10)))
    # res = []
    # l = r = 0
    # while int(all[:r+1]) <= high:
    #     cur = int(all[:r+1])
    #     if cur < low:
    #         r += 1
    #         continue
    #
    #     l = 0
    #     for i in range(r, len(all)):
    #         cur = int(all[l:i+1])
    #         if cur > high: break
    #         res.append(cur)
    #         l += 1
    #     r += 1
    # return res

if __name__ == '__main__':
    l1, h1 = 100, 300
    l2, h2 = 1000, 13000


    print(sequentialDigits(l1, h1))
    print(sequentialDigits(l2, h2))
