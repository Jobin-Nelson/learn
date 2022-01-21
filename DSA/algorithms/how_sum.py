# Write a function howSum(target_sum, numbers)
# The function should return an array containing any combination of elements that add up to exactly the target_sum.
# If there is no combination that adds up to the target_sum, then return null.
# If there are multiple combinations possible, you may return any single one.

def how_sum(target_sum, numbers, memo=None):
    if memo == None:
        memo = dict()
    if target_sum in memo:
            return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers, memo)
        if remainder_result != None:
            memo[target_sum] = [*remainder_result, num]
            return memo[target_sum]

    memo[target_sum] = None
    return None

# tabulation
def how_sum_tab(target_sum, numbers):
    dp = [None for i in range(target_sum+1)]
    dp[0] = []

    for i in range(target_sum+1):
        if dp[i]!=None:
            for num in numbers:
                if ((i+num)<=target_sum):
                    dp[i+num] = [*dp[i], num]

    return dp[target_sum]

if __name__ == '__main__':
    print(how_sum(7, [2, 3]))
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(7, [2, 4]))
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(7, [2, 3]))

    print()

    print(how_sum_tab(7, [2, 3]))
    print(how_sum_tab(7, [5, 3, 4, 7]))
    print(how_sum_tab(7, [2, 4]))
    print(how_sum_tab(8, [2, 3, 5]))
    print(how_sum_tab(7, [2, 3]))
