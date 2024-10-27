def hasDuplicate(nums: list[int]) -> bool:
    nums_set = set()
    for n in nums:
        if n in nums_set:
            return True
        nums_set.add(n)
    return False

