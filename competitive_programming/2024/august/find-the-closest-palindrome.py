"""
Created Date: 2024-08-24
Qn: Given a string n representing an integer, return the closest integer (not
    including itself), which is a palindrome. If there is a tie, return the
    smaller one.

    The closest is defined as the absolute difference minimized between two
    integers.
Link: https://leetcode.com/problems/find-the-closest-palindrome/
Notes:
    - use binary search
"""


def nearestPalindrome(n: str) -> str:
    def convert(num: int) -> int:
        s = str(num)
        n = len(s)
        l, r = (n - 1) >> 1, n >> 1
        s_list = list(s)
        while l >= 0:
            s_list[r] = s_list[l]
            r += 1
            l -= 1
        return int(''.join(s_list))

    def next_palindrome(num: int) -> int:
        left, right = 0, num
        res = float('-inf')
        while left <= right:
            mid = left + ((right - left) >> 1)
            palin = convert(mid)
            if palin < num:
                res = palin
                left = mid + 1
            else:
                right = mid - 1
        return res

    def previous_palindrome(num: int) -> int:
        left, right = num, int(1e18)
        res = float('-inf')
        while left <= right:
            mid = left + ((right - left) >> 1)
            palin = convert(mid)
            if palin > num:
                res = palin
                right = mid - 1
            else:
                left = mid + 1
        return res

    num = int(n)
    a = next_palindrome(num)
    b = previous_palindrome(num)
    if abs(a - num) <= abs(b - num):
        return str(a)
    return str(b)


if __name__ == '__main__':
    n1 = "123"
    n2 = "1"

    print(nearestPalindrome(n1))
    print(nearestPalindrome(n2))
