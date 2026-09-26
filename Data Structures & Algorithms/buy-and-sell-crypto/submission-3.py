class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 100000
        maxProfit = 0
        for p in prices:
            minPrice = min(minPrice, p)
            maxProfit = max(maxProfit, p - minPrice)
        return maxProfit