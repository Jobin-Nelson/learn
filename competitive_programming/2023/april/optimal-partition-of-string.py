'''
Created Date: 2023-04-04
Qn: Given a string s, partition the string into one or more substrings such
    that the characters in each substring are unique. That is, no letter
    appears in a single substring more than once.

    Return the minimum number of substrings in such a partition.

    Note that each character should belong to exactly one substring in a
    partition.
Link: https://leetcode.com/problems/optimal-partition-of-string/
Notes:
    - use list or map or bits to store the last index of partition
    - if you encounter an element reset the map and update the last index
'''
def partitionString(s: str) -> int:
    # Using list
    # last_pos = [0] * 26
    # last_end = 0
    # partitions = 0
    #
    # for i in range(len(s)):
    #     if last_pos[ord(s[i]) - ord('a')] >= last_end:
    #         partitions += 1
    #         last_end = i
    #     last_pos[ord(s[i]) - ord('a')] = i
    # return partitions
    
    # Bit manipulation
    xor = 0
    res = 1

    for c in s:
        if xor & (1 << (ord(c) - ord('a'))):
            xor = 0
            res += 1
        xor ^= (1 << (ord(c) - ord('a')))
    return res

if __name__ == '__main__':
    s1 = "abacaba"
    s2 = "ssssss"

    print(partitionString(s1))
    print(partitionString(s2))
