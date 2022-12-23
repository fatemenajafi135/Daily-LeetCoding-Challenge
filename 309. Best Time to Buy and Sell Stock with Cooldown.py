'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
Medium
Approach: Dynamic Programming
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: 
            return 0
        prev_sell, sell, buy = 0, 0, -prices[0]
        for i in range(1, len(prices)): 
            prev_sell, sell, buy = sell, max(buy + prices[i], sell), max(prev_sell - prices[i], buy) 
        return max(sell, buy)
