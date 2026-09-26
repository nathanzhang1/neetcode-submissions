class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left_index = 0
        right_index = 1

        while right_index < len(prices):
            maxProfit = max(prices[right_index]-prices[left_index], maxProfit)
            if (prices[right_index] < prices[left_index]):
                left_index = right_index
            right_index += 1
        
        return maxProfit