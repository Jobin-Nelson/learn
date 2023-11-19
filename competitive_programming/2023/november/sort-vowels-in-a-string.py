"""
Created Date: 2023-11-13
Qn: Given a 0-indexed string s, permute s to get a new string t such that:

        - All consonants remain in their original places. More formally, if
          there is an index i with 0 <= i < s.length such that s[i] is a
          consonant, then t[i] = s[i]. 
        - The vowels must be sorted in the nondecreasing order of their ASCII
          values. More formally, for pairs of indices i, j with 0 <= i < j <
          s.length such that s[i] and s[j] are vowels, then t[i] must not have
          a higher ASCII value than t[j].

    Return the resulting string.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in
    lowercase or uppercase. Consonants comprise all letters that are not
    vowels.
Link: https://leetcode.com/problems/sort-vowels-in-a-string/
Notes:
    - use hashmap
"""


def sortVowels(s: str) -> str:
    v = ["a", "e", "i", "o", "u"]
    v = [*[vowel.upper() for vowel in v], *v]
    v_count = {s: 0 for s in v}
    for c in s:
        if c in v_count:
            v_count[c] += 1
    res = []
    cur_vow_ind = 0
    for c in s:
        if c not in v_count:
            res.append(c)
            continue

        vowel = v[cur_vow_ind]
        while v_count[vowel] == 0:
            cur_vow_ind += 1
            vowel = v[cur_vow_ind]
        res.append(vowel)
        v_count[vowel] -= 1
    return "".join(res)

if __name__ == "__main__":
    s1 = "lEetcOde"
    s2 = "lYmpH"

    print(sortVowels(s1))
    print(sortVowels(s2))
