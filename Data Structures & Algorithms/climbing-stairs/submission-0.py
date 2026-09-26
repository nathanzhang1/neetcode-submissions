class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        if n <= 2:
            return memo[n]

        for i in range(3, n+1):
            n_i = memo[i-1] + memo[i-2]
            memo[i] = n_i
        
        return memo[n]