def twoSum(numbers: list[int], target: int) -> list[int]:
    N = len(numbers)
    for i, n in enumerate(numbers):
        comp = target - n
        l, r = i+1, N-1
        while l <= r:
            m = l + ((r - l) >> 1)
            if numbers[m] < comp:
                l = m + 1
            elif numbers[m] > comp:
                r = m - 1
            else:
                return [i+1, m+1]


if __name__ == "__main__":
    n1, t1 = [1,2,3,4], 3
    n2, t2 = [-5,-3,0,2,4,6,8], 5
    print(twoSum(n1, t1))
    print(twoSum(n2, t2))
