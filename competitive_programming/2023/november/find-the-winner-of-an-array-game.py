'''
Created Date: 2023-11-05
Qn: Given an integer array arr of distinct integers and an integer k.

    A game will be played between the first two elements of the array (i.e.
    arr[0] and arr[1]). In each round of the game, we compare arr[0] with
    arr[1], the larger integer wins and remains at position 0, and the smaller
    integer moves to the end of the array. The game ends when an integer wins k
    consecutive rounds.

    Return the integer which will win the game.

    It is guaranteed that there will be a winner of the game.
Link: https://leetcode.com/problems/find-the-winner-of-an-array-game/
Notes:
    - use simulation or iterate till you find the max or winsteak == k
'''
def getWinner(arr: list[int], k: int) -> int:
    max_element = max(arr)
    cur, winstreak = arr[0], 0
    for i in range(1, len(arr)):
        opponent = arr[i]
        if cur < opponent:
            cur = opponent
            winstreak = 1
        else:
            winstreak += 1
        if winstreak == k or cur == max_element:
            return cur
    return -1
    #queue simulation
    # q = deque(arr[1:])
    # w, win_times = arr[0], 0
    # while True:
    #     if w > q[0]:
    #         win_times += 1
    #         q.append(q.popleft())
    #     else:
    #         win_times = 1
    #         q.append(w)
    #         w = q.popleft()
    #     if win_times == k: return w

if __name__ == '__main__':
    a1, k1 = [2,1,3,5,4,6,7], 2
    a2, k2 = [3, 2, 1], 10

    print(getWinner(a1, k1))
    print(getWinner(a2, k2))
