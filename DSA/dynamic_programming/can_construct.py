# Write a function canConstruct(target, wordBank)
# The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the wordBank array
# You may reuse elements of the wordBank as many times as necessary

def can_construct(target, word_bank, memo=None):
    if memo==None:
        memo = dict()
    if target in memo:
        return memo[target]
    if target == '':
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False

# tabulation
def can_construct_tab(target, word_bank):
    target_len = len(target)
    dp = [False] * (target_len + 1)
    dp[0] = True

    for i in range(target_len + 1):
        if dp[i]:
            for word in word_bank:
                word_len = len(word)
                if ((i+word_len) <= target_len) and (target[i:i+word_len] == word):
                    dp[i+word_len] = True

    return dp[target_len]

if __name__ == '__main__':
    print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot','o', 't']))
    print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
    print()
    print(can_construct_tab('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(can_construct_tab('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(can_construct_tab('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot','o', 't']))
    print(can_construct_tab('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
