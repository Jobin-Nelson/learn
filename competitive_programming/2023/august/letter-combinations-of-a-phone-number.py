'''
Created Date: 2023-08-03
Qn: Given a string containing digits from 2-9 inclusive, return all possible
    letter combinations that the number could represent. Return the answer in
    any order.

    A mapping of digits to letters (just like on the telephone buttons) is
    given below. Note that 1 does not map to any letters.
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Notes:
    - use backtrack
'''
def letterCombinations(digits: str) -> list[str]:
    digit_to_char = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    res = []
    def backtrack(i: int, cur_str: str):
        if len(cur_str) == len(digits):
            res.append(cur_str)
            return
        for c in digit_to_char[ord(digits[i]) - ord('2')]:
            backtrack(i+1, cur_str + c)
    if digits: backtrack(0, '')
    return res

if __name__ == '__main__':
    d1 = "23"
    d2 = ""
    d3 = "2"

    print(letterCombinations(d1))
    print(letterCombinations(d2))
    print(letterCombinations(d3))
