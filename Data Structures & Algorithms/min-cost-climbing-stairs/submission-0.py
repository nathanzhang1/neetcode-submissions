class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        
        for i in range(len(cost) + 1):
            if i == 0 or i == 1:
                dp[i] = 0
                continue
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[len(cost)]