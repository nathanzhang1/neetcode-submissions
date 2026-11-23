class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        memo = {}

        def dfs(i, curSum):
            if curSum == amount:
                return 1
            
            if curSum > amount:
                return 0
            
            if (i, curSum) in memo:
                return memo[(i, curSum)]   
            
            ways = 0
            for j in range(i, n):
                ways += dfs(j, curSum + coins[j])

            memo[(i, curSum)] = ways
            return ways

        return dfs(0, 0)


# Recursion and memoization with DFS
# Dfs(i, curSum) where i = starting point of currently available coins, curSum = current value
# Recursive call: for j in range(i, n-1): dfs(j, curSum + coins[j])