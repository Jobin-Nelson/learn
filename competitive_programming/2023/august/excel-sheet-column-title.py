'''
Created Date: 2023-08-22
Qn: Given an integer columnNumber, return its corresponding column title as it
    appears in an Excel sheet.
Link: https://leetcode.com/problems/excel-sheet-column-title/
Notes:
    - use base 26 number system
    - since A starts at 1 and not 0 we need to subtract 1
'''
def convertToTitle(columnNumber: int) -> str:
    res = []
    while columnNumber:
        columnNumber, remainder = divmod(columnNumber-1, 26)
        res.append(chr(ord('A') + remainder))
    return ''.join(res[::-1])

if __name__ == '__main__':
    c1 = 1
    c2 = 28
    c3 = 701

    print(convertToTitle(c1))
    print(convertToTitle(c2))
    print(convertToTitle(c3))
