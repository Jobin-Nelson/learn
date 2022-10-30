'''
Created Date: 2022-10-27
Qn: You are given two images, img1 and img2, represented as binary, square
    matrices of size n x n. A binary matrix has only 0s and 1s as values.

    We translate one image however we choose by sliding all the 1 bits left,
    right, up, and/or down any number of units. We then place it on top of the
    other image. We can then calculate the overlap by counting the number of
    positions that have a 1 in both images.

    Note also that a translation does not include any kind of rotation. Any 1
    bits that are translated outside of the matrix borders are erased.

    Return the largest possible overlap.
Link: https://leetcode.com/problems/image-overlap/
Notes:
    - keep one static and rotate the other image
    - check the bounds and compare the values
'''
def largestOverlap(img1: list[list[int]], img2: list[list[int]]) -> int:
    N = len(img1)
    def check_shift(x_shift: int, y_shift: int) -> int:
        count = 0

        for r in range(N):
            for c in range(N):
                if 0<=r+y_shift<N and 0<=c+x_shift<N and img1[r+y_shift][c+x_shift] == 1 and img2[r][c] == 1:
                    count += 1
        return count
    return max(check_shift(x, y) for x in range(-N, N) for y in range(-N, N))

if __name__ == '__main__':
    img11, img12 = [[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]
    img21, img22 = [[1]], [[1]]
    img31, img32 = [[0]], [[0]]

    print(largestOverlap(img11, img12))
    print(largestOverlap(img21, img22))
    print(largestOverlap(img31, img32))
