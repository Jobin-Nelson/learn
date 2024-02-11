"""
Created Date: 2024-02-07
Qn: Given a string s, sort it in decreasing order based on the frequency of the
    characters. The frequency of a character is the number of times it appears
    in the string.

    Return the sorted string. If there are multiple answers, return any of
    them.
Link: https://leetcode.com/problems/sort-characters-by-frequency/
Notes:
    - use bucket sort
"""
from collections import Counter, defaultdict

def frequencySort(s: str) -> str:
    count = Counter(s)
    buckets = defaultdict(list)

    for char, cnt in count.items():
        buckets[cnt].append(char)

    res = []
    for i in range(len(s), 0, -1):
        for c in buckets[i]:
            res.append(c * i)
    return ''.join(res)

    # return ''.join(v[0]*v[1] for v in Counter(s).most_common())

    # count = {}
    # for c in s:
    #     count[c] = count.get(c, 0) + 1
    # most_common = sorted(count.items(), key=lambda x: x[1], reverse=True)
    # return ''.join(v[0] * v[1] for v in most_common)

if __name__ == '__main__':
    s1 = "tree"
    s2 = "cccaaaa"
    s3 = "Aabb"

    print(frequencySort(s1))
    print(frequencySort(s2))
    print(frequencySort(s3))
