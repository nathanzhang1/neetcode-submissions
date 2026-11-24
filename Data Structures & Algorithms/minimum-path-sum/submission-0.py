class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[i][j] = grid[i][j]
                    continue
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]

# Base case: dp[m-1][n-1] = grid[m-1][n-1]
# Recurrence: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
# 