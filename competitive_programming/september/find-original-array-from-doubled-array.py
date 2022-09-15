'''
Created Date: 2022-09-15
Qn: An integer array original is transformed into a doubled array changed by
    appending twice the value of every element in original, and then randomly
    shuffling the resulting array.

    Given an array changed, return original if changed is a doubled array. If
    changed is not a doubled array, return an empty array. The elements in original
    may be returned in any order.
- something test
Link: https://leetcode.com/problems/find-original-array-from-doubled-array/
Notes:
    - return [] if len of given list is odd
    - hashmap to keep the count of each number
    - sort the given list
    - reduce the count when both n and n*2 are in the hashmap
    - handle special case of 0, because 0*2 is 0
    - return new list if the length is half of the given list else []
'''
from collections import Counter

def findOriginalArray(changed: list[int]) -> list[int]:
    N = len(changed)
    if N % 2: return []

    count = Counter(changed)
    changed.sort()
    ans = []

    for n in changed:
        if n == 0 and count[n] >= 2:
            count[n] -= 2
            ans.append(n)
        elif n > 0 and count[n] and count[n*2]:
            count[n] -= 1
            count[n*2] -= 1
            ans.append(n)
    return ans if len(ans) == N // 2 else []

if __name__ == '__main__':
    c1 = [1, 3, 4, 2, 6, 8]
    c2 = [6, 3, 0, 1]
    c3 = [1]

    print(findOriginalArray(c1))
    print(findOriginalArray(c2))
    print(findOriginalArray(c3))
