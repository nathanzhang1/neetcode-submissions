class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[i][j] = 1
                    continue

                down = dp[i+1][j] if i+1 < m else 0
                right = dp[i][j+1] if j+1 < n else 0
                dp[i][j] = down + right
        
        return dp[0][0]
        


# Base case: dp[m-1][n-1] = 1
# Recurrence relation: dp[i][j] = dp[i+1][j] + dp[i][j+1]