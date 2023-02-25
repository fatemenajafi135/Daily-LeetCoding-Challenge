'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Easy
Approach: Greedy
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        current_min = prices[0]
        
        for value in prices[1:]:
            
            if value > current_min:
                max_profit = max(max_profit, value - current_min)
            else:
                current_min = value
        
        return max_profit