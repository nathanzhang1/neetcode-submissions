class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        memo = [[float('inf')] * 2 for _ in range(n)]
        
        def dfs(i, canBuy):
            if i >= n:
                return 0
            
            if memo[i][canBuy] != float('inf'):
                return memo[i][canBuy]
            
            if canBuy == 0:
                buy = -prices[i] + dfs(i+1, 1) 
                noBuy = dfs(i+1, 0)
                memo[i][0] = max(buy, noBuy)
                return memo[i][0]
            else:
                sell = prices[i] + dfs(i+2, 0)
                noSell = dfs(i+1, 1)
                memo[i][1] = max(sell, noSell)
                return memo[i][1]
        
        return dfs(0, 0)

# Recursion and memoization:
# Memo captures [day_i][canBuy]