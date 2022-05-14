# check if two strings are anagrams

# first way
def are_anagrams(s1, s2):
    if len(s1)!=len(s2):
        return False

    freq1 = {}
    freq2 = {}

    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    return freq1 == freq2

# second way
from collections import Counter
def counter_anagrams(s1, s2):
    if len(s1)!=len(s2):
        return False
    return Counter(s1) == Counter(s2)

# third way
def sort_anagram(s1, s2):
    if len(s1)!=len(s2):
        return False
    return sorted(s1)==sorted(s2)
