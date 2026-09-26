class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        curMax = float('-inf')

        for num in nums:
            curSum = max(curSum + num, num)
            curMax = max(curMax, curSum)
        
        return curMax