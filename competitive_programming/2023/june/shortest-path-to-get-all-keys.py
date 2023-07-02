'''
Created Date: 2023-06-29
Qn: You are given an m x n grid grid where:

        - '.' is an empty cell. 
        - '#' is a wall. 
        - '@' is the starting point.
        - Lowercase letters represent keys. 
        - Uppercase letters represent locks.

    You start at the starting point and one move consists of walking one space
    in one of the four cardinal directions. You cannot walk outside the grid,
    or walk into a wall.

    If you walk over a key, you can pick it up and you cannot walk over a lock
    unless you have its corresponding key.

    For some 1 <= k <= 6, there is exactly one lowercase and one uppercase
    letter of the first k letters of the English alphabet in the grid. This
    means that there is exactly one key for each lock, and one lock for each
    key; and also that the letters used to represent the keys and locks were
    chosen in the same order as the English alphabet.

    Return the lowest number of moves to acquire all keys. If it is impossible,
    return -1.
Link: https://leetcode.com/problems/shortest-path-to-get-all-keys/
Notes:
'''
from collections import deque, defaultdict

def shortestPathAllKeys(grid: list[str]) -> int:
    M, N = len(grid), len(grid[0])
    key_set, lock_set = set(), set()
    all_keys = 0
    start_r, start_c = -1, -1

    for i in range(M):
        for j in range(N):
            cell = grid[i][j]
            if cell in 'abcdef':
                all_keys += (1 << (ord(cell) - ord('a')))
                key_set.add(cell)
            elif cell in 'ABCDEF':
                lock_set.add(cell)
            elif cell == '@':
                start_r, start_c = i, j
    q = deque([(start_r, start_c, 0, 0)])
    seen = defaultdict(set)
    seen[0].add((start_r, start_c))
    dirs = [0, 1, 0, -1, 0]

    while q:
        r, c, k, d = q.popleft()
        for i in range(1, 5):
            nr, nc = r + dirs[i-1], c + dirs[i]
            if 0<=nr<M and 0<=nc<N and grid[nr][nc] != '#':
                cell = grid[nr][nc]
                if cell in key_set and not ((1 << (ord(cell) - ord('a')) & k)):
                    new_keys = (k | (1 << (ord(cell) - ord('a'))))
                    if new_keys == all_keys: return d + 1
                    seen[k].add((nr, nc))
                    q.append((nr, nc, new_keys, d+1))
                elif cell in lock_set and not (k & (1 << (ord(cell) - ord('A')))):
                    continue
                if (nr, nc) not in seen[k]:
                    seen[k].add((nr, nc))
                    q.append((nr, nc, k, d+1))
    return -1

if __name__ == '__main__':
    g1 = ["@.a..","###.#","b.A.B"]
    g2 = ["@..aA","..B#.","....b"]
    g3 = ["@Aa"]

    print(shortestPathAllKeys(g1))
    print(shortestPathAllKeys(g2))
    print(shortestPathAllKeys(g3))
