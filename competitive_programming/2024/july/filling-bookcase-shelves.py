"""
Created Date: 2024-07-31
Qn: You are given an array books where books[i] = [thicknessi, heighti]
indicates the thickness and height of the ith book. You are also given an
integer shelfWidth.

    We want to place these books in order onto bookcase shelves that have a
    total width shelfWidth.

    We choose some of the books to place on this shelf such that the sum of
    their thickness is less than or equal to shelfWidth, then build another
    level of the shelf of the bookcase so that the total height of the bookcase
    has increased by the maximum height of the books we just put down. We
    repeat this process until there are no more books to place.

    Note that at each step of the above process, the order of the books we
    place is the same order as the given sequence of books.

    - For example, if we have an ordered list of 5 books, we might place the
      first and second book onto the first shelf, the third book on the second
      shelf, and the fourth and fifth book on the last shelf. 
    
    Return the minimum possible height that the total bookshelf can be after
    placing shelves in this manner.
Link: https://leetcode.com/problems/filling-bookcase-shelves/
Notes:
    - use dp
"""

from sys import maxsize


def minHeightShelves(books: list[list[int]], shelfWidth: int) -> int:
    dp = [0] * (len(books) + 1)
    for i in range(len(books) - 1, -1, -1):
        cur_width = shelfWidth
        max_height = 0
        dp[i] = maxsize
        for j in range(i, len(books)):
            width, height = books[j]
            if cur_width < width:
                break
            cur_width -= width
            max_height = max(max_height, height)
            dp[i] = min(
                dp[i],
                dp[j + 1] + max_height,
            )
    return dp[0]

    # Not working but close dfs solution
    # def dfs(i: int, cur_width: int, cur_height: int) -> int:
    #     if i == len(books): return cur_height
    #     book_width, book_height = books[i]
    #     if book_width + cur_width > shiftWidth:
    #         return dfs(i+1, cur_width, book_height) + cur_height
    #     cur_max_height = max(cur_height, book_height)
    #     return min(
    #         dfs(i+1, cur_width + book_width, cur_max_height),
    #         dfs(i+1, book_width, book_height) + cur_height,
    #     )
    # return dfs(0, 0, 0)


if __name__ == '__main__':
    b1, s1 = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4
    b2, s2 = [[1, 3], [2, 4], [3, 2]], 6

    print(minHeightShelves(b1, s1))
    print(minHeightShelves(b2, s2))
