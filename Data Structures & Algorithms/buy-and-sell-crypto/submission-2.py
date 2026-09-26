class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy = 1
        max_profit = 0
        while buy != len(prices):
            profit = prices[buy] - prices[sell]
            if profit < 0:
                sell = buy
            if profit > max_profit:
                max_profit = profit
            buy += 1
        return max_profit

        
# Sliding window: increment right and set left = right when right < left, keeping track of max profit
# DP: iterate and keep track of lowest point and max profit