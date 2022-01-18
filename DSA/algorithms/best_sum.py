# Write a function best_sum(targetSum, numbers)
# The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum

def best_sum(target_sum, numbers, memo=None):
    if memo==None:
        memo = dict()
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = best_sum(remainder, numbers, memo)
        if remainder_result != None:
            combination = [*remainder_result, num]
            if shortest_combination==None or len(combination)<len(shortest_combination):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return memo[target_sum]


if __name__ == '__main__':
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(8, [5, 4, 5]))
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(100, [1, 2, 5, 25]))

