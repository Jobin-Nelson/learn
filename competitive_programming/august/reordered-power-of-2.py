'''
Created Date: 2022-08-26
Qn: You are given an integer n. We reorder the digits in any order (including
    the original order) such that the leading digit is not zero.
    Return true if and only if we can do this so that the resulting number is a
    power of two.
Link: https://leetcode.com/problems/reordered-power-of-2/
Notes:
- There are lesser number of power of 2's than going through every permutation
  of a given number
- Check the counter of each 2's power with the given number's counter
'''
from collections import Counter

def reorderedPowerOf2(n: int) -> bool:
    c = Counter([ int(i) for i in str(n) ])

    x, y = 0, 0
    while x <= 10**9:
        x = 2**y
        s = Counter([ int(i) for i in str(x) ])
        if s == c: return True
        y += 1
    return False

if __name__ == '__main__':
    n1, n2, n3, n4 = 1, 10, 16, 24
    print(reorderedPowerOf2(n1))
    print(reorderedPowerOf2(n2))
    print(reorderedPowerOf2(n3))
    print(reorderedPowerOf2(n4))
