class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(n+1):
            if i == 0:
                dp[i] = 0
                continue
            if i == 1 or i == 2:
                dp[i] = 1
                continue
            
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

        return dp[n]