'''
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
Easy
Approach: :)
'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = (high - low) // 2
        return diff + 1 if  high % 2 == 1 or low % 2 == 1 else diff