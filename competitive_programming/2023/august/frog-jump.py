'''
Created Date: 2023-08-27
Qn: A frog is crossing a river. The river is divided into some number of units,
    and at each unit, there may or may not exist a stone. The frog can jump on
    a stone, but it must not jump into the water.

    Given a list of stones' positions (in units) in sorted ascending order,
    determine if the frog can cross the river by landing on the last stone.
    Initially, the frog is on the first stone and assumes the first jump must
    be 1 unit.

    If the frog's last jump was k units, its next jump must be either k - 1, k,
    or k + 1 units. The frog can only jump in the forward direction.
Link: https://leetcode.com/problems/frog-jump/
Notes:
    - use dp
'''
def canCross(stones: list[int]) -> bool:
    N = len(stones)
    mark = {stone: i for i, stone in enumerate(stones)}
    dp = [[False] * (N+1) for _ in range(N)]
    dp[0][0] = True

    for index in range(N):
        for prev_jump in range(N+1):
            if dp[index][prev_jump]:
                if stones[index] + prev_jump in mark:
                    dp[mark[stones[index] + prev_jump]][prev_jump] = True
                if stones[index] + prev_jump + 1 in mark:
                    dp[mark[stones[index] + prev_jump + 1]][prev_jump + 1] = True
                if stones[index] + prev_jump - 1 in mark:
                    dp[mark[stones[index] + prev_jump - 1]][prev_jump - 1] = True

    return any(n for n in dp[N-1])

if __name__ == '__main__':
    s1 = [0,1,3,5,6,8,12,17]
    s2 = [0,1,2,3,4,8,9,11]

    print(canCross(s1))
    print(canCross(s2))
