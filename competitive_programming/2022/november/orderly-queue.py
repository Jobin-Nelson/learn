'''
Created Date: 2022-11-06
Qn: You are given a string s and an integer k. You can choose one of the first
    k letters of s and append it at the end of the string..

    Return the lexicographically smallest string you could have after applying
    the mentioned step any number of moves.
Link: https://leetcode.com/problems/orderly-queue/
Notes:
'''
def orderelyQueue(s: str, k: int) -> str:
    if k > 1: return ''.join(sorted(s))
    return min(s[i:]+s[:i] for i in range(len(s)))

if __name__ == '__main__':
    s1, k1 = 'cba', 1
    s2, k2 = 'baaca', 3
    
    print(orderelyQueue(s1, k1))
    print(orderelyQueue(s2, k2))

