'''
Created Date: 2023-09-24
Qn: We stack glasses in a pyramid, where the first row has 1 glass, the second
    row has 2 glasses, and so on until the 100th row.  Each glass holds one cup
    of champagne.

    Then, some champagne is poured into the first glass at the top.  When the
    topmost glass is full, any excess liquid poured will fall equally to the
    glass immediately to the left and right of it.  When those glasses become
    full, any excess champagne will fall equally to the left and right of those
    glasses, and so on.  (A glass at the bottom row has its excess champagne
    fall on the floor.)

    For example, after one cup of champagne is poured, the top most glass is
    full. After two cups of champagne are poured, the two glasses on the second
    row are half full.  After three cups of champagne are poured, those two
    cups become full - there are 3 full glasses total now.  After four cups of
    champagne are poured, the third row has the middle glass half full, and the
    two outside glasses are a quarter full, as pictured below. Now after
    pouring some non-negative integer cups of champagne, return how full the
    jth glass in the ith row is (both i and j are 0-indexed.)
Link: https://leetcode.com/problems/champagne-tower/
Notes:
    - use simulation
'''
def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    prev_row = [poured]

    for row in range(1, query_row + 1):
        cur_row = [0] * (row + 1)
        for i in range(row):
            extra = prev_row[i] - 1
            if extra > 0:
                cur_row[i] += 0.5 * extra
                cur_row[i+1] += 0.5 * extra
        prev_row = cur_row
    return min(1, prev_row[query_glass])


if __name__ == '__main__':
    p1, qr1, qg1 = 1, 1, 1
    p2, qr2, qg2 = 2, 1, 1
    p3, qr3, qg3 = 100000009, 33, 17 

    print(champagneTower(p1, qr1, qg1))
    print(champagneTower(p2, qr2, qg2))
    print(champagneTower(p3, qr3, qg3))
