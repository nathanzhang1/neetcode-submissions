class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[1:]
        nums2 = nums[:-1]

        if len(nums) == 1:
            return nums[0]

        def robX(nums):
            memo = [-1] * len(nums)

            def dfs(i):
                if i >= len(nums):
                    return 0

                if memo[i] != -1:
                    return memo[i]

                memo[i] = max(dfs(i+2) + nums[i], dfs(i+1))

                return memo[i]
            
            return dfs(0)
        
        return max(robX(nums1), robX(nums2))