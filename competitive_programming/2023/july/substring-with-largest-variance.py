'''
Created Date: 2023-07-09
Qn: The variance of a string is defined as the largest difference between the
    number of occurrences of any 2 characters present in the string. Note the
    two characters may or may not be the same.

    Given a string s consisting of lowercase English letters only, return the
    largest variance possible among all substrings of s.

    A substring is a contiguous sequence of characters within a string.
Link: https://leetcode.com/problems/substring-with-largest-variance/
Notes:
    - use modified kadane's algorithm
'''
def largestVariance(s: str) -> int:
    N = 26
    counter = [0] * N
    for c in s:
        counter[ord(c) - ord('a')] += 1

    res = 0

    for i in range(N):
        for j in range(N):
            if i == j or counter[i] == 0 or counter[j] == 0: continue
            major = chr(ord('a') + i)
            minor = chr(ord('a') + j)

            major_count = 0
            minor_count = 0
            rest_minor = counter[j]

            for c in s:
                if c == major:
                    major_count += 1
                if c == minor:
                    minor_count += 1
                    rest_minor -= 1
                if minor_count > 0:
                    res = max(res, major_count - minor_count)

                if major_count < minor_count and rest_minor > 0:
                    major_count = 0
                    minor_count = 0
    return res

if __name__ == '__main__':
    s1 = "aababbb"
    s2 = "abcde"

    print(largestVariance(s1))
    print(largestVariance(s2))
