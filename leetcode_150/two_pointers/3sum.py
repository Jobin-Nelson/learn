def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if a > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum < 0:
                l += 1
            elif three_sum > 0:
                r -= 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


if __name__ == "__main__":
    n1 = [-1, 0, 1, 2, -1, -4]
    n2 = [0, 1, 1]
    n3 = [0] * 3

    print(threeSum(n1))
    print(threeSum(n2))
    print(threeSum(n3))
