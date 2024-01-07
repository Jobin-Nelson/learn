"""
Created Date: 2024-01-03
Qn: Anti-theft security devices are activated inside a bank. You are given a
    0-indexed binary string array bank representing the floor plan of the bank,
    which is an m x n 2D matrix. bank[i] represents the ith row, consisting of
    '0's and '1's. '0' means the cell is empty, while'1' means the cell has a
    security device.

    There is one laser beam between any two security devices if both conditions
    are met:

        - The two devices are located on two different rows: r1 and r2, where
          r1 < r2. 
        - For each row i where r1 < i < r2, there are no security devices in
          the ith row.

    Laser beams are independent, i.e., one beam does not interfere nor join
    with another.

    Return the total number of laser beams in the bank.
Link: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
Notes:
    - use two variables cur and prev and multiply them together to the number
      of lasers
"""
def numberOfBeams(bank: list[str]) -> int:
    res =  prev_beams = 0
    for row in bank:
        cur_beams = row.count('1')
        if cur_beams == 0: continue
        res += (prev_beams * cur_beams)
        prev_beams = cur_beams
    return res

if __name__ == '__main__':
    b1 = ["011001","000000","010100","001000"]
    b2 = ["000","111","000"]

    print(numberOfBeams(b1))
    print(numberOfBeams(b2))
