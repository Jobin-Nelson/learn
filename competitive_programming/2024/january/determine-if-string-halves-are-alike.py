"""
Created Date: 2024-01-12
Qn: You are given a string s of even length. Split this string into two halves
    of equal lengths, and let a be the first half and b be the second half.

    Two strings are alike if they have the same number of vowels ('a', 'e',
    'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase
    and lowercase letters.

    Return true if a and b are alike. Otherwise, return false.
Link: https://leetcode.com/problems/determine-if-string-halves-are-alike/
Notes:
    - use set or better in this case since the number of elements to iterate
      over is less than 1000 use string or list
"""
def halvesAreAlike(s: str) -> bool:
    c1 = c2 = 0
    half = len(s) >> 1
    vowels = ['a', 'e', 'i', 'o', 'u']
    vs = set()
    for v in vowels:
        vs.add(v)
        vs.add(v.upper())

    for c in s[:half]:
        if c in vs: c1 += 1
    for c in s[half:]:
        if c in vs: c2 += 1
    return c1 == c2

    # c1, c2 = defaultdict(int), defaultdict(int)
    # half = len(s) >> 1
    # print(s[:half], s[half:])
    # for c in s[:half]: c1[c] += 1
    # for c in s[half:]: c2[c] += 1
    # vowels = ['a', 'e', 'i', 'o', 'u']
    # return all(c1[v] == c2[v] and c1[v.upper()] == c2[v.upper()] for v in vowels)
    

if __name__ == '__main__':
    s1 = "book"
    s2 = "textbook"
    s3 = "AbCdEfGh"

    print(halvesAreAlike(s1))
    print(halvesAreAlike(s2))
    print(halvesAreAlike(s3))
