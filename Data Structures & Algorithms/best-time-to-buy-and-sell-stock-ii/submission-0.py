class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        for i, p in enumerate(prices):
            if i == len(prices) - 1:
                break
            if p < prices[i+1]:
                output += prices[i+1] - p
        return output