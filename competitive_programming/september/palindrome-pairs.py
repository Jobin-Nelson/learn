'''
Created Date: 2022-09-17
Qn: Given a list of unique words, return all the pairs of the distinct indices
    (i, j) in the given list, so that the concatenation of the two words words[i] +
    words[j] is a palindrome.
Link: https://leetcode.com/problems/palindrome-pairs/
Notes:
    - lookup table
    - handle three case, empty, reverse and substring palindrome
'''
def palindromePairs(words: list[str]) -> list[list[int]]:
    N = len(words)
    result = []
    lookup = {w: i for i, w in enumerate(words)}

    for i in range(N):
        w = words[i]
        if w == "":
            for j in range(N):
                if i!=j and is_palindrome(words[j]):
                    result.append([i, j])
                    result.append([j, i])

        rw = w[::-1]
        if rw in lookup and lookup[rw] != i:
            result.append([i, lookup[rw]])

        for k in range(1, len(w)):
            if is_palindrome(w[:k]) and w[k:][::-1] in lookup:
                result.append([lookup[w[k:][::-1]], i])
            if is_palindrome(w[k:]) and w[:k][::-1] in lookup:
                result.append([i, lookup[w[:k][::-1]]])

    return result

def is_palindrome(w: str) -> bool:
    l, r = 0, len(w)-1

    while l < r:
        if w[l] != w[r]: return False
        l += 1
        r -= 1
    return True


if __name__ == '__main__':
    w1 = ["abcd", "dcba", "lls", "s", "sssll"]
    w2 = ["bat", "tab", "cat"]
    w3 = ["a", ""]

    print(palindromePairs(w1))
    print(palindromePairs(w2))
    print(palindromePairs(w3))
