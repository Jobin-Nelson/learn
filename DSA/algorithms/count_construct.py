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


if __name__ == '__main__':
    print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot','o', 't']))
    print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
