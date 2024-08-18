"""
Created Date: 2024-08-07
Qn: Convert a non-negative integer num to its English words representation.
Link: https://leetcode.com/problems/integer-to-english-words/
Notes:
    - use map, divmod and iterate through each 3 digits
"""


def numberToWords(num: int) -> str:
    if num == 0:
        return 'Zero'
    ones_map = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
    }

    tens_map = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety',
    }

    def get_string(n: int) -> str:
        res = []
        hundreds = n // 100
        if hundreds:
            res.append(ones_map[hundreds] + ' Hundred')
        last_2_digits = n % 100
        if last_2_digits >= 20:
            tens, ones = divmod(last_2_digits, 10)
            res.append(tens_map[tens])
            if ones:
                res.append(ones_map[ones])
        elif last_2_digits:
            res.append(ones_map[last_2_digits])
        return ' '.join(res)

    postfix = ['', ' Thousand', ' Million', ' Billion']
    i = 0
    res = []
    while num:
        digits = num % 1000
        s = get_string(digits)
        if s:
            res.append(s + postfix[i])
        num //= 1000
        i += 1
    res.reverse()
    return ' '.join(res)


if __name__ == '__main__':
    n1 = 123
    n2 = 12345
    n3 = 1234567

    print(numberToWords(n1))
    print(numberToWords(n2))
    print(numberToWords(n3))
