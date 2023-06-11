'''
Created Date: 2023-06-09
Qn: You are given an array of characters letters that is sorted in
    non-decreasing order, and a character target. There are at least two
    different characters in letters.

    Return the smallest character in letters that is lexicographically greater
    than target. If such a character does not exist, return the first character
    in letters.
Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
Notes:
    - use binary search
'''
def nextGreatestLetter(letters: list[str], target: str) -> str:
    l, r = 0, len(letters) -1

    while l <= r:
        m = l + ((r-l) >> 1)
        if target < letters[m]:
            if m > 0 and letters[m-1] <= target:
                return letters[m]
            r = m - 1
        else:
            l = m + 1
    return letters[0]
    # return letters[bisect_right(letters, target) % len(letters)]


if __name__ == '__main__':
    l1, t1 = ["c","f","j"], "a"
    l2, t2 = ["c","f","j"], "c"
    l3, t3 = ["x","x","y","y"], "z"

    print(nextGreatestLetter(l1, t1))
    print(nextGreatestLetter(l2, t2))
    print(nextGreatestLetter(l3, t3))
