'''
Created Date: 10-06-2022
Qn: Given a string , find the length of the longest substring without repeating 
    characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Notes:
- using sliding window, slide when there is a duplicate
'''
def lengthOflongestSubstring(s: str) -> int:
    visited = set()
    res, l, r = 0, 0, 0
    while r < len(s):
        while s[r] in visited:
            visited.remove(s[l])
            l += 1
        visited.add(s[r])
        res = max(res, r-l+1)
        r += 1
    return res

if __name__ == '__main__':
    s1, s2, s3 = 'abcabcbb', 'bbbbb', 'pwwkew'
    print(lengthOflongestSubstring(s1))
    print(lengthOflongestSubstring(s2))
    print(lengthOflongestSubstring(s3))
