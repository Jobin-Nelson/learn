def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    scount = [0] * 26
    tcount = [0] * 26
    ord_a = ord('a')
    for cs, ct in zip(s, t):
        scount[ord(cs) - ord_a] += 1
        tcount[ord(ct) - ord_a] += 1
    return scount == tcount

