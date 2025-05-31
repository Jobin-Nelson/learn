from functools import reduce


def rob(nums: list[int]) -> int:
    # functional
    return reduce(lambda x, y: (x[1], max(x[0] + y, x[1])), nums, (0, 0))[1]

    # imperative
    # r1, r2 = 0, 0
    # for n in nums:
    #     r1, r2 = r2, max(r2, n + r1)
    # return r2


if __name__ == "__main__":
    n1 = [1, 1, 3, 3]
    n2 = [2, 9, 8, 3, 6]

    print(rob(n1))
    print(rob(n2))
