def solve():
    s = list(map(int, input().split()))

    if (s[0] and s[1]) or (s[1] and s[2]) or (s[0] and s[2]):
        return True
    return False
            

def main():
    n = int(input())

    ans = 0
    for i in range(n):
        if solve():
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()