'''
Created Date: 2023-08-06
Qn: Your music player contains n different songs. You want to listen to goal
    songs (not necessarily different) during your trip. To avoid boredom, you
    will create a playlist so that:

        - Every song is played at least once.
        - A song can only be played again only if k other songs have been
          played.

    Given n, goal, and k, return the number of possible playlists that you can
    create. Since the answer can be very large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/number-of-music-playlists/
Notes:
    - use dp
'''
def numMusicPlaylists(n: int, goal: int, k: int) -> int:
    mod = 10**9 + 7

    dp = [[0] * (n+1) for _ in range(goal+1)]
    dp[0][0] = 1

    for i in range(1, goal + 1):
        for j in range(1, min(i,n) + 1):
            dp[i][j] = dp[i-1][j-1] * (n-j+1) % mod
            if j > k:
                dp[i][j] = (dp[i][j] + dp[i-1][j] * (j-k)) % mod
    return dp[goal][n]

if __name__ == '__main__':
    n1, g1, k1 = 3, 3, 1
    n2, g2, k2 = 2, 3, 0
    n3, g3, k3 = 2, 3, 1

    print(numMusicPlaylists(n1, g1, k1))
    print(numMusicPlaylists(n2, g2, k2))
    print(numMusicPlaylists(n3, g3, k3))

