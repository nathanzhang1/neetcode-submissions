class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        globalMax = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            prevMax, prevMin = maxProd, minProd
            maxProd = max(num, prevMax * num, prevMin * num)
            minProd = min(num, prevMax * num, prevMin * num)
            globalMax = max(globalMax, maxProd)
        
        return globalMax