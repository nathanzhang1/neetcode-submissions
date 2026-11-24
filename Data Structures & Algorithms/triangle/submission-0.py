class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        dp = [[0] * len(triangle[-1]) for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1):
                if i == n-1:
                    dp[i][j] = triangle[i][j]
                    continue
                
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]

            
# Brute force DFS:
    # Check every path and update when get to bottom

# Base case: at row n-1 cell j, dp[n-1][j] = triangle[n-1][j]
# Recurrence relation: at row i cell j, dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
# Bottom up DP:
    # Outer loop: bottom row to top
    # Inner loop: left cell to right