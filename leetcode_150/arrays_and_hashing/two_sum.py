def twoSum(nums: list[int], target: int) -> list[int]:
    complement = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in complement:
            return [complement[comp], i]
        complement[n] = i
    return [-1,-1]
