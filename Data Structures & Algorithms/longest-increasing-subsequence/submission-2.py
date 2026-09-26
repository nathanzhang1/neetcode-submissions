class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        
        def findLIS(start):
            if start == len(nums) - 1:
                return 1
            if memo[start] != -1:
                return memo[start]
            
            max_LIS = 1
            for i in range(start+1, len(nums)):
                if nums[start] < nums[i]:
                    max_LIS = max(max_LIS, 1 + findLIS(i))
            
            memo[start] = max_LIS

            return max_LIS
        
        return max(findLIS(i) for i in range(len(nums)))