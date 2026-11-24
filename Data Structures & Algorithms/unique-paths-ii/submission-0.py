class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1 and obstacleGrid[i][j] == 0:
                    dp[i][j] = 1
                    continue

                down = dp[i+1][j] if i+1 < m and obstacleGrid[i+1][j] == 0 else 0
                right = dp[i][j+1] if j+1 < n and obstacleGrid[i][j+1] == 0 else 0
                dp[i][j] = down + right
        
        return dp[0][0] if obstacleGrid[0][0] == 0 else 0

# Modify such that we check whether down or right contains an obstacle if so ignore it (count it as 0)