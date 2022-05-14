'''
Qn: Given a string s, find the length of the longest substring without repeating characters.
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Notes:
- sliding window, sliding when there is a duplicate
'''

def length_of_longest_substring(s):
    visited = set()
    l, r = 0, 0
    res = 0
    
    while r < len(s):
        while s[r] in visited:
            visited.remove(s[l])
            l += 1
        visited.add(s[r])
        res = max(res, r-l+1)
        r += 1
    return res

if __name__ == '__main__':
    s1, s2, s3 = "abcabcbb", "bbbbb", "pwwkew"
    print(length_of_longest_substring(s1))
    print(length_of_longest_substring(s2))
    print(length_of_longest_substring(s3))