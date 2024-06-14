"""
Created Date: 2024-06-02
Qn: Write a function that reverses a string. The input string is given as an
    array of characters s.

    You must do this by modifying the input array in-place with O(1) extra
    memory.
Link: https://leetcode.com/problems/reverse-string/
Notes:
"""
def reverseString(s: list[str]) -> None:
    N = len(s)
    for i in range(N >> 1):
        s[i], s[N-1-i] = s[N-1-i], s[i]

if __name__ == '__main__':
    s1 = list("hello")
    s2 = list("Hannah")

    reverseString(s1)
    reverseString(s2)

    print(s1)
    print(s2)
