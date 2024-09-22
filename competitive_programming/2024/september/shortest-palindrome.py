"""
Created Date: 2024-09-20
Qn: You are given a string s. You can convert s to a palindrome by adding
    characters in front of it.

    Return the shortest palindrome you can find by performing this
    transformation.
Link: https://leetcode.com/problems/shortest-palindrome/
Notes:
    - use robin karp algo
    - convert substrings into integers (encode)
    - comparing integers is O(1) vs strings O(n)
"""


def shortestPalindrome(s: str) -> str:
    ord_a = ord('a')
    forward_hash = 0
    reverse_hash = 0
    mod_value = 10**9 + 7
    power_value = 1
    base = 29
    palindrome_end_index = -1

    for i, c in enumerate(s):
        ord_val = ord(c) - ord_a + 1
        forward_hash = (forward_hash * base + ord_val) % mod_value
        reverse_hash = (reverse_hash + ord_val * power_value) % mod_value
        power_value = (power_value * base) % mod_value
        if forward_hash == reverse_hash:
            palindrome_end_index = i

    suffix = s[palindrome_end_index + 1 :]
    reversed_suffix = suffix[::-1]
    return reversed_suffix + s


if __name__ == '__main__':
    s1 = "aacecaaa"
    s2 = "abcd"

    print(shortestPalindrome(s1))
    print(shortestPalindrome(s2))
