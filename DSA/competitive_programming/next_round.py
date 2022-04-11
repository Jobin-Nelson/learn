from tkinter import W


def solve(k, scores):
    passed = list(filter(lambda x: x > 0, scores[:k+1]))
    print(len(passed))

def main():
    n, k = list(map(int, input().split()))
    scores = list(map(int, input().split()))
    print(scores)

    solve(k, scores)
    

if __name__ == '__main__':
    main()