'''
Qn: 
- How many measurements are larger than the previous measurement?
- Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
Link: https://adventofcode.com/2021/day/1
ans: 1711, 1743
'''
def main() -> int:
    with open('input1.txt') as f:
        input = f.readlines()

    input = list(map(int, input))
    ans1 = sum(input[i-1] < input[i] for i in range(1, len(input)))
    ans2 = sum(input[i-3] < input[i] for i in range(1, len(input)))
    print(ans1, ans2)
    
    return ans1, ans2

if __name__ == '__main__':
    print(main())
