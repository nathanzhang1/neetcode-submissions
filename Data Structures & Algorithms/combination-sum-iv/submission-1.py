class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [-1 for _ in range(target+1)]
        dp[0] = 1

        for i in range(1, target+1):
            curSum = 0
            for num in nums:
                if i - num >= 0:
                    curSum += dp[i - num]
            dp[i] = curSum
        
        return dp[target]

        # def dfs(curSum):
        #     if curSum > target:
        #         return 0
            
        #     if curSum == target:
        #         return 1
            
        #     if dp[curSum] != -1:
        #         return dp[curSum]
            
        #     combs = 0
        #     for num in nums:
        #         combs += dfs(curSum + num)
            
        #     dp[curSum] = combs
        #     return combs
        
        # return dfs(0)