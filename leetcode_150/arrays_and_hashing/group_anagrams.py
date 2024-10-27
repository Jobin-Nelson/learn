from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    ord_a = ord('a')
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord_a] += 1
        res[tuple(count)].append(s)
    return res.values()
