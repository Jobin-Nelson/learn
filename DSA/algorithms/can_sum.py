# can sum with repetition
def can_sum(arr, target, memo=None):
    if memo == None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for n in arr:
        remainder = target - n

        if can_sum(arr, remainder, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


if __name__ == '__main__':
    print(can_sum([2, 3], 7))
    print(can_sum([5, 3, 4, 7], 7))
    print(can_sum([2, 4], 7))
    print(can_sum([2, 3, 5], 7))
