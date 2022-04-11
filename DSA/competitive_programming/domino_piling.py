def solve(m, n):
    area = m * n
    print(area // 2)

def main():
    m, n = list(map(int, input().split()))
    solve(m, n)

if __name__ == '__main__':
    main()