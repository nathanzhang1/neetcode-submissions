class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = {}
        
        for i in range(amount+1):
            for j in range(n-1, -1, -1):
                if i == 0:
                    dp[(i, j)] = 1
                    continue
                
                first = dp[(i, j+1)] if j+1 < n else 0
                second = dp[(i - coins[j], j)] if i-coins[j] >= 0 else 0

                dp[(i, j)] = first + second
        
        return dp[(amount, 0)]