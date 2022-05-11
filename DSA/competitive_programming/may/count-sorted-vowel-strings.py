'''
Qn: Given an integer n, return the number of strings of length n 
    that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
Link: https://leetcode.com/problems/count-sorted-vowel-strings/
Notes:
- recursively add values till n hits zero
'''
def countVowelStrings(n: int) -> int:
    def rec(n, k):
        if n == 0:
            return 1
        total = 0
        for i in range(k, 5):
            total += rec(n-1, i)

        return total
    return rec(n, 0)

if __name__ == '__main__':
    n1, n2, n3 = 1, 2, 33
    print(countVowelStrings(n1))
    print(countVowelStrings(n2))
    print(countVowelStrings(n3))
