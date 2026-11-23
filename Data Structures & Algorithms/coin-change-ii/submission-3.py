class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [[0] * (n+1) for _ in range(amount+1)]
        
        for i in range(amount+1):
            for j in range(n-1, -1, -1):
                if i == 0:
                    dp[i][j] = 1
                    continue
                
                first = dp[i][j+1] if j+1 < n else 0
                second = dp[i - coins[j]][j] if i-coins[j] >= 0 else 0

                dp[i][j] = first + second
        
        return dp[amount][0]

        # n = len(coins)
        # memo = {}

        # def dfs(i, curSum):
        #     if curSum == amount:
        #         return 1
            
        #     if curSum > amount:
        #         return 0
            
        #     # if (i, curSum) in memo:
        #     #     return memo[(i, curSum)]   
            
        #     ways = 0
        #     for j in range(i, n):
        #         subp = curSum + coins[j]
        #         if (j, subp) in memo:
        #             ways += memo[j, subp]
        #         else:
        #             ways += dfs(j, curSum + coins[j])

        #     memo[(i, curSum)] = ways
        #     return ways

        # return dfs(0, 0)


# Recursion and memoization with DFS
# Dfs(i, curSum) where i = starting point of currently available coins, curSum = current value
# Recursive call: for j in range(i, n-1): dfs(j, curSum + coins[j])