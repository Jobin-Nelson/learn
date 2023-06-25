'''
Created Date: 2023-06-24
Qn: You are installing a billboard and want it to have the largest height. The
    billboard will have two steel supports, one on each side. Each steel
    support must be an equal height.

    You are given a collection of rods that can be welded together. For
    example, if you have rods of lengths 1, 2, and 3, you can weld them
    together to make a support of length 6.

    Return the largest possible height of your billboard installation. If you
    cannot support the billboard, return 0.
Link: https://leetcode.com/problems/tallest-billboard/
Notes:
    - split the rods in half
    - create a dict of {diff: left}
'''
def tallestBillboard(rods: list[int]) -> int:
    def helper(half_rods: list[int]) -> dict[int, int]:
        states = set()
        states.add((0,0))
        for r in half_rods:
            new_states = set()
            for left, right in states:
                new_states.add((left + r, right))
                new_states.add((left, right + r))
            states |= new_states

        dp = dict()
        for left, right in states:
            dp[left-right] = max(dp.get(left-right, 0), left)
        return dp

    N = len(rods)
    first_half = helper(rods[:N//2])
    second_half = helper(rods[N//2:])

    res = 0
    for diff in first_half:
        if -diff in second_half:
            res = max(res, first_half[diff] + second_half[-diff])
    return res

if __name__ == '__main__':
    r1 = [1,2,3,6]
    r2 = [1,2,3,4,5,6]

    print(tallestBillboard(r1))
    print(tallestBillboard(r2))
