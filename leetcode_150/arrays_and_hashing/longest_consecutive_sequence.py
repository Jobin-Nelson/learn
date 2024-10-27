def longestConsecutive(nums: list[int]) -> int:
    nset = set(nums)
    res = 0
    for n in nset:
        if n-1 in nset:
            continue
        length = 0
        while n+length in nset:
            length += 1
        res = max(res, length)
    return res

if __name__ == "__main__":
    n1 = [2,20,4,10,3,4,5]
    n2 = [0,3,2,5,4,6,1,1]

    print(longestConsecutive(n1))
    print(longestConsecutive(n2))

