'''
Created Date: 2023-10-31
Qn: You are given an integer array pref of size n. Find and return the array
    arr of size n that satisfies:

        - pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].

    Note that ^ denotes the bitwise-xor operation.

    It can be proven that the answer is unique.
Link: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
Notes:
    - use xor property of a ^ a = 0 to find the shortcut pref[i] = pref[i] ^ pref[i-1]
'''
def findArray(pref: list[int]) -> list[int]:
    if not pref: return []
    for i in range(len(pref)-1, 0, -1):
        pref[i] ^= pref[i-1]
    return pref

if __name__ == '__main__':
    p1 = [5,2,0,3,1]
    p2 = [13]

    print(findArray(p1))
    print(findArray(p2))
