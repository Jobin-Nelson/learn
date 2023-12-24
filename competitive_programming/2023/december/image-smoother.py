"""
Created Date: 2023-12-19
Qn: An image smoother is a filter of the size 3 x 3 that can be applied to each
    cell of an image by rounding down the average of the cell and the eight
    surrounding cells (i.e., the average of the nine cells in the blue
    smoother). If one or more of the surrounding cells of a cell is not
    present, we do not consider it in the average (i.e., the average of the
    four cells in the red smoother). Given an m x n integer matrix img
    representing the grayscale of an image, return the image after applying the
    smoother on each cell of it.
Link: https://leetcode.com/problems/image-smoother/
Notes:
    - since there is a constraint of 0 <= img[i][j] <= 255
    - use bit manipulation to store smoothed value in place
"""
def imageSmoother(img: list[list[int]]) -> list[list[int]]:
    M, N = len(img), len(img[0])

    for r in range(M):
        for c in range(N):
            total = count = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if 0 <= i < M and 0 <= j < N:
                        # Extract the original value of img[i][j]
                        total += img[i][j] & 255
                        count += 1
            # Encode the smoothed value in img[i][j]
            img[r][c] |= (total // count) << 8
    for r in range(M):
        for c in range(N):
            # Extract the smoothed value of img[i][j]
            img[r][c] >>= 8
    return img

if __name__ == '__main__':
    i1 = [[1,1,1],[1,0,1],[1,1,1]]
    i2 = [[100,200,100],[200,50,200],[100,200,100]]

    print(imageSmoother(i1))
    print(imageSmoother(i2))

