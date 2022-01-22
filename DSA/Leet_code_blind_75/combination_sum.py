class Solution
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [None for i in range(len(target+1))]
        dp[0] = []

        for i in range(target+1):
            if dp[i] != None:
                for num in candidates:
                    if ((i+num) <= target):
                        dp[i+num] = [*dp[i], dp[num]


        return dp[target]
