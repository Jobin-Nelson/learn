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

def best_sum_tab(target_sum, numbers):
    dp = [None for i in range(target_sum+1)]
    dp[0] = []

    for i in range(target_sum+1):
        if dp[i] != None:
            for num in numbers:
                if (i+num <= target_sum):
                    combination = [*dp[i], num]

                    if (dp[i+num] == None) or (len(combination) < len(dp[i+num])):
                        dp[i+num] = [*dp[i], num]

    return dp[target_sum]

if __name__ == '__main__':
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(8, [5, 4, 5]))
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(100, [1, 2, 5, 25]))

    print(best_sum_tab(7, [5, 3, 4, 7]))
    print(best_sum_tab(8, [2, 3, 5]))
    print(best_sum_tab(8, [5, 4, 5]))
    print(best_sum_tab(7, [5, 3, 4, 7]))
    print(best_sum_tab(100, [1, 2, 5, 25]))
