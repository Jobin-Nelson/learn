'''
Qn: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Notes:
- backtrack recursively to to get all possible combinations
'''
def letterCombination(digits: str) -> list[str]:
    hashmap = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
            }
    res = []
    N = len(digits)
    def backtrack(i, cur_str):
        if len(cur_str) == N:
            res.append(cur_str)
            return
        for char in hashmap[digits[i]]:
            backtrack(i+1, cur_str + char)

    if digits:
        backtrack(0, '')
    return res

if __name__ == '__main__':
    d1 = '23'
    d2 = ''
    d3 = '2'
    print(letterCombination(d1))
    print(letterCombination(d2))
    print(letterCombination(d3))
