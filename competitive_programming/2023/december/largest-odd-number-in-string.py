"""
Created Date: 2023-12-07
Qn: You are given a string num, representing a large integer. Return the
    largest-valued odd integer (as a string) that is a non-empty substring of
    num, or an empty string "" if no odd integer exists.

    A substring is a contiguous sequence of characters within a string.
Link: https://leetcode.com/problems/largest-odd-number-in-string/
Notes:
    - find the right most odd digit
"""
def largestOddNumber(num: str) -> str:
    return num[:max(num.rfind(i) for i in '13579')+1]

    # res = ''
    # for i, d in enumerate(map(int, num)):
    #     if d & 1:
    #         res = num[:i+1]
    # return res

if __name__ == '__main__':
    n1 = "52"
    n2 = "4206"
    n3 = "35427"

    print(largestOddNumber(n1))
    print(largestOddNumber(n2))
    print(largestOddNumber(n3))
