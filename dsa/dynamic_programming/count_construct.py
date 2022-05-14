# Write a function canConstruct(target, wordBank)
# The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the wordBank array
# You may reuse elements of the wordBank as many times as necessary

def count_construct(target, word_bank, memo=None):
    if memo == None:
        memo = dict()
    if target in memo:
        return memo[target]
    if target == '':
        return 1

    total_ways = 0

    for word in word_bank:
        if target.startswith(word):
            total_ways += count_construct(target[len(word):], word_bank, memo)

    memo[target] = total_ways
    return total_ways

# tabulation
def count_construct_tab(target, word_bank):
    target_len = len(target)
    dp = [0] * (target_len + 1)
    dp[0] = 1

    for i in range(target_len + 1):
        if dp[i]:
            for word in word_bank:
                word_len = len(word)
                if ((i+word_len) <= target_len) and (target[i:i+word_len] == word):
                    dp[i+word_len] += dp[i]

    return dp[target_len]

if __name__ == '__main__':
    print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot','o', 't']))
    print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))

    print(count_construct_tab('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(count_construct_tab('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(count_construct_tab('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(count_construct_tab('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot','o', 't']))
    print(count_construct_tab('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
