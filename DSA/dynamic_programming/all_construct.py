# Write a function(target, wordBank)
# The function should return a 2D array containing all of the ways that the target can be constructed by concatenting elements of the wordBank array. Each element of the 2D array should represent one combination that constructs the target
# You may reuse the elements of wordBank as many times as necessary

def all_construct(target, word_bank, memo=None):
    if memo == None:
        memo = dict()
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):
            suffix_ways = all_construct(target[len(word):], word_bank, memo)
            target_ways = list(map(lambda x: [word, *x], suffix_ways))

            result.extend(target_ways)
            
    memo[target] = result
    return result

# tabulation
def all_construct_tab(target, word_bank):
    target_len = len(target)
    dp = [[] for i in range(target_len + 1)]
    dp[0] = [[]]

    for i in range(target_len + 1):
        if dp[i]:
            for word in word_bank:
                word_len = len(word)
                if target[i:i+word_len] == word:
                    combination = list(map(lambda x: [ *x, word], dp[i]))
                    dp[i + word_len].extend(combination)

    return dp[target_len]

if __name__ == '__main__':
    print(all_construct('purple', ['purp', 'p', 'purpl', 'le', 'ur', 'e']))
    print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
    print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aaa', 'aa', 'aaaa', 'aaaaa',]))
    
    print(all_construct_tab('purple', ['purp', 'p', 'purpl', 'le', 'ur', 'e']))
    print(all_construct_tab('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
    print(all_construct_tab('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
