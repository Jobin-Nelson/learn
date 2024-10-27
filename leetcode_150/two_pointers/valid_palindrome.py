def isPalindrome(s: str) -> bool:
    sn = [c.lower() for c in s if c.isalnum()]
    N = len(sn)
    for i in range(N):
        si = N - i - 1
        if sn[i] != sn[si]:
            return False
    return True

if __name__ == "__main__":
    s1 = "Was it a car or a cat I saw?"
    s2 = "tab a cat"
    print(isPalindrome(s1))
    print(isPalindrome(s2))
