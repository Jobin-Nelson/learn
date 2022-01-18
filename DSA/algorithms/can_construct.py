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

if __name__ == '__main__':
    print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot','o', 't']))
    print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
