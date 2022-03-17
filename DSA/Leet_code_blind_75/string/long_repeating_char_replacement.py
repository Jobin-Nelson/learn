'''
Qn: You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
Link: https://leetcode.com/problems/longest-repeating-character-replacement/
Notes:
'''

def character_replacement(s, k):
    count = {}
    l, r = 0, 0
    res = 0
    maxf = 0

    while r < len(s):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r-l+1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r-l+1)
        r += 1
    return res

if __name__ == '__main__':
    s1, k1 = "ABAB", 2
    s2, k2 = "AABABBA", 1
    print(character_replacement(s1, k1))
    print(character_replacement(s2, k2))