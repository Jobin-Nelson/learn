'''
Created Date: 2023-03-02
Qn: Given an array of characters chars, compress it using the following
    algorithm:

    Begin with an empty string s. For each group of consecutive repeating
    characters in chars:

        - If the group's length is 1, append the character to s. 
        - Otherwise, append the character followed by the group's length.

    The compressed string s should not be returned separately, but instead, be
    stored in the input character array chars. Note that group lengths that are
    10 or longer will be split into multiple characters in chars.

    After you are done modifying the input array, return the new length of the
    array.

    You must write an algorithm that uses only constant extra space.
Link: https://leetcode.com/problems/string-compression/
Notes:
    - use two pointers
'''
def compress(chars: list[str]) -> int:
    N = len(chars)
    if N == 1: return 1
    i = j = 0

    while i < N:
        count = 1
        while i < N-1 and chars[i] == chars[i+1]:
            count += 1
            i += 1
        chars[j] = chars[i]
        j += 1
        if count > 1:
            for c in str(count):
                chars[j] = c
                j += 1
        i += 1
    return j
    

if __name__ == '__main__':
    c1 = ["a","a","b","b","c","c","c"]
    c2 = ["a"]
    c3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

    print(compress(c1))
    print(compress(c2))
    print(compress(c3))
